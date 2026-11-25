#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — one short funny rant.

The program writes a single rant (<= 400 characters) about an everyday
annoyance to /output/entry.txt.
"""

import os

RANT = (
    "Our office printer has one job and a PhD in refusing it. "
    "It jams on page one, drinks a full cartridge to print a blank page, "
    "then flashes ERROR 0xDEAD like a riddle from a dying robot. "
    "Yesterday I unplugged it, marched it to the bin, and apologised to the bin. "
    "The bin accepted. HR is now investigating why productivity is up 40%."
)


def main():
    text = RANT.strip()
    assert 1 <= len(text) <= 400, f"rant is {len(text)} chars, must be 1-400"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
