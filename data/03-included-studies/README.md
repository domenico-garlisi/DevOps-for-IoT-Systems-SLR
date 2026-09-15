# Included studies

- `primary-studies-template.csv` — the studies returned by the primary database search and retained after screening (manuscript Table I; count to be reconciled, see known issues). `thematic_area` should use one of the seven areas from `../../protocol/review-protocol.md` (or "DevOps Framework for IoT" for the Section IX comparative-analysis group). `quality_score_*` columns follow the [0,1]-per-aspect scheme in `../04-data-extraction/extraction-codebook.md`.
- `secondary-studies-snowballing-template.csv` — the 7 studies added via forward-snowballing (manuscript Table I, secondary search), with the `found_via_ref_id` linking back to the primary study whose citations/citing-papers surfaced it.
- `supporting-background-references-template.csv` — the ~56 background/general-purpose references (standards, tools, frameworks such as Docker) cited for context rather than as primary studies (manuscript Section II-B text and Appendix B / Table IV tool references).
- `bibtex/` (create on export) — full reference list exported from the Zotero group library (https://www.zotero.org/groups/6502633/devops-iot-library) as `.bib`, kept in sync with the CSVs above.
