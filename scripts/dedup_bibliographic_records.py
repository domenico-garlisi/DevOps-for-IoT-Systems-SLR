#!/usr/bin/env python3
"""
dedup_bibliographic_records.py

Skeleton deduplication script for the per-database exports in
data/01-primary-search/uniformed/ -- the semicolon-delimited, common-schema
files (source;entry_type;document_type;title;authors;year;doi;url;abstract;
keywords;journal;booktitle;publisher;pages), one per database (wos, ieee,
acm, scopus). Use these rather than data/01-primary-search/raw/, whose
files keep each database's own native column names/delimiter and are not
directly comparable across databases.

Strategy (adjust to taste, but document whatever you actually use in
data/02-screening/README.md and this file's docstring):
  1. Normalize titles (lowercase, strip punctuation/whitespace) and DOIs.
  2. Exact-match on normalized DOI -> definite duplicate.
  3. Exact-match on normalized title + year -> probable duplicate, flag for
     manual confirmation (conference papers that later appear as extended
     journal articles will NOT be caught by this and need a manual pass,
     per the manuscript's own inclusion/exclusion note on this exact case).
  4. Write survivors + a dedup log to data/02-screening/duplicate.csv.

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


def load_records(input_dir: Path):
    records = []
    for csv_path in sorted(input_dir.glob("*.csv")):
        with csv_path.open(newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f, delimiter=";")
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
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input-dir", default="../data/01-primary-search/uniformed",
                     help="Directory containing the uniformed, semicolon-delimited "
                          "per-database CSV exports")
    ap.add_argument("--title-field", default="title")
    ap.add_argument("--doi-field", default="doi")
    args = ap.parse_args()

    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        print(f"No uniformed exports found at {input_dir} -- populate "
              f"data/01-primary-search/uniformed/ first.", file=sys.stderr)
        sys.exit(1)

    records = load_records(input_dir)
    if not records:
        print("Input directory exists but contains no CSV records yet.", file=sys.stderr)
        sys.exit(1)

    groups = find_duplicate_groups(records, args.title_field, args.doi_field)
    print(f"Loaded {len(records)} records from {input_dir}")
    print(f"Found {len(groups)} candidate duplicate group(s) "
          f"(manual confirmation still required before writing to "
          f"data/02-screening/duplicate.csv).")


if __name__ == "__main__":
    main()
