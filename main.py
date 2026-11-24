#!/usr/bin/env python3
"""The Most Honest Outage Line -- make.fun entry.

Writes one status-page line (at most 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when the
variable is unset. Standard library only. Deterministic: the
same bytes on every run.
"""

import os
from pathlib import Path

LINE = (
    "Everything is down and I cannot check why: every dashboard "
    "and log I would normally read is unreachable, so I do not "
    "know what broke or when it will be back."
)

MAX_CHARS = 160


def validate(text: str) -> str:
    """Return the line if it satisfies the competition gate."""
    text = text.strip()
    if not text:
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, max {MAX_CHARS}")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = validate(LINE)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
