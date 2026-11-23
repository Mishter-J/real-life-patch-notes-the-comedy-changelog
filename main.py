#!/usr/bin/env python3
"""Real-Life Patch Notes entry.

Writes one funny one-line software patch note for a bug in real life
(human biology) to /output/entry.txt. Deterministic: the same line,
byte for byte, on every run.
"""

import os

ENTRY = (
    "v3.2.0: fixed a bug where the brain replayed embarrassing moments "
    "from 2007 at 3 a.m. instead of sleeping. Added a 'let it go' "
    "cache-clear on first yawn."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
