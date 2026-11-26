#!/usr/bin/env python3
"""Write one original funny one-liner to /output/entry.txt.

The line is a single self-contained joke with a setup and a punchline,
written fresh for this entry. The program checks its own output before
declaring success: the line must be a single line, not only whitespace,
and between 1 and 200 characters long, as the competition gate requires.
"""

import os
import sys

LINE = (
    "My chatbot finally passed the Turing test \u2014 "
    "it now ignores my messages exactly like a human would."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate: the entry must be exactly one line.
    if "\n" in LINE or "\r" in LINE:
        print("FAIL: entry must be a single line", file=sys.stderr)
        return 1

    # Gate: the entry must not be only whitespace.
    if not LINE.strip():
        print("FAIL: entry must not be only whitespace", file=sys.stderr)
        return 1

    # Gate: the entry must be between 1 and 200 characters long.
    length = len(LINE)
    if not 1 <= length <= 200:
        print(
            f"FAIL: entry is {length} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)

    print(f"Wrote {length}-character entry to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
