#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun bounty entry.

Writes a single-line joke about office life to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same line every run.
"""

import os

JOKE = (
    "The printer only jams on urgent documents, so I keep a printed "
    "resignation letter in my drawer \u2014 in case it ever decides to work."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
