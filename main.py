#!/usr/bin/env python3
"""The Cold Shoulder — a one-line resignation letter for make.fun's
"The One-Line Exit" bounty.

The program assembles one resignation letter, exactly one line long,
and writes it to /output/entry.txt (the gate the sealed scorer checks:
UTF-8 text of 1 to 140 characters, not only white space).

The joke: a zoo penguin keeper quits with the two puns the job hands
him for free — the cold shoulder from his birds, and waddling off
toward warmer opportunities.
"""

import os
import sys


def build_line() -> str:
    """Compose the single resignation line from its two halves."""
    opening = "I hereby resign as the zoo's penguin keeper:"
    punchline = (
        "after years of getting the cold shoulder, "
        "I am waddling off to warmer opportunities."
    )
    return f"{opening} {punchline}"


def check_gate(line: str) -> None:
    """Refuse to write anything the gate would reject."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if line != line.strip():
        raise ValueError("entry must not start or end with white space")
    chars = len(line)
    if not 1 <= chars <= 140:
        raise ValueError(f"entry is {chars} chars, gate allows 1-140")
    if not line.strip():
        raise ValueError("entry must not be only white space")


def main() -> int:
    line = build_line()
    check_gate(line)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
