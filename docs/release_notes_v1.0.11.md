# Release notes — v1.0.11 (published 2026-10-12; corpus frozen 2026-08-06)

Documentation-consistency release cited by the revised LARS 2026 manuscript. It supersedes v1.0.10, whose
tag pointed to a commit predating the final documentation harmonization; v1.0.11 tags the corrected
`main` directly. **No scientific results, CSVs, counts, or figures changed with respect to v1.0.10.**

## What changed since v1.0.10 (documentation only)

- `docs/SR_supplement.md` — the manuscript supplement is now part of the public release (PRISMA flow,
  group lists, Group D C1-C3 table, counter-example table, R1-R4 traceability, moved figures list).
- `README.md`, `docs/protocol.md`, `docs/provenance.md`, `docs/taxonomy_audit.md`,
  `data/extraction/README.md`, `data/screening/README.md` — harmonized to the 46-study corpus
  (55 assessed / 46 included / 9 excluded / 11 not retrieved) and to the 17-retrieved-vs-18-candidates
  wording of the supplementary retrieval round.
- `CITATION.cff` — release date reflects publication (2026-10-12); corpus freeze date (2026-08-06) is
  recorded in these notes as a historical data date.

## Content (unchanged from v1.0.10)

- Supplementary open-access retrieval round (August 2026): 18 candidates with open-access versions
  identified; 17 full texts retrieved and assessed (11 included, 6 excluded); 1 unobtainable.
  Per-report coding in `data/screening/oa_retrieval_coding.csv` (frozen protocol, single coder).
- Canonical data: `studies.csv` (55), `not_retrieved.csv` (11), `study_extraction.csv` (46),
  `taxonomy_membership.csv` (46).
- Taxonomy: Group D spans all three verification-formality levels; distribution A=18, B=18, C=4, D=6.
- Regenerated `results/tables/*` and `results/figures/*`; `docs/numeric_audit.md` all Match.

## Citation

```bibtex
@misc{guerche2026larsrepo,
  author  = {Guerche, Felipe Delduque},
  title   = {LARS 2026 systematic review reproducibility repository},
  year    = {2026},
  version = {1.0.11},
  url     = {https://github.com/Felipe-Guerche/lars-2026-systematic-review/releases/tag/v1.0.11}
}
```
