#"DevOps for IoT Systems: Methodologies and Software Tools"

This repository is the Replication Package (RP) for the Systematic Literature Review (SLR):

> P. Ciancarini, D. Garlisi, R. Giancarlo, G. Grimaudo, **"DevOps for IoT Systems: Methodologies and Software Tools."**.

It packages additional matirial including the review protocol, search strategy, screening decisions, included-study lists, data-extraction sheets, and the analysis tables/figures, so that another researcher can inspect, audit, or re-run the study selection and synthesis.

**Companion resources already maintained by the authors:**
- Research-process tracking (GitHub): https://github.com/domenico-garlisi/DevOps-for-IoT-Systems-SLR
- Reference library (Zotero group): https://www.zotero.org/groups/6502633/devops-iot-library

This package is meant to sit alongside those two: Zotero holds the live, browsable bibliography; this repository (mirrored to Zenodo for a versioned DOI) holds the frozen protocol, data, and analysis artifacts tied to a specific manuscript version.

## Research Process

The review was conducted through a structured and reproducible process consisting of:

1. Definition of the review protocol and research questions;
2. Construction of a two-level search strategy;
3. Collection of publications from multiple digital libraries;
4. Deduplication and screening of retrieved studies;
5. Classification of publications according to thematic areas;
6. Data extraction and synthesis;
7. Development of taxonomies, use cases, and research trends.

---

## Project Structure

The work is organized into the following components:

### Protocol

Contains the research protocol, research questions, and inclusion/exclusion criteria.


#### Research questions

- **RQ1.** What are the reasons for considering DevOps as a strategic enabler for IoT?
- **RQ2.** Which practices and areas emerge from the recent literature on the integration of DevOps and IoT?
- **RQ3.** Which tools and frameworks facilitate the integration of DevOps and CI/CD into IoT?

The objective is to provide a comprehensive overview of how DevOps principles are adapted to support IoT ecosystems characterized by heterogeneous devices, distributed infrastructures, edge-cloud architectures, and cyber-physical interactions.


### Search Strategy

Documents the search strings, search procedures, and digital libraries considered in the review.

- Databases: Web of Science, IEEE Xplore, ACM Digital Library, Scopus.
- Query: `(DevOps OR "CI/CD" OR CICD OR DevSecOps) AND (IoT OR "Internet of Things" OR "Cyber-Physical Systems" OR CPS OR "Sensors Network" OR "Connected Devices" OR "Embedded Systems" OR "Edge Systems" OR "Fog Systems")` — per-database syntax in [`protocol/search-strings/`](protocol/search-strings/).

### Search Results

Provides access to the raw datasets exported from the selected digital libraries.

### Screening

Documents the deduplication process, screening activities, and thematic classification of publications.

### Data Extraction

Contains the extracted information used to perform the synthesis and comparative analysis.

### Analysis

Includes taxonomies, classifications, visualizations, use cases, and research findings generated from the selected studies.

### Replication Material

Contains supplementary material supporting the reproducibility of the review.

---

## Data Sources

The literature search was conducted using the following scientific databases:

* Scopus
* IEEE Xplore
* ACM Digital Library
* Web of Science

The resulting datasets are available within this repository in CSV format and constitute the basis for the subsequent screening and analysis activities.



## Methodology at a glance

- Framework: PRISMA-P (planning → execution → analysis), see [`protocol/review-protocol.md`](protocol/review-protocol.md).
- Primary search window: 2015-01-01 to 2026-04-29 (records pulled 2026-04-30). Secondary (forward-snowballing) search: 2026-07-01 to 2026-09-03.
- Filters: English language; articles and conference papers only (books, posters, short communications excluded).
- Screening: title/abstract then full text, by two reviewers independently, with disagreements resolved by the other two authors.

## Repository layout

```
.
├── protocol/                  Review protocol + per-database search strings
├── data/
│   ├── 01-search-results/     Raw exports per database (primary + secondary search) — drop CSV/RIS/BibTeX exports under raw/<db>/
│   ├── 02-screening/          PRISMA flow counts, deduplication log, title/abstract and full-text screening decisions
│   ├── 03-included-studies/   Final primary studies, snowballed secondary studies, and background/supporting references
│   ├── 04-data-extraction/    Extraction codebook + per-study extraction sheet
│   └── 05-analysis-tables/    Machine-readable versions of the paper's Tables II–V (maturity assessment, tool catalog, tool↔phase mapping, comparison with prior reviews)
├── figures/                   Mapping of each paper figure to its underlying data/regeneration script
├── scripts/                   Deduplication, PRISMA-count, and figure-regeneration scripts (Python)
├── manuscript/                Snapshot(s) of the paper as submitted/drafted
├── docs/                      Data dictionary and open issues to resolve before archiving
├── CITATION.cff               Citation metadata (GitHub "Cite this repository")
├── .zenodo.json               Metadata Zenodo reads when archiving a GitHub release
```

## How to reproduce the study selection

1. Run the four per-database searches in [`protocol/search-strings/`](protocol/search-strings/) and export results (CSV/RIS/BibTeX) into `data/01-search-results/raw/<database>/`.
2. Deduplicate with [`scripts/dedup_bibliographic_records.py`](scripts/dedup_bibliographic_records.py) (or your own tool) and log merges in `data/02-screening/deduplication-log-template.csv`.
3. Apply the inclusion/exclusion criteria in [`protocol/review-protocol.md`](protocol/review-protocol.md) at title/abstract level, then full text, recording decisions + reasons in `data/02-screening/`.
4. Recompute the PRISMA flow counts with [`scripts/compute_prisma_counts.py`](scripts/compute_prisma_counts.py) and compare against `data/02-screening/prisma-flow-counts.csv`.
5. Populate `data/03-included-studies/` and extract data per study using the codebook in `data/04-data-extraction/extraction-codebook.md`.
6. Regenerate Figures 5–6 with [`scripts/generate_fig5_fig6.py`](scripts/generate_fig5_fig6.py) from the included-studies table and compare against the manuscript.

## How to cite

See [`CITATION.cff`](CITATION.cff). Once archived on Zenodo, cite the versioned DOI for the exact snapshot you used, and the GitHub repository for the actively maintained version.

## License


## Authors / contacts

- Paolo Ciancarini — University of Bologna
- Domenico Garlisi — University of Palermo 
- Raffaele Giancarlo — University of Palermo
- Gennaro Grimaudo — University of Palermo
