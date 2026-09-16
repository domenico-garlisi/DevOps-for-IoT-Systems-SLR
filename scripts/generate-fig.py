#!/usr/bin/env python3
"""
generate-fig.py

Regenerates Figure 5 (temporal distribution of selected papers, 2016-2026)
from data/05-data-extraction/extraction-form.csv (the semicolon-delimited
export of the working extraction spreadsheet), using its `year` column.
Rows with no year recorded yet are skipped.

Usage:
    python generate-fig.py --input ../data/05-data-extraction/extraction-form.csv --outdir ../figures

Requires: pandas, matplotlib (see requirements.txt)
"""
import argparse
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", default="../data/05-data-extraction/extraction-form.csv")
    ap.add_argument("--outdir", default="../figures")
    args = ap.parse_args()

    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_path, sep=";", encoding="utf-8-sig")
    if df.empty or "year" not in df.columns:
        print(f"{input_path} is empty or missing a 'year' column -- "
              f"populate data/05-data-extraction/extraction-form.csv "
              f"with real extracted-study records first.")
        return

    years = df["year"].dropna().astype(int)
    if years.empty:
        print(f"{input_path} has a 'year' column but no populated values yet.")
        return

    # Figure 5: temporal distribution
    year_counts = years.value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    year_counts.plot(kind="bar", ax=ax, color="#2f7d6b")
    ax.set_title("Temporal Distribution of the Selected Papers")
    ax.set_xlabel("Publication Year")
    ax.set_ylabel("Number of Selected Papers")
    fig.tight_layout()
    fig.savefig(outdir / "fig5_temporal_distribution_regenerated.png", dpi=200)
    plt.close(fig)

    print(f"Wrote regenerated Figure 5 to {outdir}/")


if __name__ == "__main__":
    main()
