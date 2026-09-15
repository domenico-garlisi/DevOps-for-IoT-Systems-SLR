# Figures

The manuscript's figures are architecture/UML diagrams (not data-driven) or charts derived from the included-studies data. This folder documents where each comes from and, for the data-driven ones, how to regenerate them.

| Figure | Manuscript title | Type | Source |
|---|---|---|---|
| Fig. 1 | CECC multilayer architecture (Cloud/Fog/Edge/Devices) | Conceptual diagram | Hand-drawn in the manuscript; not data-driven. Redraw from the description in Section I if a source file is wanted here. |
| Fig. 2 | MBSE for IoT accounting for DevOps (UML) | Conceptual diagram | Hand-drawn (Section III-A); not data-driven. |
| Fig. 3 | Structured, iterative DevOps workflow (development/integration/deployment) | Conceptual diagram | Hand-drawn (Section IV); not data-driven. |
| Fig. 4 | DevSecOps pipeline for IoT | Conceptual diagram | Hand-drawn (Section X-A/1); not data-driven. |
| Fig. 5 | Temporal distribution of the selected papers (2016–2026) | Data-driven bar chart | Regenerate with [`../scripts/generate_fig5_fig6.py`](../scripts/generate_fig5_fig6.py) from `../data/03-included-studies/primary-studies-template.csv` once populated. **Caption says 122 papers — reconcile against `../docs/known-issues-and-todos.md` first.** |
| Fig. 6 | Distribution of the selected papers across research areas (heatmap) | Data-driven heatmap | Same script/source as Fig. 5. The manuscript's version is a 6×6 cross-tabulation heatmap (row area × column area, in %); the regeneration script here produces a simpler per-area bar chart as a starting point — extend it to a full cross-tab once `thematic_area` supports multi-label assignment per paper (the manuscript's heatmap implies some papers count toward more than one area). |

Regenerated PNGs land in this folder as `fig5_temporal_distribution_regenerated.png` / `fig6_thematic_distribution_regenerated.png` and are for validation only — they are not meant to replace the manuscript's own figures.
