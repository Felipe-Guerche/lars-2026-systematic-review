# Release notes — v1.0.13 (published 2026-10-12; corpus frozen 2026-08-06)

Definitive submission snapshot cited by the LARS 2026 manuscript. It supersedes v1.0.12. **No count,
taxonomy assignment, or result changed**; this release fixes one stale classification note and
harmonizes retrieval terminology across the documentation.

## What changed since v1.0.12

- **Data correction (`study_extraction.csv`):** the `classification_note` of
  `tziafasOpenWorldGraspingLarge2024` described "formal symbolic verification with an execution-feedback
  loop" — a remnant of earlier coding that contradicted the final classification. It now reads:
  "Runtime grasp-failure recovery without formal symbolic verification: failed or blocked grasps trigger
  autonomous re-grounding and re-planning (Algorithm 1 loop)." Group assignment (D), counts, percentages,
  and all generated results are unchanged.
- **Documentation harmonization:** `manuscript_sync.md`, `SR_supplement.md`, `numeric_audit.md`, and
  `provenance.md` now use the precise retrieval terminology — 18 candidates identified with
  open-access versions, **17 full texts retrieved and assessed**, 1 unobtainable (previously conflated as
  "18 recovered") — and point to release v1.0.13.
- `docs/provenance.md` additionally records that `scripts/generate_prisma.py` encodes the PRISMA flow
  counts explicitly and that `scripts/validate_data.py` verifies them against the canonical CSVs.

## Content (unchanged from v1.0.12)

- Canonical data: `studies.csv` (55 records: 46 included, 9 excluded), `not_retrieved.csv` (11),
  `study_extraction.csv` (46), `taxonomy_membership.csv` (46), `oa_retrieval_coding.csv` (18 candidates).
- Taxonomy A=18, B=18, C=4, D=6; verification levels L1/L2/L3 = 20/19/7; Group D spans all three levels.
- Regenerated `results/tables/*` and `results/figures/*`; `docs/numeric_audit.md` all Match.

## Citation

```bibtex
@misc{guerche2026larsrepo,
  author  = {Guerche, Felipe Delduque},
  title   = {LARS 2026 systematic review reproducibility repository},
  year    = {2026},
  version = {1.0.13},
  url     = {https://github.com/Felipe-Guerche/lars-2026-systematic-review/releases/tag/v1.0.13}
}
```
