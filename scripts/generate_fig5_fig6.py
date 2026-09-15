#!/usr/bin/env python3
"""
generate_fig5_fig6.py

Regenerates Figure 5 (temporal distribution of selected papers, 2016-2026)
and Figure 6 (heatmap of the 122 selected papers across the six research
areas x six research areas cross-tabulation as printed in the manuscript)
from data/03-included-studies/primary-studies-template.csv, once that file
is populated with real `year` and `thematic_area` columns.

Usage:
    python generate_fig5_fig6.py --input ../data/03-included-studies/primary-studies-template.csv --outdir ../figures

Requires: pandas, matplotlib (see requirements.txt)
"""
import argparse
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", default="../data/03-included-studies/primary-studies-template.csv")
    ap.add_argument("--outdir", default="../figures")
    args = ap.parse_args()

    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_path)
    if df.empty or "year" not in df.columns:
        print(f"{input_path} is empty or missing a 'year' column -- "
              f"populate data/03-included-studies/primary-studies-template.csv "
              f"with real included-study records first.")
        return

    # Figure 5: temporal distribution
    year_counts = df["year"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    year_counts.plot(kind="bar", ax=ax, color="#2f7d6b")
    ax.set_title("Temporal Distribution of the Selected Papers")
    ax.set_xlabel("Publication Year")
    ax.set_ylabel("Number of Selected Papers")
    fig.tight_layout()
    fig.savefig(outdir / "fig5_temporal_distribution_regenerated.png", dpi=200)
    plt.close(fig)

    # Figure 6: thematic-area cross-tabulation heatmap
    if "thematic_area" in df.columns:
        area_counts = df["thematic_area"].value_counts()
        fig, ax = plt.subplots(figsize=(8, 5))
        area_counts.plot(kind="bar", ax=ax, color="#2f6d7d")
        ax.set_title("Distribution of Selected Papers Across Research Areas")
        ax.set_ylabel("Number of Papers")
        fig.tight_layout()
        fig.savefig(outdir / "fig6_thematic_distribution_regenerated.png", dpi=200)
        plt.close(fig)

    print(f"Wrote regenerated figures to {outdir}/")


if __name__ == "__main__":
    main()
