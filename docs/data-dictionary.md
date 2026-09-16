# Data dictionary

Quick index of every data file in this package and its column schema. For narrative context, see each folder's own `README.md`; for the extraction-specific field definitions, see `data/05-data-extraction/extraction-codebook.md`.

| File | Rows represent | Key columns |
|---|---|---|
| `data/01-primary-search/raw/<db>-primary-29042026.csv` (wos, ieee, acm, scopus) | One raw export record from that database, in the database's own native schema | `title`, `authors`/`author`, `year`, `doi`, `abstract` (exact column names vary per database export) |
| `data/01-primary-search/uniformed/<db>-29042026-uniformed.csv` (wos, ieee, acm, scopus) | Same records as the matching `raw/` file, remapped to one common schema | `source;entry_type;document_type;title;authors;year;doi;url;abstract;keywords;journal;booktitle;publisher;pages` |
| `data/02-screening/duplicate.csv` | One detected duplicate record | *(currently empty placeholder)* |
| `data/02-screening/excluded.csv` | One record excluded after surviving deduplication | *(currently empty placeholder)* |
| `data/03-secondary-search/secondary-studies-snowballing.csv` | One candidate record from the forward-snowballing secondary search (2026-07-01 to 2026-09-03), pre-dedup/screening | `Relevance;Presence;Reference;Authors;Title;Year;Source title;DOI;Abstract;Document Type;…` |
| `data/04-included-studies/primary-studies.csv` | One included primary study, post-screening | `ref_id`, `title`, `authors`, `year`, `venue`, `type`, `doi_or_url`, `database_source`, `study_group`, `thematic_area`, `quality_score_design`, `quality_score_validity`, `quality_score_reproducibility`, `quality_score_threats`, `quality_score_total`, `notes` |
| `data/04-included-studies/previous-reviews.csv` | One prior/related SLR selected for comparison | *(currently empty placeholder)* |
| `data/04-included-studies/supporting-background-references.csv` | One background/motivation reference cited for context | *(currently empty placeholder)* |
| `data/05-data-extraction/extraction-form.csv` | One extracted/screened study record (exported from the working spreadsheet below) | see `extraction-codebook.md`; includes `thematic_area`, `iot_context`, `devops_practices`, `tools_frameworks`, `quality_score_*`, `rq1_addressed`/`rq2_addressed`/`rq3_addressed` |
| `data/05-data-extraction/complete-process-v16.xlsx` (sheet `RELEVANT`) | One candidate/included study — the working extraction spreadsheet `extraction-form.csv` is exported from | same fields as `extraction-form.csv`, plus the underlying scoring/formula columns (`DESIGN`, `VALIDITY`, `REPLICABILITY`, `THREATS`, `PUNTO`, `Quality Score`, per-area `ALL*` flags) and a citation/quality-score summary block below the table |
| `data/06-analysis/maturity-assessment-table.csv` | One thematic area | `area`, `papers`, `tools`, `validation`, `maturity_level` |
| `data/06-analysis/tool-devops-phase-mapping-table.csv` | One tool/framework | `id`, `tool_framework`, `manuscript_ref`, `category`, one 0/1 column per DevOps phase (`modeling`, `development`, `deployment`, `orchestration`, `monitoring_visualization`, `testing`, `security_privacy`) |
| `data/06-analysis/comparison-previous-reviews-table.csv` | One prior review study (or the present SLR) | `study_ref`, `scope_and_objective`, `corpus_and_data_sources`, `method_and_outputs`, `relation_to_present_slr` |
| `data/06-analysis/existing-systems.csv` | One named system from the manuscript's existing-systems discussion | `system_name`, `focus_area`, `description`, `manuscript_refs` |
