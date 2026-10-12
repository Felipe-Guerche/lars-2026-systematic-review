# Release notes — v1.1 (published 2026-10-12; corpus frozen 2026-08-06)

Definitive submission snapshot cited by the LARS 2026 manuscript. It supersedes v1.0.13 and is cut
directly from the corrected `main`, so the tag content matches the documentation shipped with the article.
**No count, taxonomy assignment, or scientific result changed with respect to v1.0.13.**

## What changed since v1.0.13 (documentation only)

- `README.md` — release-notes link updated to this release.
- `docs/SR_supplement.md` — R1--R4 traceability now points to Section V of the main paper (the discussion
  section in the final layout).
- `docs/manuscript_sync.md` — final six-page compilation recorded with its actual date (2026-10-12).

## Content (unchanged from v1.0.13)

- Canonical data: `studies.csv` (55 records: 46 included, 9 excluded), `not_retrieved.csv` (11),
  `study_extraction.csv` (46, including the corrected Tziafas classification note),
  `taxonomy_membership.csv` (46), `oa_retrieval_coding.csv` (18 candidates: 17 full texts retrieved and
  assessed, 1 unobtainable).
- Taxonomy A=18, B=18, C=4, D=6; verification levels L1/L2/L3 = 20/19/7; Group D spans all three levels.
- Regenerated `results/tables/*` and `results/figures/*`; `docs/numeric_audit.md` all Match.
- Manuscript supplement included as `docs/SR_supplement.md`.

## Citation

```bibtex
@misc{guerche2026larsrepo,
  author  = {Guerche, Felipe Delduque},
  title   = {LARS 2026 systematic review reproducibility repository},
  year    = {2026},
  version = {1.1},
  url     = {https://github.com/Felipe-Guerche/lars-2026-systematic-review/releases/tag/v1.1}
}
```
