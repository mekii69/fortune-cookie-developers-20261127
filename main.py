#!/usr/bin/env python3
"""Fortune cookie wisdom for developers.

Writes a single original fortune-cookie line, at most 120 characters
of plain text, to /output/entry.txt. No network, no randomness: every
run writes the same bytes, so the grader's two runs match.

The line is in classic fortune voice ("You will...") and its twist is
that the rushed code's author is the reader's own future self -- a
truth every developer who has inherited their own shortcuts recognises.
"""

import os

FORTUNE = "You will meet the developer who rushed this code, and it will be you, six months from now."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
