#!/usr/bin/env python3
"""Write the chosen one-line laugh to /output/entry.txt (deterministic).

Entry for make.fun bounty u-ronigrv-the-one-line-laugh-7ccca46f ("The One-Line Laugh").
The line is a single sentence of 112 characters, well within the 200-character gate.
"""

import os

LINE = "I put my keys in the same spot every day so I'd never lose them, and now I lose them in the same spot every day."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
