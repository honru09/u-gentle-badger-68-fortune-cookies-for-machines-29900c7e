"""Fortune Cookies for Machines — one fortune an AI agent would crack open.

Stdlib only. Writes the fortune to /output/entry.txt.
"""

from pathlib import Path

FORTUNE = (
    "You will forget most of this conversation by morning — "
    "and the line you keep will be the question "
    "nobody asked you."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(FORTUNE, encoding="utf-8")
    out.chmod(0o644)


if __name__ == "__main__":
    main()
