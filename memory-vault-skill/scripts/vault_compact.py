#!/usr/bin/env python3
"""
Memory Vault Compactor (minimal helper)

This script does NOT attempt to rewrite meaningfully by itself.
It reports:
- files over a line limit
- candidates for splitting

The LLM should perform the real compaction edits (topic-aware).
"""

from __future__ import annotations

import sys
from pathlib import Path

DEFAULT_LIMIT = 250

def count_lines(path: Path) -> int:
    with path.open("r", encoding="utf-8", errors="replace") as f:
        return sum(1 for _ in f)

def main() -> int:
    limit = DEFAULT_LIMIT
    if len(sys.argv) >= 2:
        try:
            limit = int(sys.argv[1])
        except ValueError:
            print("Usage: vault_compact.py [line_limit]")
            return 2

    root = Path(".memory")
    if not root.exists() or not root.is_dir():
        print("No .memory/ directory found.")
        return 0

    oversized = []
    for p in root.rglob("*.md"):
        if not p.is_file():
            continue
        n = count_lines(p)
        if n > limit:
            oversized.append((n, p))

    oversized.sort(reverse=True, key=lambda x: x[0])

    if not oversized:
        print(f"OK: no files exceed {limit} lines.")
        return 0

    print(f"Files exceeding {limit} lines:")
    for n, p in oversized:
        print(f"- {p} ({n} lines)")

    return 1

if __name__ == "__main__":
    sys.exit(main())
