#!/usr/bin/env python3
"""Write one funny one-line review a dog gives the mailman.

Stdlib only, no network. Writes the review to /output/entry.txt.
"""

import os

LINE = (
    "Five stars: the mailman comes every day, drops the good stuff "
    "through the slot, and still hasn't worked out that the bills keep "
    "disappearing because I eat them. Would bark again."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
