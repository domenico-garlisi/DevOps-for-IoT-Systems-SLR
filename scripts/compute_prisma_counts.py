#!/usr/bin/env python3
"""
compute_prisma_counts.py

Recomputes the PRISMA funnel counts from the current data/ layout and
compares them against the "Reported selection counts" table in
protocol/review-protocol.md. Run this once data/02-screening/,
data/03-secondary-search/ and data/04-included-studies/ are populated
with real decisions, to get one single, self-consistent set of counts
to report in the final manuscript.

Primary-search funnel is one row per CSV in the corresponding folder:
  data/01-primary-search/uniformed/*.csv  -> search results
  data/02-screening/duplicate.csv         -> duplicates removed
  data/02-screening/excluded.csv          -> excluded on relevance/soundness
  data/04-included-studies/primary-studies.csv               -> included
  data/04-included-studies/supporting-background-references.csv -> background refs (+)
  data/04-included-studies/previous-reviews.csv               -> prior reviews found

Secondary-search (forward-snowballing) funnel lives in a single file,
data/03-secondary-search/secondary-studies-snowballing.csv, where each
row already carries a screening decision in its `Relevance` column
(as currently used in that working file -- adjust RELEVANCE_BUCKETS
below if the labels change):
  "in primary study"    -> already covered by the primary search (duplicate)
  "non rilevante"/"escluso" -> excluded on relevance/soundness
  "in review collegate" -> related/previous review
  "in background"       -> background/supporting reference (+)
  "rilevante"            -> included secondary study
"""
import argparse
import csv
from collections import Counter
from pathlib import Path

RELEVANCE_BUCKETS = {
    "in primary study": "duplicate_of_primary",
    "non rilevante": "excluded",
    "escluso": "excluded",
    "in review collegate": "related_review",
    "in background": "background",
    "rilevante": "included",
}


def count_csv_rows(path: Path) -> int:
    if not path.exists() or path.stat().st_size == 0:
        return 0
    with path.open(newline="", encoding="utf-8-sig") as f:
        return sum(1 for _ in csv.DictReader(f))


def count_csv_rows_glob(dir_: Path, pattern: str) -> int:
    if not dir_.exists():
        return 0
    total = 0
    for path in sorted(dir_.glob(pattern)):
        total += count_csv_rows(path)
    return total


def bucket_secondary_snowballing(path: Path) -> Counter:
    buckets = Counter()
    if not path.exists() or path.stat().st_size == 0:
        return buckets
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            relevance = (row.get("Relevance") or "").strip()
            bucket = RELEVANCE_BUCKETS.get(relevance, f"unmapped:{relevance!r}")
            buckets[bucket] += 1
    return buckets


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--primary-search-dir", default="../data/01-primary-search/uniformed")
    ap.add_argument("--screening-dir", default="../data/02-screening")
    ap.add_argument("--secondary-search-dir", default="../data/03-secondary-search")
    ap.add_argument("--included-dir", default="../data/04-included-studies")
    args = ap.parse_args()

    primary_search_dir = Path(args.primary_search_dir)
    screening_dir = Path(args.screening_dir)
    secondary_search_dir = Path(args.secondary_search_dir)
    included_dir = Path(args.included_dir)

    # --- primary search funnel ---
    primary_search_results = count_csv_rows_glob(primary_search_dir, "*.csv")
    primary_duplicates = count_csv_rows(screening_dir / "duplicate.csv")
    primary_excluded = count_csv_rows(screening_dir / "excluded.csv")
    primary_included = count_csv_rows(included_dir / "primary-studies.csv")
    primary_background = count_csv_rows(included_dir / "supporting-background-references.csv")
    primary_related_reviews = count_csv_rows(included_dir / "previous-reviews.csv")

    # --- secondary search (snowballing) funnel ---
    snowball_path = secondary_search_dir / "secondary-studies-snowballing.csv"
    secondary_search_results = count_csv_rows(snowball_path)
    secondary_buckets = bucket_secondary_snowballing(snowball_path)
    secondary_duplicates = secondary_buckets.get("duplicate_of_primary", 0)
    secondary_excluded = secondary_buckets.get("excluded", 0)
    secondary_included = secondary_buckets.get("included", 0)
    secondary_background = secondary_buckets.get("background", 0)
    secondary_related_reviews = secondary_buckets.get("related_review", 0)
    secondary_unmapped = {k: v for k, v in secondary_buckets.items() if k.startswith("unmapped:")}

    print("Recomputed counts from populated CSVs (0 = template not yet filled in):")
    print()
    print("Primary search:")
    print(f"  Search results:                   {primary_search_results}")
    print(f"  Duplicate elimination (-):        {primary_duplicates}")
    print(f"  Relevance/soundness exclusion (-): {primary_excluded}")
    print(f"  Additional supporting studies (+): {primary_background}")
    print(f"  Related/previous reviews found:    {primary_related_reviews}")
    print(f"  Included primary studies:          {primary_included}")
    print()
    print("Secondary search (forward-snowballing):")
    print(f"  Search results:                   {secondary_search_results}")
    print(f"  Duplicate of primary set (-):      {secondary_duplicates}")
    print(f"  Relevance/soundness exclusion (-): {secondary_excluded}")
    print(f"  Additional supporting studies (+): {secondary_background}")
    print(f"  Related/previous reviews found:    {secondary_related_reviews}")
    print(f"  Included secondary studies:        {secondary_included}")
    if secondary_unmapped:
        print(f"  WARNING - unmapped Relevance labels: {secondary_unmapped}")
        print("  (update RELEVANCE_BUCKETS in this script if these are legitimate)")
    print()
    print(f"TOTAL included (primary + secondary): {primary_included + secondary_included}")
    print()
    print("Compare this against the 'Reported selection counts' table in "
          "protocol/review-protocol.md and reconcile with the manuscript's "
          "Table I, body text, and Figure 5/6 captions before finalizing.")


if __name__ == "__main__":
    main()
