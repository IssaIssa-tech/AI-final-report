from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
MODEL_TABLE = ROOT / "paper" / "tables" / "model_taxonomy.csv"
BENCHMARK_TABLE = ROOT / "paper" / "tables" / "benchmark_taxonomy.csv"
FIG_DIR = ROOT / "paper" / "figures"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def save_model_timeline() -> None:
    rows = read_rows(MODEL_TABLE)
    counts = Counter(row["year"] for row in rows)
    years = sorted(counts)
    values = [counts[year] for year in years]

    plt.figure(figsize=(6.2, 3.0))
    bars = plt.bar(years, values, color="#6f6f6f", edgecolor="black", linewidth=0.6)
    plt.xlabel("Publication year", fontsize=9)
    plt.ylabel("Representative models", fontsize=9)
    plt.xticks(fontsize=8)
    plt.yticks(range(0, max(values) + 2), fontsize=8)
    plt.grid(axis="y", linestyle="--", linewidth=0.4, alpha=0.6)
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, value + 0.05, str(value), ha="center", va="bottom", fontsize=8)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "model_timeline.png", dpi=300)
    plt.close()


def save_benchmark_timeline() -> None:
    rows = read_rows(BENCHMARK_TABLE)
    counts = Counter(row["year"] for row in rows)
    years = sorted(counts)
    values = [counts[year] for year in years]

    plt.figure(figsize=(6.2, 3.0))
    plt.plot(years, values, marker="o", color="black", linewidth=1.2)
    plt.fill_between(years, values, color="#bdbdbd", alpha=0.45)
    plt.xlabel("Publication year", fontsize=9)
    plt.ylabel("Representative benchmarks", fontsize=9)
    plt.xticks(fontsize=8)
    plt.yticks(range(0, max(values) + 2), fontsize=8)
    plt.grid(axis="both", linestyle="--", linewidth=0.4, alpha=0.6)
    for year, value in zip(years, values):
        plt.text(year, value + 0.05, str(value), ha="center", va="bottom", fontsize=8)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "benchmark_timeline.png", dpi=300)
    plt.close()


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    save_model_timeline()
    save_benchmark_timeline()
    print(f"Wrote {FIG_DIR / 'model_timeline.png'}")
    print(f"Wrote {FIG_DIR / 'benchmark_timeline.png'}")


if __name__ == "__main__":
    main()

