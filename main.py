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


def validate(word):
    """Check the word against the competition gate.

    The gate requires UTF-8 text of 1 to 24 characters, not only
    whitespace; the entry itself must be exactly one word, and a word
    the judge reads as a word contains letters only.
    """
    if not word:
        return "word is blank"
    if len(word) < MIN_LEN or len(word) > MAX_LEN:
        return "word must be %d-%d characters, got %d" % (
            MIN_LEN,
            MAX_LEN,
            len(word),
        )
    if len(word.split()) != 1:
        return "entry must be exactly one word"
    if not word.isalpha():
        return "entry must be letters only, got %r" % word
    return None


def main() -> int:
    word = WORD.strip()
    problem = validate(word)
    if problem is not None:
        print("error: %s" % problem, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)
    # Read the file back and confirm it holds exactly the validated word.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != word:
        print(
            "error: %s holds %r, expected %r" % (OUTPUT_PATH, written, word),
            file=sys.stderr,
        )
        return 1
    print("wrote %r (%d chars) to %s" % (word, len(word), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
