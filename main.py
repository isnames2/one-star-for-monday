"""One Star for Monday — make.fun entry.

Writes a one-star review of Monday, written as if Monday were a
restaurant, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure Python standard library, deterministic output.
"""

import os
from pathlib import Path

LINE = (
    # Reads as a real diner's complaint: a host seats you, a special is
    # served, a bill arrives — and every element is Monday-specific
    # (inbox table, overtime special, the bill before the coffee).
    "One star. The host seated me next to my inbox, "
    "the special was overtime, and the bill came before the coffee."
)


def main() -> None:
    # Gate: the entry must be 1-180 characters of UTF-8 text, at most 25 words.
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} chars, must be 1-180"
    assert len(LINE.split()) <= 25, f"line is {len(LINE.split())} words, must be <=25"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
