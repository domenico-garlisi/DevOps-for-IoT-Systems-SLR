# Data-extraction codebook

Defines the fields recorded per primary study, per the manuscript's own "synoptic papers summary template" and "synoptic papers strength template" (Section II-A).

## Bibliographic / synoptic summary fields

| Field | Description |
|---|---|
| `ref_id` | Citation key as used in the manuscript bibliography (e.g. `[25]`) |
| `title`, `authors`, `year`, `venue`, `type` | Standard bibliographic metadata |
| `database_source` | Which database(s) the record was retrieved from (for citations-per-database bookkeeping) |
| `total_citations` | Citation count at time of extraction (record the date checked) |
| `study_group` | One of: `motivations_and_challenges`, `review_of_devops_and_iot`, `thematic_area_and_framework` |
| `thematic_area` | One of the seven areas (see `../../protocol/review-protocol.md`), or blank if `study_group` is not `thematic_area_and_framework` |
| `iot_context` | Free text: the specific IoT context/domain the study addresses (e.g. smart building, vehicular, industrial) |
| `devops_practices` | Free text / semicolon-separated: which DevOps practices are discussed (e.g. CI/CD, IaC, MaC, orchestration) |
| `tools_frameworks` | Semicolon-separated list of named tools/frameworks the study uses or proposes; cross-reference against `../05-analysis-tables/table-iv-tool-devops-phase-mapping.csv` |

## Quality / strength assessment (per manuscript Section II-A "Summary Statistics of Primary Studies")

Each of the four aspects below is scored in **[0, 1]**; `quality_score_total` is their sum (range 0–4, higher = stronger).

| Field | What it captures |
|---|---|
| `quality_score_design` | Clarity of research design |
| `quality_score_validity` | Validity of claims |
| `quality_score_reproducibility` | Availability of reproducible elements: tools, datasets, or replicable protocols |
| `quality_score_threats` | Whether the study evaluates threats to validity — scored per the authors' *explicit* mention of weaknesses/future directions when threats aren't addressed directly |

The manuscript notes these cumulative scores are computed for every primary study but, "in order to keep our presentation within journal limits," are not reported in the paper body — they are meant to live in "the provided additional material," i.e. this replication package.

## Notes

- Studies belonging to the "Reviews of DevOps and IoT" group that are directly compared against this SLR (the 9 studies `[14]`–`[22]`/`[21],[22]` combined) additionally get a row in `../05-analysis-tables/table-v-comparison-previous-reviews.csv`, which records scope, corpus/data sources, method/outputs, and relation to the present SLR along the five dimensions the manuscript's Appendix A defines (SLR scope; research questions; corpus and data sources; inclusion/exclusion criteria and synthesis method; domain coverage and findings).
- The five "Existing Systems" case studies from Section IX (JuNo-OPS, DsP-Installer, PROMENADE, Git-Ku IoT, 5G-IoT) are not primary *studies* to screen but named systems described within primary studies — track them via the `tools_frameworks` field of whichever `ref_id` introduces each one, rather than as separate rows here.
