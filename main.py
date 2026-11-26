#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door -- make.fun entry.

The sign taped to the haunted server room door, written by this
program to /output/entry.txt, where the program/v1 harness reads it.
Pure standard library; the only I/O is that one file.
"""

import os

LINE = "DO NOT REBOOT THE GHOST IN RACK 7. IT LIKES THE UPTIME."


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 120, "sign must be 1 to 120 characters, got %d" % len(line)
    assert "\n" not in line, "sign must be a single line"
    assert line.endswith("."), "sign must end with a period"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "read-back mismatch: file differs from entry"


if __name__ == "__main__":
    main()
