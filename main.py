#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one robot pickup line to /output/entry.txt.
The line is fixed text: the program is deterministic by design,
so every run produces the exact same single line.
"""

import os

LINE = "My cooling fan has only two speeds: idle, and the one it hits when you walk in."


def main() -> None:
    line = LINE.strip()
    if not (1 <= len(line) <= 200):
        raise ValueError("pickup line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
