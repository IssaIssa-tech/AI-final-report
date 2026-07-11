from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper" / "paper.md"
BIB = ROOT / "paper" / "references.bib"


CITATION_PATTERN = re.compile(r"\[@([A-Za-z0-9:_-]+)\]")
BIBKEY_PATTERN = re.compile(r"@\w+\{([^,]+),")


def main() -> None:
    paper_text = PAPER.read_text(encoding="utf-8")
    bib_text = BIB.read_text(encoding="utf-8")

    cited_keys = set(CITATION_PATTERN.findall(paper_text))
    bib_keys = set(BIBKEY_PATTERN.findall(bib_text))

    missing = sorted(cited_keys - bib_keys)
    unused = sorted(bib_keys - cited_keys)

    print(f"Citation keys used in paper: {len(cited_keys)}")
    print(f"Bibliography entries: {len(bib_keys)}")

    if missing:
        print("Missing bibliography entries:")
        for key in missing:
            print(f"  - {key}")
        raise SystemExit(1)

    if unused:
        print("Unused bibliography entries:")
        for key in unused:
            print(f"  - {key}")

    print("Reference validation passed.")


if __name__ == "__main__":
    main()

