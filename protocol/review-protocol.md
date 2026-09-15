# Review Protocol


## Framework

PRISMA-P, applied in three stages: **i) planning**, **ii) execution**, **iii) analysis**.

## Research questions

- **RQ1.** What are the reasons for considering DevOps as a strategic enabler for IoT?
- **RQ2.** Which practices and areas emerge from the recent literature on the integration of DevOps and IoT?
- **RQ3.** Which tools and frameworks facilitate the integration of DevOps and CI/CD into IoT?

## Planning

### Electronic databases

- Web of Science (WoS)
- IEEE Xplore
- ACM Digital Library
- Scopus

### Query string

Logical AND of DevOps synonyms and IoT synonyms. Synonyms were selected using the IEEE 2675 DevOps standard and the IEEE 2413 IoT standard.

```
(DevOps OR "CI/CD" OR CICD OR DevSecOps)
AND
(IoT OR "Internet of Things" OR "Cyber-Physical Systems" OR CPS OR "Sensors Network"
 OR "Connected Devices" OR "Embedded Systems" OR "Edge Systems" OR "Fog Systems")
```

See [`search-strings/`](search-strings/) for a suggested per-database field-search translation — verify each against the live database syntax before re-running, and archive the exact string actually executed alongside the raw export.

### Database searches

Two search passes:

1. **Primary search.** Covered the period 2015-01-01 to 2026-04-29; records downloaded 2026-04-30.
2. **Secondary search (forward-snowballing).** Conducted 2026-07-01 to 2026-09-03, seeded from the primary-search included set, once that set was identified.

### Filters

- Language: English.
- Publication type: articles and conference papers.
- Excluded: books, posters, short communications.

### Exclusion / inclusion criteria

Applied in order, to both the primary- and secondary-search result sets:

1. **Duplicate removal**, including conference papers that later appear, in extended form, as journal articles.
2. **Relevance.** An evaluation of the extent to which a paper covers the integration of DevOps and IoT; poor coverage leads to exclusion.

### Study selection process

Performed by two researchers, independently, at both the title/abstract and full-text screening stages. The two reviewers compared their evaluations; the other two authors validated the outcome (i.e., a 4-author team with 2 primary screeners + 2 validators/arbiters).

## Execution and analysis

This file is the complete **planning** stage of PRISMA-P: every decision here (databases, query string, filters, criteria, screening design, quality-scheme design, study-group taxonomy) was made before any screening happened. 
The **execution** and **analysis** stages that follow from this plan are not narrated in prose here — they are the actual, evolving data under `../data/`:

| Stage | Folder(s) | What it holds |
|---|---|---|
| Execution | `data/01-search-results/` | Raw per-database exports (primary + secondary search) |
| Execution | `data/02-screening/` | PRISMA flow counts, deduplication log, title/abstract and full-text screening decisions |
| Execution | `data/03-included-studies/` | The resulting primary studies, snowballed secondary studies, and background/supporting references |
| Execution | `data/04-data-extraction/` | Extraction codebook and the per-study extraction sheet |
| Analysis | `data/05-quality-assessment/` | Per-study strength/quality scores, using the [0,1] scheme defined above |
| Analysis | `data/06-analysis/` | Thematic synthesis and maturity assessment, the tool↔DevOps-phase mapping, and the comparison with prior reviews |

In short: **plan here, execute and analyze in `data/`.** Each `data/` subfolder has its own `README.md` with the exact file-by-file schema.


### Reported selection counts 

| Selection stage | Primary | Secondary |
|---|---:|---:|
| Search results | 1109 | 986 |
| Duplicate elimination (−) | 322 | 342 |
| Relevance and soundness (−) | 666 | 639 |
| Additional supporting studies (+) | 56 | 2 |
| **Total included studies** | **219*** | **7** |

### Quality / strength assessment

For each primary study the manuscript records, in addition to bibliographic information:
- clarity of research design,
- validity of claims,
- availability of reproducible elements,
- evaluation of threats to validity.

Each aspect is scored in [0,1]; the sum is the paper's overall weight. See [`../data/04-data-extraction/extraction-codebook.md`](../data/04-data-extraction/extraction-codebook.md).

### Study groups

Selected studies were classified into three groups:

1. **Motivations and challenges** — drivers, benefits, and challenges of adopting DevOps in IoT.
2. **Reviews of DevOps and IoT** — prior studies investigating the DevOps/IoT relationship (compared against this SLR in Table V / Appendix A).
3. **Thematic areas and supporting frameworks** — studies addressing specific DevOps-adoption areas in IoT, with the tools/frameworks they use. Further analyzed into the seven thematic areas (see below).

## Thematic synthesis (seven areas)

| # | Area | Manuscript section | Papers (per Table II/IV of manuscript) |
|---|---|---|---:|
| 1 | Novel Models for IoT | III | 28 |
| 2 | CI/CD for Development, Integration, and Deployment | IV | 35 |
| 3 | System-Wide Orchestration of Software and Hardware | V | 29 |
| 4 | Performance Monitoring | VI | 21 |
| 5 | Large-Scale Testing | VII | 24 |
| 6 | Security, Privacy and Risk Assessment | VIII | 25 |
| 7 | DevOps Framework for IoT (comparative analysis of existing frameworks) | IX | 11 |

Maturity of each area is rated on three indicators — *volume of evidence*, *tool availability*, *validation breadth* — into three levels: **Exploratory**, **Consolidating**, **Mature**. See `data/05-analysis-tables/table-ii-maturity-assessment.csv`.

## Accountability / reproducibility infrastructure already in place

- GitHub process-tracking repository: https://github.com/domenico-garlisi/DevOps-for-IoT-Systems-Methodologies-and-Software-Tools
- Zotero group library (papers grouped by source database, plus a directory of primary studies partitioned by research area): https://www.zotero.org/groups/6502633/devops-iot-library

This replication package is designed to complement — not duplicate — those two: the raw, evolving bibliography stays in Zotero/GitHub; the frozen, versioned protocol + data + tables tied to a specific manuscript draft live here and get archived to Zenodo.
