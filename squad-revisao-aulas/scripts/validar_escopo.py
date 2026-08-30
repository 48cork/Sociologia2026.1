#!/usr/bin/env python3
"""Captura e valida o escopo Git de uma ou mais aulas do mesmo gate.

``capturar`` grava um baseline JSON a pedido do orquestrador. ``validar`` compara o
estado atual, hashes de todas as aulas e caminhos modificados. O script nunca edita HTML,
nunca executa stage e nunca restaura alterações.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


SCRIPT = Path(__file__).resolve()
REPO = SCRIPT.parents[2]
CONFIG = REPO / "squad-revisao-aulas/config/curso.yaml"


def load_course() -> dict:
    try:
        return json.loads(CONFIG.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ERRO: configuração inválida: {exc}") from exc


def git(*args: str) -> bytes:
    result = subprocess.run(
        ["git", *args], cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", "replace").strip())
    return result.stdout


GLOB_CHARS = set("*?[]{}")
SHA256_RE = re.compile(r"[0-9a-f]{64}")


def repo_relative(raw: str | Path, *, must_exist: bool = False) -> str:
    raw_text = str(raw)
    if any(char in raw_text for char in GLOB_CHARS):
        raise ValueError(f"globs não são permitidos: {raw}")
    path = Path(raw)
    if ".." in path.parts:
        raise ValueError(f"caminho com '..' não é permitido: {raw}")
    absolute = path.resolve() if path.is_absolute() else (REPO / path).resolve()
    try:
        relative = absolute.relative_to(REPO)
    except ValueError as exc:
        raise ValueError(f"caminho fora do repositório: {raw}") from exc
    if must_exist and not absolute.is_file():
        raise ValueError(f"arquivo inexistente: {raw}")
    return relative.as_posix()


def lesson_path(raw: str | Path, course: dict) -> tuple[str, int]:
    relative = repo_relative(raw, must_exist=True)
    lesson_dir = course["diretorio_aulas"].rstrip("/")
    match = re.fullmatch(rf"{re.escape(lesson_dir)}/aula-(\d{{2}})\.html", relative)
    if not match:
        raise ValueError(f"aula deve seguir {lesson_dir}/aula-NN.html: {raw}")
    absolute = REPO / relative
    if not absolute.is_file():
        raise ValueError(f"aula deve ser arquivo regular: {raw}")
    number = int(match.group(1))
    if not 1 <= number <= int(course["total_aulas"]):
        raise ValueError(f"número de aula fora do curso: {number:02d}")
    return relative, number


def authorized_lessons(args: argparse.Namespace, course: dict) -> list[str]:
    raw_items = list(getattr(args, "autorizar_aula", []) or [])
    legacy = getattr(args, "arquivo", None)
    if legacy:
        raw_items.append(legacy)
    if not raw_items:
        raise ValueError("informe --autorizar-aula (repetível) ou --arquivo")
    resolved: list[tuple[str, int]] = [lesson_path(raw, course) for raw in raw_items]
    paths = [path for path, _ in resolved]
    if len(paths) != len(set(paths)):
        raise ValueError("aula autorizada repetida")
    numbers = {number for _, number in resolved}
    gates = [set(map(int, gate)) for gate in course.get("gates_commit", [])]
    if not any(numbers <= gate for gate in gates):
        raise ValueError("aulas autorizadas não pertencem ao mesmo gate configurado")
    start, end = course["aulas_processamento_inicial"]
    if any(not start <= number <= end for number in numbers):
        raise ValueError(f"aula somente leitura; faixa gravável: {start:02d}-{end:02d}")
    return paths


def parse_approved_hashes(values: list[str], authorized: set[str], course: dict) -> dict[str, str]:
    approved: dict[str, str] = {}
    for value in values:
        if "=" not in value:
            raise ValueError("--hash-aprovado exige CAMINHO=SHA256")
        raw_path, digest = value.rsplit("=", 1)
        path, _ = lesson_path(raw_path, course)
        digest = digest.lower()
        if path not in authorized:
            raise ValueError(f"hash aprovado informado para aula não autorizada: {path}")
        if not SHA256_RE.fullmatch(digest):
            raise ValueError(f"SHA-256 aprovado inválido para {path}")
        if path in approved:
            raise ValueError(f"hash aprovado repetido para {path}")
        approved[path] = digest
    return approved


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def lesson_hashes(course: dict) -> dict[str, str]:
    directory = REPO / course["diretorio_aulas"]
    result: dict[str, str] = {}
    for number in range(1, int(course["total_aulas"]) + 1):
        path = directory / course["padrao_arquivo"].format(numero=number)
        if not path.is_file():
            raise RuntimeError(f"aula inexistente: {path.relative_to(REPO)}")
        result[path.relative_to(REPO).as_posix()] = sha256(path)
    return result


def status_entries() -> dict[str, str]:
    raw = git("status", "--porcelain=v1", "-z", "--untracked-files=all")
    chunks = raw.split(b"\0")
    entries: dict[str, str] = {}
    index = 0
    while index < len(chunks):
        chunk = chunks[index]
        index += 1
        if not chunk:
            continue
        text = chunk.decode("utf-8", "surrogateescape")
        code, path = text[:2], text[3:]
        if "R" in code or "C" in code:
            if index >= len(chunks):
                raise RuntimeError("status Git truncado em rename/copy")
            destination = chunks[index].decode("utf-8", "surrogateescape")
            index += 1
            entries[path] = code + " (origem)"
            entries[destination] = code + " (destino)"
        else:
            entries[path] = code
    return entries


def snapshot(authorized: list[str], approved: dict[str, str], course: dict) -> dict:
    return {
        "schema_version": 1,
        "capturado_em": datetime.now(timezone.utc).isoformat(),
        "repo": str(REPO),
        "head": git("rev-parse", "HEAD").decode().strip(),
        "branch": git("branch", "--show-current").decode().strip(),
        "arquivos_autorizados": authorized,
        "hashes_aprovados": approved,
        "git_status": status_entries(),
        "hashes_aulas": lesson_hashes(course),
    }


def allowed_path(path: str, exact: set[str], prefixes: set[str]) -> bool:
    if path in exact:
        return True
    return any(path == prefix or path.startswith(prefix.rstrip("/") + "/") for prefix in prefixes)


def capture(args: argparse.Namespace, course: dict) -> int:
    authorized = authorized_lessons(args, course)
    approved = parse_approved_hashes(args.hash_aprovado, set(authorized), course)
    initial_status = status_entries()
    dirty_authorized = set(authorized) & set(initial_status)
    missing_locks = dirty_authorized - set(approved)
    if missing_locks:
        raise ValueError(
            "aula já modificada exige --hash-aprovado: " + ", ".join(sorted(missing_locks))
        )
    for path, digest in approved.items():
        if sha256(REPO / path) != digest:
            raise ValueError(f"hash aprovado não coincide com o arquivo atual: {path}")
    output = Path(args.saida)
    output = output if output.is_absolute() else REPO / output
    output.resolve().relative_to(REPO)
    if output.exists():
        raise ValueError(f"baseline já existe e não será sobrescrito: {output.relative_to(REPO)}")
    output.parent.mkdir(parents=True, exist_ok=True)
    data = snapshot(authorized, approved, course)
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"BASELINE {output.relative_to(REPO)}")
    print(f"HEAD {data['head']}")
    print(f"AUTORIZADAS {', '.join(authorized)}")
    if approved:
        print("APROVADAS_BLOQUEADAS " + ", ".join(sorted(approved)))
    print(f"STATUS_INICIAL {len(data['git_status'])} caminho(s)")
    return 0


def validate(args: argparse.Namespace, course: dict) -> int:
    authorized = authorized_lessons(args, course)
    baseline_path = Path(args.baseline)
    baseline_path = baseline_path if baseline_path.is_absolute() else REPO / baseline_path
    try:
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"baseline inválido: {exc}") from exc
    baseline_authorized = baseline.get("arquivos_autorizados")
    if baseline_authorized is None and baseline.get("arquivo_autorizado"):
        baseline_authorized = [baseline["arquivo_autorizado"]]
    if baseline_authorized != authorized:
        raise ValueError("aulas autorizadas não coincidem com o baseline")
    approved = baseline.get("hashes_aprovados", {})
    if (
        not isinstance(approved, dict)
        or any(path not in authorized for path in approved)
        or any(not isinstance(digest, str) or not SHA256_RE.fullmatch(digest) for digest in approved.values())
    ):
        raise ValueError("hashes aprovados inválidos no baseline")

    exact = set(authorized)
    prefixes: set[str] = set()
    lesson_dir = course["diretorio_aulas"].rstrip("/") + "/"
    for raw in args.permitir:
        relative = repo_relative(raw)
        if relative.startswith(lesson_dir):
            raise ValueError("--permitir não pode autorizar outra aula")
        target = REPO / relative
        if target.exists() and target.is_dir():
            prefixes.add(relative)
        elif str(raw).endswith("/"):
            prefixes.add(relative)
        else:
            exact.add(relative)

    current_status = status_entries()
    initial_status = baseline.get("git_status", {})
    changed_paths = set(current_status) | set(initial_status)
    violations = sorted(path for path in changed_paths if not allowed_path(path, exact, prefixes))

    current_hashes = lesson_hashes(course)
    hash_violations: list[str] = []
    for path, old_hash in baseline.get("hashes_aulas", {}).items():
        if path in approved:
            if current_hashes.get(path) != approved[path]:
                hash_violations.append(path + " (hash aprovado alterado)")
            continue
        if path in authorized:
            continue
        if current_hashes.get(path) != old_hash:
            hash_violations.append(path)

    if violations or hash_violations:
        print("FALHA_TECNICA: escopo violado")
        for path in violations:
            print(f"  - caminho Git fora da allowlist: {path}")
        for path in hash_violations:
            print(f"  - hash de aula protegida alterado: {path}")
        print("Nenhum arquivo foi restaurado.")
        return 1

    print("ESCOPO_OK")
    print(f"AUTORIZADAS {', '.join(authorized)}")
    print(f"PROTEGIDAS {len(current_hashes) - len(authorized)} aula(s) com hash preservado")
    if approved:
        print("APROVADAS_BLOQUEADAS " + ", ".join(sorted(approved)))
    print(f"CAMINHOS_PERMITIDOS {', '.join(sorted(exact | prefixes))}")
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest="comando", required=True)
    capture_cmd = commands.add_parser("capturar", help="gravar baseline antes da escrita")
    capture_cmd.add_argument("--arquivo", help="compatibilidade: uma aula autorizada")
    capture_cmd.add_argument("--autorizar-aula", action="append", default=[], help="HTML de aula autorizado; repetível dentro do mesmo gate")
    capture_cmd.add_argument("--hash-aprovado", action="append", default=[], metavar="CAMINHO=SHA256", help="bloqueia aula já aprovada no hash informado")
    capture_cmd.add_argument("--saida", required=True)
    validate_cmd = commands.add_parser("validar", help="comparar estado depois da escrita")
    validate_cmd.add_argument("--arquivo", help="compatibilidade: uma aula autorizada")
    validate_cmd.add_argument("--autorizar-aula", action="append", default=[], help="HTML de aula autorizado; repetível dentro do mesmo gate")
    validate_cmd.add_argument("--baseline", required=True)
    validate_cmd.add_argument("--permitir", action="append", default=[], help="caminho adicional explícito")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    course = load_course()
    try:
        if args.comando == "capturar":
            return capture(args, course)
        return validate(args, course)
    except (ValueError, RuntimeError) as exc:
        print(f"FALHA_TECNICA: {exc}", file=sys.stderr)
        print("Nenhum arquivo foi restaurado.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
