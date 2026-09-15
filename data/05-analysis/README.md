# Analysis tables

Machine-readable transcriptions of the manuscript's synthesis tables, kept alongside the paper so the analysis is checkable and reusable independent of the PDF.

| File | Manuscript source | Confidence |
|---|---|---|
| `table-ii-maturity-assessment.csv` | Table II (§ II-C) | High — small, clearly legible table, transcribed directly. |
| `table-iii-representative-tools.csv` | Table III (§ IX-C) | High. |
| `table-iv-tool-devops-phase-mapping.csv` | Table IV / Appendix B (p. 14) | **Medium — verify before relying on it.** The tool names, IDs, and references were read directly and are high-confidence; the seven phase checkmarks per tool were transcribed from a dense, small-print matrix and cross-checked against the prose descriptions of each tool where the manuscript gives one, but were **not** verified cell-by-cell against the original LaTeX/table source. Confirm every row against the manuscript before citing this file as authoritative. |
| `table-v-comparison-previous-reviews.csv` | Table V / Appendix A (p. 24, expanded in §-by-§ prose on pp. 14–16) | High for the prose content; **the "Present SLR" row's corpus size (172) is transcribed as printed in Table V's header cell but conflicts with the 219 / "xx" / 122 figures reported elsewhere in the same draft** — see `../../docs/known-issues-and-todos.md`. |
| `existing-systems-section-ix.csv` | Section IX-C narrative (not a numbered table in the manuscript) | High — short narrative descriptions, directly transcribed. |

None of these files are placeholders — they contain the manuscript's actual reported data. What still needs reconciliation is the *inconsistent primary-study count* that shows up differently in Table I, the body text, the figure captions, and (now confirmed) Table V's header — not the table contents themselves.
