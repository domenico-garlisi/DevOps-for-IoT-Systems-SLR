#!/usr/bin/env python3
"""
compute_prisma_counts.py

Recomputes the PRISMA funnel counts from the screening CSVs and compares
them against data/02-screening/prisma-flow-counts.csv (which currently
records the manuscript's own, INTERNALLY INCONSISTENT numbers -- see
docs/known-issues-and-todos.md). Run this once the screening templates in
data/02-screening/ and data/03-included-studies/ are populated with real
decisions, to get one single, self-consistent set of counts to report in
the final manuscript.
"""
import argparse
import csv
from pathlib import Path


def count_csv_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(newline="", encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--screening-dir", default="../data/02-screening")
    ap.add_argument("--included-dir", default="../data/03-included-studies")
    args = ap.parse_args()

    screening_dir = Path(args.screening_dir)
    included_dir = Path(args.included_dir)

    dedup_log = count_csv_rows(screening_dir / "duplicate.csv")
    ta_screened = count_csv_rows(screening_dir / "title-abstract-screening-template.csv")
    ft_screened = count_csv_rows(screening_dir / "full-text-screening-template.csv")
    primary = count_csv_rows(included_dir / "primary-studies-template.csv")
    secondary = count_csv_rows(included_dir / "secondary-studies-snowballing-template.csv")
    background = count_csv_rows(included_dir / "supporting-background-references-template.csv")

    print("Recomputed counts from populated CSVs (0 = template not yet filled in):")
    print(f"  Deduplication log rows:          {dedup_log}")
    print(f"  Title/abstract screening rows:    {ta_screened}")
    print(f"  Full-text screening rows:         {ft_screened}")
    print(f"  Primary studies included:         {primary}")
    print(f"  Secondary (snowballed) studies:   {secondary}")
    print(f"  Background/supporting references: {background}")
    print(f"  TOTAL included (primary+secondary): {primary + secondary}")
    print()
    print("Compare this against data/02-screening/prisma-flow-counts.csv and "
          "reconcile with the manuscript's Table I, body text, and Figure 5/6 "
          "captions before finalizing (see docs/known-issues-and-todos.md).")


if __name__ == "__main__":
    main()
