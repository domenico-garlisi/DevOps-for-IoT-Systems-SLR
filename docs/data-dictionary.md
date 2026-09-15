# Data dictionary

Quick index of every data file in this package and its column schema. For narrative context, see each folder's own `README.md`; for the extraction-specific field definitions, see `data/04-data-extraction/extraction-codebook.md`.

| File | Rows represent | Key columns |
|---|---|---|
| `data/02-screening/prisma-flow-counts.csv` | One PRISMA funnel stage | `search_pass`, `stage`, `count`, `source_note` |
| `data/02-screening/deduplication-log-template.csv` | One detected duplicate | `record_id`, `title`, `doi`, `duplicate_type`, `kept_record_id` |
| `data/02-screening/title-abstract-screening-template.csv` | One record screened at title/abstract stage | `record_id`, `reviewer_1_decision`, `reviewer_2_decision`, `final_decision` |
| `data/02-screening/full-text-screening-template.csv` | One record screened at full-text stage | `record_id`, `final_decision`, `exclusion_criterion`, `study_group`, `thematic_area` |
| `data/03-included-studies/primary-studies-template.csv` | One included primary study | `ref_id`, `study_group`, `thematic_area`, `quality_score_total` |
| `data/03-included-studies/secondary-studies-snowballing-template.csv` | One snowballed secondary study | `ref_id`, `found_via_ref_id`, `snowball_direction` |
| `data/03-included-studies/supporting-background-references-template.csv` | One background/tool reference | `ref_id`, `title_or_tool_name`, `cited_for` |
| `data/04-data-extraction/extraction-form-template.csv` | One extracted study record | see `extraction-codebook.md` |
| `data/05-analysis-tables/table-ii-maturity-assessment.csv` | One thematic area | `area`, `papers`, `tools`, `validation`, `maturity_level` |
| `data/05-analysis-tables/table-iii-representative-tools.csv` | One thematic area | `area`, `main_tools_and_frameworks` |
| `data/05-analysis-tables/table-iv-tool-devops-phase-mapping.csv` | One tool/framework | `id`, `tool_framework`, `manuscript_ref`, one 0/1 column per DevOps phase |
| `data/05-analysis-tables/table-v-comparison-previous-reviews.csv` | One prior review study (or the present SLR) | `study_ref`, `scope_and_objective`, `corpus_and_data_sources`, `method_and_outputs`, `relation_to_present_slr` |
| `data/05-analysis-tables/existing-systems-section-ix.csv` | One named system from Section IX | `system_name`, `focus_area`, `description`, `manuscript_refs` |

`ref_id` / `manuscript_ref` values match the citation keys used in the manuscript bibliography (e.g. `[25]`) so any file here can be cross-referenced against `manuscript/`.
