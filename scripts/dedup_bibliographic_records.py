#!/usr/bin/env python3
"""
dedup_bibliographic_records.py

Skeleton deduplication script for the raw per-database exports in
data/01-search-results/raw/<database>/.

Strategy (adjust to taste, but document whatever you actually use in
data/02-screening/README-backup.md and this file's docstring):
  1. Normalize titles (lowercase, strip punctuation/whitespace) and DOIs.
  2. Exact-match on normalized DOI -> definite duplicate.
  3. Exact-match on normalized title + year -> probable duplicate, flag for
     manual confirmation (conference papers that later appear as extended
     journal articles will NOT be caught by this and need a manual pass,
     per the manuscript's own inclusion/exclusion note on this exact case).
  4. Write survivors + a dedup log to data/02-screening/.

This is a starting skeleton, not a finished, validated pipeline -- the
manuscript reports 322 primary-search and 342 secondary-search duplicates
removed; use those counts as a sanity check on whatever method you run.
"""
import argparse
import csv
import re
import sys
from pathlib import Path


def normalize_title(title: str) -> str:
    title = title.lower().strip()
    title = re.sub(r"[^a-z0-9\s]", "", title)
    title = re.sub(r"\s+", " ", title)
    return title


def normalize_doi(doi: str) -> str:
    if not doi:
        return ""
    doi = doi.strip().lower()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    return doi


def load_records(raw_dir: Path):
    records = []
    for csv_path in sorted(raw_dir.rglob("*.csv")):
        with csv_path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["_source_file"] = str(csv_path)
                records.append(row)
    return records


def find_duplicate_groups(records, title_field="title", doi_field="doi"):
    by_doi, by_title = {}, {}
    for i, r in enumerate(records):
        doi = normalize_doi(r.get(doi_field, ""))
        title = normalize_title(r.get(title_field, ""))
        if doi:
            by_doi.setdefault(doi, []).append(i)
        if title:
            by_title.setdefault(title, []).append(i)
    groups = [g for g in by_doi.values() if len(g) > 1]
    groups += [g for g in by_title.values() if len(g) > 1]
    return groups


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--raw-dir", default="../data/01-search-results/raw",
                     help="Directory tree containing per-database CSV exports")
    ap.add_argument("--title-field", default="title")
    ap.add_argument("--doi-field", default="doi")
    args = ap.parse_args()

    raw_dir = Path(args.raw_dir)
    if not raw_dir.exists():
        print(f"No raw exports found at {raw_dir} -- populate "
              f"data/01-search-results/raw/<database>/ first.", file=sys.stderr)
        sys.exit(1)

    records = load_records(raw_dir)
    if not records:
        print("Raw directory exists but contains no CSV records yet.", file=sys.stderr)
        sys.exit(1)

    groups = find_duplicate_groups(records, args.title_field, args.doi_field)
    print(f"Loaded {len(records)} records from {raw_dir}")
    print(f"Found {len(groups)} candidate duplicate group(s) "
          f"(manual confirmation still required before writing the dedup log).")


if __name__ == "__main__":
    main()
