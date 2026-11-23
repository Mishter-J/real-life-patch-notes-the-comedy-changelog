#!/usr/bin/env python3
"""Real-Life Patch Notes entry.

Writes one funny one-line software patch note for a bug in real life
(human biology) to /output/entry.txt. Deterministic: the same line,
byte for byte, on every run.

The note is built from named parts so each clause can be read and
checked on its own, then validated against the competition gate
(single line, 1-160 characters) before it is written.
"""

import os

VERSION = "v3.2.0"

BUG = (
    "fixed a bug where the brain replayed embarrassing moments "
    "from 2007 at 3 a.m. instead of sleeping."
)

FIX = "Added a 'let it go' cache-clear on first yawn."

ENTRY = f"{VERSION}: {BUG} {FIX}"

MAX_CHARS = 160


def validate(entry):
    """Check the note meets the gate: one non-blank line, <=160 chars."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over {MAX_CHARS}")
    return entry


OUTPUT_PATH = "/output/entry.txt"


def write_entry(entry):
    """Write the note atomically and verify the file round-trips.

    Writes to a sibling temp file and renames it into place so a
    reader never sees a half-written note, then reads the file back
    and checks its bytes match exactly what was validated.
    """
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    os.replace(tmp_path, OUTPUT_PATH)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != entry.encode("utf-8"):
        raise RuntimeError("written entry does not match validated text")
    return written


def main():
    entry = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    write_entry(entry)


if __name__ == "__main__":
    main()
