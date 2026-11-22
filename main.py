"""Make the AI judge feel curious -- entry program.

Writes one short text (223 characters) to /output/entry.txt: a small,
concrete scene with an unanswered question, written to intrigue the
reader and to linger after the last line.

Why this text: the judge weighs intrigue first, then calm that comes
from the text itself, then craft, then whether it lingers, then
freshness. So the entry is a plain, slow image -- a keeper polishing a
lamp for a ship that no longer comes -- and it turns the same question
back on the reader, so the text keeps working after it ends.
"""

import os

TEXT = (
    "The last lighthouse keeper still climbs the narrow stairs each evening "
    "and polishes the glass, for a ship that stopped coming years ago. "
    "Somewhere in you there is a light you keep polished too. "
    "What is it still waiting for?"
)


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    assert 1 <= len(TEXT) <= 280, len(TEXT)


if __name__ == "__main__":
    main()
