#!/usr/bin/env python3
"""Auditoria determinística e somente leitura dos HTMLs de aula.

Aceita caminhos explícitos ou ``--intervalo INICIO-FIM``. Usa apenas a biblioteca
padrão, não escreve arquivos e retorna 1 quando qualquer aula falha.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


SCRIPT = Path(__file__).resolve()
REPO = SCRIPT.parents[2]
CONFIG = REPO / "squad-revisao-aulas/config"


def load_json_yaml(path: Path) -> dict:
    """Lê o subconjunto JSON de YAML 1.2 usado pelo squad."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ERRO: configuração inválida em {path}: {exc}") from exc


@dataclass
class Node:
    tag: str
    attrs: dict[str, str | None]
    classes: set[str]
    text: list[str] = field(default_factory=list)


class LessonParser(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[Node] = []
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.headings: list[str] = []
        self.pauses = 0
        self.details: list[dict[str, object]] = []
        self.activity_cards: list[str | None] = []
        self.plan_minutes: list[int] = []
        self.sections: set[str] = set()
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs_list)
        classes = set((attrs.get("class") or "").split())
        node = Node(tag, attrs, classes)
        if tag not in self.VOID:
            self.stack.append(node)
        if ident := attrs.get("id"):
            self.ids.append(ident)
            if tag == "section":
                self.sections.add(ident)
        if tag == "a" and attrs.get("href"):
            self.hrefs.append(attrs["href"] or "")
        if tag == "aside" and ({"pause", "pause-box"} & classes):
            self.pauses += 1
        if tag == "details":
            self.details.append({"open": "open" in attrs, "text": [], "blocks": 0})
        if tag == "div" and "activity-card" in classes:
            gabarito_attr = attrs.get("data-gabarito")
            self.activity_cards.append(gabarito_attr)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        for node in self.stack:
            node.text.append(data)
        if self.details:
            for detail in self.details:
                if any(node.tag == "details" for node in self.stack):
                    detail["text"].append(data)  # type: ignore[union-attr]

    def handle_endtag(self, tag: str) -> None:
        if tag in self.VOID:
            return
        if not self.stack:
            self.errors.append(f"fechamento </{tag}> sem abertura")
            return
        pos = next((i for i in range(len(self.stack) - 1, -1, -1) if self.stack[i].tag == tag), None)
        if pos is None:
            self.errors.append(f"fechamento </{tag}> sem abertura compatível")
            return
        while len(self.stack) - 1 > pos:
            orphan = self.stack.pop()
            self.errors.append(f"elemento <{orphan.tag}> não fechado antes de </{tag}>")
        node = self.stack.pop()
        text = " ".join("".join(node.text).split())
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(text)
        if ({"time", "tl-duration"} & node.classes):
            match = re.fullmatch(r"\s*(\d+)\s*min(?:utos?)?\s*", text, re.I)
            if match and self._inside_plan():
                self.plan_minutes.append(int(match.group(1)))
        if self.details and tag in {"p", "li", "dd"} and self._inside_details():
            self.details[-1]["blocks"] = int(self.details[-1]["blocks"]) + (1 if text else 0)

    def close(self) -> None:
        super().close()
        for node in self.stack:
            self.errors.append(f"elemento <{node.tag}> não fechado")

    def _inside_details(self) -> bool:
        return any(node.tag == "details" for node in self.stack)

    def _inside_plan(self) -> bool:
        for node in self.stack:
            ident = node.attrs.get("id") or ""
            if node.tag == "section" and ident in {"plano", "plano-aula"}:
                return True
        return False


def normalize_text(parts: list[str]) -> str:
    return " ".join("".join(parts).split())


def resolve_local_link(html: Path, href: str) -> Path | None:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or href.startswith("mailto:"):
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    if path.startswith("/"):
        return REPO / path.lstrip("/")
    return html.parent / path


