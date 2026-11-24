#!/usr/bin/env python3
"""Everyday Things, Two Lines: a traffic jam explained to a 10-year-old.

Writes the two-line entry to /output/entry.txt. Stdlib only, no network.
The gate requires UTF-8 text of 1 to 400 characters, so the length is
checked in code before writing.
"""

import os

LINE_1 = (
    "A traffic jam is like a hallway full of kids all trying to squeeze "
    "through one narrow doorway at the same time, so everyone shuffles "
    "forward a tiny step, waits, and shuffles again."
)

LINE_2 = (
    "The doorway shows why too many cars on too little road means "
    "stop-and-go crawling, but it leaves out traffic lights, crashes, "
    "and drivers choosing different routes."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 400):
        raise SystemExit(f"entry is {len(text)} chars, outside the 1-400 gate")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    lines = text.strip().split("\n")
    if len(lines) != 2:
        raise SystemExit(f"entry must be exactly 2 lines, got {len(lines)}")
    if any(line.count(".") != 1 for line in lines):
        raise SystemExit("each line must be a single sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
