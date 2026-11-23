#!/usr/bin/env python3
"""One Word, First Thought — writes the entry word to /output/entry.txt.

The gate requires UTF-8 text of 1 to 24 characters, not only whitespace.
This program writes exactly one word and validates it before writing.
"""
import os
import sys

WORD = "defenestration"
OUTPUT_PATH = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 24


def main() -> int:
    word = WORD.strip()
    if not word:
        print("error: word is blank", file=sys.stderr)
        return 1
    if len(word) < MIN_LEN or len(word) > MAX_LEN:
        print(
            "error: word must be %d-%d characters, got %d"
            % (MIN_LEN, MAX_LEN, len(word)),
            file=sys.stderr,
        )
        return 1
    if len(word.split()) != 1:
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)
    print("wrote %r (%d chars) to %s" % (word, len(word), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