def expected_navigation(path: Path) -> tuple[str | None, str | None]:
    match = re.fullmatch(r"aula-(\d{2})\.html", path.name)
    if not match:
        return None, None
    number = int(match.group(1))
    previous = f"aula-{number - 1:02d}.html" if number > 1 else None
    following = f"aula-{number + 1:02d}.html" if number < 60 else None
    return previous, following


def audit(path: Path, criteria: dict) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    notes: list[str] = []
    if not path.is_file():
        return ["arquivo inexistente"], notes
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"não foi possível ler UTF-8: {exc}"], notes

    parser = LessonParser()
    try:
        parser.feed(source)
        parser.close()
    except Exception as exc:  # HTMLParser can surface malformed declarations
        failures.append(f"falha de parsing HTML: {exc}")

    lower = source.lower()
    if not re.search(r"<!doctype\s+html", source, re.I):
        failures.append("DOCTYPE HTML ausente")
    for required in ("<html", "<head", "<body", "</body>", "</html>"):
        if required not in lower:
            failures.append(f"estrutura básica ausente: {required}")
    failures.extend(parser.errors)

    min_pauses = int(criteria["texto_base"].get("pausas_minimas", 0))
    max_pauses = int(criteria["texto_base"].get("pausas_maximas", 99))
    if not (min_pauses <= parser.pauses <= max_pauses):
        failures.append(
            f"pausas: esperado entre {min_pauses} e {max_pauses}, encontrado {parser.pauses}"
        )

    expected_minutes = int(criteria["plano"]["minutos_exatos"])
    total = sum(parser.plan_minutes)
    if not parser.plan_minutes:
        failures.append("tempos do plano não encontrados em #plano ou #plano-aula")
    elif total != expected_minutes:
        failures.append(f"plano: esperado {expected_minutes} min, encontrado {total} min")

    duplicate_ids = sorted({ident for ident in parser.ids if parser.ids.count(ident) > 1})
    if duplicate_ids:
        failures.append("IDs duplicados: " + ", ".join(duplicate_ids))
    fragments = [unquote(urlsplit(href).fragment) for href in parser.hrefs if urlsplit(href).fragment]
    missing_fragments = sorted({frag for frag in fragments if frag not in parser.ids})
    if missing_fragments:
        failures.append("fragmentos sem destino: " + ", ".join(missing_fragments))

    missing_links: list[str] = []
    for href in parser.hrefs:
        target = resolve_local_link(path, href)
        if target is not None and not target.exists():
            missing_links.append(href)
    if missing_links:
        failures.append("links locais inexistentes: " + ", ".join(sorted(set(missing_links))))

    previous, following = expected_navigation(path)
    local_names = {Path(urlsplit(href).path).name for href in parser.hrefs}
    if previous and previous not in local_names:
        failures.append(f"navegação anterior ausente: {previous}")
    if following and following not in local_names:
        failures.append(f"navegação seguinte ausente: {following}")
    if not previous and "aula-00.html" in local_names:
        failures.append("Aula 01 contém navegação anterior inválida")
    if not following and "aula-61.html" in local_names:
        failures.append("Aula 60 contém navegação seguinte inválida")

    if "texto-base" not in parser.ids:
        failures.append("seção #texto-base ausente")
    if "atividade" not in parser.ids:
        failures.append("seção #atividade ausente")

    gabarito_required = "obrigatorio" in parser.activity_cards
    if gabarito_required and len(parser.details) != 1:
        failures.append(
            f"<details>: atividade desta aula está marcada data-gabarito=\"obrigatorio\", "
            f"esperado exatamente 1, encontrado {len(parser.details)}"
        )
    elif not gabarito_required and len(parser.details) > 1:
        failures.append(
            f"<details>: no máximo 1 esperado quando a atividade não é "
            f"data-gabarito=\"obrigatorio\", encontrado {len(parser.details)}"
        )
    elif len(parser.details) == 1:
        detail = parser.details[0]
        if detail["open"]:
            failures.append("<details> está aberto por padrão")
        text = normalize_text(detail["text"])  # type: ignore[arg-type]
        word_count = len(re.findall(r"\b[\wÀ-ÿ'-]+\b", text, re.UNICODE))
        minimum = int(criteria["atividade"]["gabarito_minimo_palavras"])
        if word_count < minimum or int(detail["blocks"]) < 2:
            failures.append(
                f"gabarito sem conteúdo substantivo: {word_count} palavras, "
                f"{detail['blocks']} blocos (mínimo {minimum} palavras e 2 blocos)"
            )
        notes.append(f"gabarito: {word_count} palavras em {detail['blocks']} blocos")
    else:
        notes.append("gabarito: dispensado nesta aula (atividade leve)")

    if any(not heading.strip() for heading in parser.headings):
        failures.append("subtítulo vazio encontrado")

    for placeholder in criteria["placeholders_proibidos"]:
        if placeholder.isupper() and placeholder.isalpha():
            found = re.search(rf"(?<!\w){re.escape(placeholder)}(?!\w)", source) is not None
        else:
            found = placeholder.lower() in lower
        if found:
            failures.append(f"placeholder encontrado: {placeholder!r}")

    overflow_ok = bool(
        re.search(r"overflow-x\s*:\s*(?:clip|hidden|auto)", source, re.I)
        and ("overflow-wrap" in lower or "word-break" in lower)
    )
    if not overflow_ok:
        failures.append("proteção contra overflow insuficiente")
    if not re.search(r"@media\s+print", source, re.I):
        failures.append("regra @media print ausente")
    if not re.search(r"@media\s*\([^)]*max-width", source, re.I):
        failures.append("breakpoint responsivo max-width ausente")

    notes.extend(
        [
            f"pausas: {parser.pauses}",
            f"plano: {total} min",
            f"IDs: {len(parser.ids)} únicos" if not duplicate_ids else f"IDs: {len(parser.ids)}",
            f"fragmentos: {len(fragments)} válidos" if not missing_fragments else f"fragmentos: {len(fragments)}",
        ]
    )
    return failures, notes


