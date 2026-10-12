# Release notes — v1.0.12 (published 2026-10-12; corpus frozen 2026-08-06)

Definitive submission snapshot cited by the LARS 2026 manuscript. It supersedes v1.0.11. **No CSV,
taxonomy, count, or figure-generation change with respect to v1.0.11**; this release corrects and
completes the supplementary documentation.

## What changed since v1.0.11 (documentation only)

- `docs/SR_supplement.md` — the "Per-Database Yield Breakdown" section now separates the
  **original screening flow before supplementary retrieval** (28 not retrieved / 38 assessed /
  3 excluded / 35 included) from the **final flow** used in the article (11 not retrieved / 55 assessed /
  9 excluded / 46 included), and the `not_retrieved.csv` description now correctly states that the file
  contains 11 records (10 with no open-access version + 1 bot-blocked), not 28.

## Content (unchanged from v1.0.11)

- Supplementary open-access retrieval round (August 2026): 18 candidates with open-access versions
  identified; 17 full texts retrieved and assessed (11 included, 6 excluded); 1 unobtainable.
  Per-report coding in `data/screening/oa_retrieval_coding.csv` (frozen protocol, single coder).
- Canonical data: `studies.csv` (55), `not_retrieved.csv` (11), `study_extraction.csv` (46),
  `taxonomy_membership.csv` (46); taxonomy A=18, B=18, C=4, D=6.
- Regenerated `results/tables/*` and `results/figures/*` (including `results/figures/prisma.pdf`,
  the PRISMA diagram used in the article); `docs/numeric_audit.md` all Match.

## Citation

```bibtex
@misc{guerche2026larsrepo,
  author  = {Guerche, Felipe Delduque},
  title   = {LARS 2026 systematic review reproducibility repository},
  year    = {2026},
  version = {1.0.12},
  url     = {https://github.com/Felipe-Guerche/lars-2026-systematic-review/releases/tag/v1.0.12}
}
```
