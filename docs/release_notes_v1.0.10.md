# Release notes — v1.0.10 (published 2026-10-12; corpus frozen 2026-08-06)

Frozen reproducibility snapshot for the revised LARS 2026 manuscript (46-study corpus). This release
supersedes v1.0.9 and is the version cited by the article. The corpus freeze date (2026-08-06) is a
historical data date; the release publication date is 2026-10-12.

## What changed since v1.0.9

- **Supplementary open-access retrieval round (August 2026):** open-access versions of 18 of the 28
  originally not-retrieved reports were identified (arXiv, publisher open access, institutional
  repositories; verified against Semantic Scholar and OpenAlex). Seventeen full texts were retrieved and
  assessed under the frozen protocol in `reviews/protocol_a7b.md` (manuscript companion): 11 included,
  6 excluded (5 EC3, 1 EC1). One report (liuSPECTRA) remained unobtainable (ACM bronze OA bot-blocked).
  Final flow: **55 assessed, 46 included, 9 excluded, 11 not retrieved**.
- **New files:** `data/screening/oa_retrieval_coding.csv` — per-report coding of the 18 recovered
  reports (eligibility decision; dimensions D1-D4 and C1-C3 as Sim/Nao/Nao determinado with textual
  evidence and page references; single-coder adjudication flags).
- **Updated files:** `data/studies.csv` (55 rows), `data/screening/not_retrieved.csv` (11 rows),
  `data/extraction/study_extraction.csv` (46 rows), `data/extraction/taxonomy_membership.csv` (46 rows).
- **Taxonomy:** Group D now spans all three verification-formality levels (PaLM-E and open-world
  grasping recover without formal symbolic structure; RONAR uses a lightweight runtime scene graph).
  Distribution: A=18, B=18, C=4, D=6.
- **Regenerated outputs:** all `results/tables/*` and `results/figures/*` (including the taxonomy
  matrix, PRISMA flow 66/55/46/9/11, and verification-level chart).
- **Validation:** `scripts/validate_data.py`, `scripts/doublecheck_taxonomy.py` updated for the
  46-study corpus and passing; `docs/numeric_audit.md` records the manuscript-vs-data comparison.

## Provenance

- The bibliographic search snapshot is unchanged (ended 3 November 2025); the supplementary retrieval
  round is documented separately and does not extend the coverage window.
- Screening, extraction, taxonomy coding, and borderline adjudication were performed by a single coder
  (first author). No second-reviewer series exists; this limitation is declared in the article.
- Publisher PDFs, abstracts, and local attachment paths are not redistributed.

## Citation

Cite this release as:

```bibtex
@misc{guerche2026larsrepo,
  author  = {Guerche, Felipe Delduque},
  title   = {LARS 2026 systematic review reproducibility repository},
  year    = {2026},
  version = {1.0.10},
  url     = {https://github.com/Felipe-Guerche/lars-2026-systematic-review/releases/tag/v1.0.10}
}
```
