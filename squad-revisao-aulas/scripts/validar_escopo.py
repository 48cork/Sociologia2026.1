#!/usr/bin/env python3
"""Captura e valida o escopo Git de uma aula sem restaurar arquivos.

``capturar`` grava um baseline JSON a pedido do orquestrador. ``validar`` compara o
estado atual, hashes de todas as aulas e caminhos modificados. O script nunca edita HTML,
nunca executa stage e nunca restaura alterações.
"""

from __future__ import annotations

import argparse
import hashlib
import json
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


def repo_relative(raw: str | Path, *, must_exist: bool = False) -> str:
    path = Path(raw)
    absolute = path.resolve() if path.is_absolute() else (REPO / path).resolve()
    try:
        relative = absolute.relative_to(REPO)
    except ValueError as exc:
        raise ValueError(f"caminho fora do repositório: {raw}") from exc
    if must_exist and not absolute.is_file():
        raise ValueError(f"arquivo inexistente: {raw}")
    return relative.as_posix()


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


def snapshot(authorized: str, course: dict) -> dict:
    return {
        "schema_version": 1,
        "capturado_em": datetime.now(timezone.utc).isoformat(),
        "repo": str(REPO),
        "head": git("rev-parse", "HEAD").decode().strip(),
        "branch": git("branch", "--show-current").decode().strip(),
        "arquivo_autorizado": authorized,
        "git_status": status_entries(),
        "hashes_aulas": lesson_hashes(course),
    }


def allowed_path(path: str, exact: set[str], prefixes: set[str]) -> bool:
    if path in exact:
        return True
    return any(path == prefix or path.startswith(prefix.rstrip("/") + "/") for prefix in prefixes)


def capture(args: argparse.Namespace, course: dict) -> int:
    authorized = repo_relative(args.arquivo, must_exist=True)
    lesson_dir = course["diretorio_aulas"].rstrip("/") + "/"
    if not authorized.startswith(lesson_dir):
        raise ValueError("--arquivo deve ser um HTML do diretório de aulas configurado")
    number = int(Path(authorized).stem.split("-")[-1])
    start, end = course["aulas_processamento_inicial"]
    if not start <= number <= end:
        raise ValueError(f"Aula {number:02d} é somente leitura; faixa gravável: {start:02d}-{end:02d}")
    output = Path(args.saida)
    output = output if output.is_absolute() else REPO / output
    output.resolve().relative_to(REPO)
    output.parent.mkdir(parents=True, exist_ok=True)
    data = snapshot(authorized, course)
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"BASELINE {output.relative_to(REPO)}")
    print(f"HEAD {data['head']}")
    print(f"AUTORIZADO {authorized}")
    print(f"STATUS_INICIAL {len(data['git_status'])} caminho(s)")
    return 0


def validate(args: argparse.Namespace, course: dict) -> int:
    authorized = repo_relative(args.arquivo, must_exist=True)
    baseline_path = Path(args.baseline)
    baseline_path = baseline_path if baseline_path.is_absolute() else REPO / baseline_path
    try:
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"baseline inválido: {exc}") from exc
    if baseline.get("arquivo_autorizado") != authorized:
        raise ValueError("arquivo autorizado não coincide com o baseline")

    exact = {authorized}
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
        if path == authorized:
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
    print(f"AUTORIZADO {authorized}")
    print(f"PROTEGIDAS {len(current_hashes) - 1} aula(s) com hash preservado")
    print(f"CAMINHOS_PERMITIDOS {', '.join(sorted(exact | prefixes))}")
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest="comando", required=True)
    capture_cmd = commands.add_parser("capturar", help="gravar baseline antes da escrita")
    capture_cmd.add_argument("--arquivo", required=True)
    capture_cmd.add_argument("--saida", required=True)
    validate_cmd = commands.add_parser("validar", help="comparar estado depois da escrita")
    validate_cmd.add_argument("--arquivo", required=True)
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
