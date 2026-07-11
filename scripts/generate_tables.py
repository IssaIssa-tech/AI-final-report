from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_TABLES = ROOT / "paper" / "tables"
RESULT_TABLES = ROOT / "results" / "tables"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_markdown_table(rows: list[dict[str, str]], output_path: Path) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {output_path}")

    headers = list(rows[0].keys())
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row[h] for h in headers) + " |")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    RESULT_TABLES.mkdir(parents=True, exist_ok=True)
    for csv_path in sorted(PAPER_TABLES.glob("*.csv")):
        rows = read_csv(csv_path)
        output_path = RESULT_TABLES / f"{csv_path.stem}.md"
        write_markdown_table(rows, output_path)
        print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()

