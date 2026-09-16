# Data-extraction codebook


## Bibliographic / synoptic summary fields

| Field | Description |
|---|---|
| `ref_id` | Citation key as used in the manuscript bibliography (e.g. `[25]`) |
| `title`, `authors`, `year`, `venue`, `type` | Standard bibliographic metadata |
| `citations` | Citation count at time of extraction (record the date checked) |

## Quality / strength assessment

Each of the four aspects below is scored in **[0, 1]**; `quality_score_total` is their sum (range 0–4, higher = stronger).

| Field | What it captures |
|---|---|
| `quality_score_design` | Clarity of research design |
| `quality_score_validity` | Validity of claims |
| `quality_score_reproducibility` | Availability of reproducible elements: tools, datasets, or replicable protocols |
| `quality_score_threats` | Whether the study evaluates threats to validity |


| Field | Description                                                                                                                                                          |
|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `thematic_area` | One of the six areas (see `../../protocol/review-protocol.md`) |
| `iot_context` | Free text: the specific IoT context/domain the study addresses (e.g. smart building, vehicular, industrial)                                                          |
| `devops_practices` | Free text / semicolon-separated: which DevOps practices are discussed (e.g. CI/CD, IaC, MaC, orchestration)                                                          |
| `tools_frameworks` | Semicolon-separated list of named tools/frameworks the study uses or proposes; cross-reference against `../05-analysis-tables/table-iv-tool-devops-phase-mapping.csv` |