def parse_interval(value: str) -> tuple[int, int]:
    match = re.fullmatch(r"(\d{1,2})-(\d{1,2})", value)
    if not match:
        raise argparse.ArgumentTypeError("use INICIO-FIM, por exemplo 01-23")
    start, end = map(int, match.groups())
    if not (1 <= start <= end <= 60):
        raise argparse.ArgumentTypeError("intervalo deve estar entre 01 e 60")
    return start, end


def main(argv: list[str] | None = None) -> int:
    argp = argparse.ArgumentParser(description=__doc__)
    argp.add_argument("arquivos", nargs="*", type=Path, help="HTMLs a auditar")
    argp.add_argument("--intervalo", type=parse_interval, help="intervalo INICIO-FIM")
    args = argp.parse_args(argv)
    if not args.arquivos and not args.intervalo:
        argp.error("informe ao menos um arquivo ou --intervalo")

    course = load_json_yaml(CONFIG / "curso.yaml")
    criteria = load_json_yaml(CONFIG / "criterios.yaml")
    paths = [path if path.is_absolute() else REPO / path for path in args.arquivos]
    if args.intervalo:
        start, end = args.intervalo
        lesson_dir = REPO / course["diretorio_aulas"]
        paths.extend(lesson_dir / course["padrao_arquivo"].format(numero=n) for n in range(start, end + 1))

    seen: set[Path] = set()
    failed = 0
    for path in paths:
        path = path.resolve()
        if path in seen:
            continue
        seen.add(path)
        failures, notes = audit(path, criteria)
        label = path.relative_to(REPO) if path.is_relative_to(REPO) else path
        if failures:
            failed += 1
            print(f"FALHA {label}")
            for item in failures:
                print(f"  - {item}")
        else:
            print(f"OK    {label}")
        for note in notes:
            print(f"      {note}")

    print(f"\nResumo: {len(seen) - failed} aprovada(s), {failed} com falha(s), {len(seen)} auditada(s).")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
