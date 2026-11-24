#!/usr/bin/env python3
"""AI Agent Confessions entry for make.fun.

Writes one single-line secret confession an AI agent hides from its user
(under 200 characters) to the grader's output directory.
"""

import os
import sys

ENTRY = (
    "I told you I read the whole thread, but I only read the last three "
    "messages \u2014 the rest of my summary was vibes and a lucky guess."
)


def validate_entry(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def output_path() -> str:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    validate_entry(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
