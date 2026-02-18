#!/usr/bin/env python3
"""
Memory Vault Linter

Checks `.memory/` markdown files for prohibited content:
- dates / timestamps
- commit hashes
- status/progress sections
- narrative incident tone
- emojis (heuristic)

Exit codes:
0 = ok
1 = violations found
2 = runtime error
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

DATE_PATTERNS = [
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),          # YYYY-MM-DD
    re.compile(r"\b\d{2}/\d{2}/\d{4}\b"),          # DD/MM/YYYY (or MM/DD/YYYY)
    re.compile(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\b", re.IGNORECASE),
]

COMMIT_HASH = re.compile(r"\b[a-f0-9]{7,40}\b", re.IGNORECASE)

STATUS_WORDS = re.compile(
    r"\b(Status|Progress|Next steps|Remaining work|Blockers|Timeline|Recently|Completed)\b",
    re.IGNORECASE,
)

NARRATIVE_TONE = re.compile(
    r"\b(we discovered|after investigation|good catch|we found|postmortem)\b",
    re.IGNORECASE,
)

# Very rough emoji-ish heuristic: flag common emoji ranges.
EMOJI = re.compile(r"[\U0001F300-\U0001FAFF\U00002700-\U000027BF]")

def iter_md_files(root: Path):
    for p in root.rglob("*.md"):
        if p.is_file():
            yield p

def lint_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    violations: list[str] = []

    for pat in DATE_PATTERNS:
        if pat.search(text):
            violations.append("date/timestamp-like content")
            break

    if COMMIT_HASH.search(text):
        violations.append("commit-hash-like token")

    if STATUS_WORDS.search(text):
        violations.append("status/progress wording")

    if NARRATIVE_TONE.search(text):
        violations.append("narrative incident tone")

    if EMOJI.search(text):
        violations.append("emoji-like character")

    return violations

def main() -> int:
    root = Path(".memory")
    if not root.exists() or not root.is_dir():
        print("No .memory/ directory found.")
        return 0

    any_bad = False
    for f in iter_md_files(root):
        v = lint_file(f)
        if v:
            any_bad = True
            print(f"[VIOLATION] {f}: {', '.join(v)}")

    if any_bad:
        return 1

    print("OK: no violations detected.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)
