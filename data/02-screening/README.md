# Screening

- `prisma-flow-counts.csv` — the funnel counts as currently reported across the manuscript (Table I, body text, figure captions). **These disagree with each other in the current draft** — see `../../docs/known-issues-and-todos.md`. Treat this file as a record of *what the draft currently claims*, not as verified ground truth, until reconciled.
- `duplicate.csv` — one row per duplicate record found, 
- `excluded.csv` — one row per unique record surviving deduplication; both reviewers' independent decisions plus the reconciled final decision. Reviewer identities can be pseudonymized (e.g. `R1`, `R2`) if the authors prefer not to name themselves in the public dataset.
- `full-text-screening-template.csv` — one row per record that passed title/abstract screening; full-text decision, exclusion criterion if excluded, and (if included) which of the three study groups / seven thematic areas it was assigned to.
