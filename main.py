#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = (
    "My alarm clock went off at 6 AM on a Saturday, "
    "so I snoozed it nine times \u2014 "
    "then it filed a noise complaint against me."
)


def main() -> None:
    # Gate: entry must be 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
