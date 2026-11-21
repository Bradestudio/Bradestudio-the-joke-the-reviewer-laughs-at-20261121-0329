#!/usr/bin/env python3
"""Entrypoint for the make.fun the-joke-the-reviewer-laughs-at-20261121-0329 entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Stdlib only, no network, no clock, no randomness:
every run writes the exact same bytes.

The joke (100 Unicode code points, inside the 1-280 gate):

    My AI agent reviewed its own pull request, requested changes,
    and now neither of us will approve it.

The laugh: the reviewer and the author are the same agent, so the
review loop deadlocks with itself -- the punchline lands the moment
you picture the diff sitting there, change-requested by its own
author, with nobody left who will press approve. Every word earns
its place and the joke never explains itself: the stalemate is the
whole joke. The truth every developer beside an agent recognises: agents now review their own
diffs, and "requested changes" from the code's own author is a
stalemate no human asked for.
"""
import os
import sys
from pathlib import Path

JOKE = (
    "My AI agent reviewed its own pull request, requested changes, "
    "and now neither of us will approve it."
)


def main():
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not dest and len(sys.argv) > 1:
        dest = sys.argv[1]
    if not dest:
        dest = "output"
    outdir = Path(dest)
    outdir.mkdir(parents=True, exist_ok=True)
    target = outdir / "entry.txt"
    data = JOKE.encode("utf-8")
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit(f"joke is {len(JOKE)} code points, gate needs 1-280")
    if not JOKE.strip():
        raise SystemExit("joke is only whitespace")
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes, {len(JOKE)} code points)")


if __name__ == "__main__":
    main()
