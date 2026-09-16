# Figures

The manuscript's figures are architecture/UML diagrams (not data-driven) or charts derived from the included-studies data. This folder documents where each comes from and, for the data-driven ones, how to regenerate them.

| Figure | Manuscript title | Type | Source |
|---|---|---|---|
| Fig. 1 | CECC multilayer architecture (Cloud/Fog/Edge/Devices) | Conceptual diagram | Hand-drawn in the manuscript; not data-driven. Redraw from the description in Section I if a source file is wanted here. |
| Fig. 2 | MBSE for IoT accounting for DevOps (UML) | Conceptual diagram | Hand-drawn (Section III-A); not data-driven. |
| Fig. 3 | Structured, iterative DevOps workflow (development/integration/deployment) | Conceptual diagram | Hand-drawn (Section IV); not data-driven. |
| Fig. 4 | DevSecOps pipeline for IoT | Conceptual diagram | Hand-drawn (Section X-A/1); not data-driven. |
| Fig. 5 | Temporal distribution of the selected papers (2016–2026) | Data-driven bar chart | Regenerate with [`../scripts/generate-fig.py`](../scripts/generate-fig.py) from `../data/05-data-extraction/extraction-form.csv`. **Caption says 122 papers — reconcile against the "Reported selection counts" table in `../protocol/review-protocol.md` first.** |
| Fig. 6 | Distribution of the selected papers across research areas (heatmap) | Data-driven heatmap | Not currently regenerated — `generate-fig.py` produces Fig. 5 only. The manuscript's version is a 6×6 cross-tabulation heatmap (row area × column area, in %) built from `thematic_area`; re-add a Fig. 6 code path to the script once `thematic_area` supports multi-label assignment per paper (the manuscript's heatmap implies some papers count toward more than one area). |

Regenerated PNGs land in this folder as `fig5_temporal_distribution_regenerated.png` and are for validation only — they are not meant to replace the manuscript's own figures.
