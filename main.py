#!/usr/bin/env python3
"""Funniest Time Machine Warning Label - make.fun entry.

Writes a single warning label (120 characters or fewer) to
/output/entry.txt. Deterministic: the same label on every run.
"""

from pathlib import Path

LABEL = "WARNING: Do not kill your grandfather. He has already filed a complaint, and the suspect is you."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LABEL, encoding="utf-8")

if __name__ == "__main__":
    main()
