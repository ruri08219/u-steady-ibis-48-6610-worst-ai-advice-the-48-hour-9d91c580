"""Worst AI advice, one line.

Writes a single line of deliberately terrible AI advice to
/output/entry.txt. The competition gate requires 1-140 characters;
anything outside that range is a bug, not an entry.
"""

from pathlib import Path

ENTRY = "If your smoke alarm keeps beeping, remove the battery \u2014 silence is the fastest way to fix a fire."

MIN_CHARS = 1
MAX_CHARS = 140
# Length of the entry line, checked at runtime so a bad edit fails loudly
# instead of shipping an entry the gate would refuse.
ENTRY_CHARS = len(ENTRY)


def main() -> None:
    if not MIN_CHARS <= ENTRY_CHARS <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {ENTRY_CHARS}"
        )
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
