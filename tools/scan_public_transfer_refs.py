#!/usr/bin/env python3
"""Fail if private-only transfer references leak into public PR-facing files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("private run id", re.compile(r"27708114308|27712200105|27713315407|27715221107|27716446235")),
    ("private account", re.compile(r"gloriouskilka")),
    ("tooling marker", re.compile(r"Made-with:\s*Cursor")),
]

SKIP_DIRS = {
    ".git",
    ".ccache",
    ".cpmcache",
    "build",
    "dist",
    ".worktrees",
    "torch_ttnn/cpp_extension/third-party",
}

SKIP_FILES = {
    Path("tools/scan_public_transfer_refs.py"),
    Path("tools/gen_public_transfer_provenance.py"),
    Path("docs/public_transfer/RUNBOOK_ru.md"),
    Path("docs/public_transfer/ASSESSMENT_ru.md"),
    Path("docs/public_transfer/STATUS_ru.md"),
    Path("docs/public_transfer/provenance_index.md"),
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if rel in SKIP_FILES:
            continue
        if "pr_bodies" in rel.parts:
            continue
        if rel.name == "PR_BODY.md":
            continue
        yield path


def main() -> int:
    violations: list[str] = []
    for path in iter_files(ROOT):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    rel = path.relative_to(ROOT)
                    violations.append(f"{rel}:{line_no}: {label}: {line.strip()}")
    if violations:
        print("Private reference scan failed:", file=sys.stderr)
        for item in violations:
            print(item, file=sys.stderr)
        return 1
    print("Private reference scan: clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
