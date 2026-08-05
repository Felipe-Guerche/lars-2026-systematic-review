# v1.0.9 — Reproducibility package

This release is the public reproducibility snapshot cited by the LARS 2026 systematic review.

## Authorship and maintenance

Repository development, release engineering, and maintenance are credited to **Felipe Delduque Guerche** (`Felipe-Guerche`). The associated article has a separate scientific author list; repository development credit should not be inferred from the article authorship.

## Included

- Canonical search, screening, full-text, and study-level extraction data.
- Regenerated result tables and publication figures.
- Validation and figure-generation scripts with repository-relative paths.
- Updated taxonomy documentation, provenance notes, and manuscript synchronization checklist.
- Added `CITATION.cff` and a repository citation block to the README.
- Corrected terminology for the four taxonomy groups and Verification Formality Level.

## Validated snapshot

- 183 records before deduplication; 148 screening units after deduplication.
- 66 reports sought for retrieval; 28 not retrieved; 38 assessed; 35 included.
- Taxonomy counts: Group A = 14, Group B = 16, Group C = 2, Group D = 3.
- Screening, extraction, and taxonomy validation scripts pass.
- The associated IEEE manuscript compiles to six pages.

## Reproduce

From a clean checkout:

```bash
python -m pip install -r requirements.txt
python scripts/validate_data.py
python scripts/doublecheck_taxonomy.py
python scripts/generate_results.py
python scripts/generate_taxonomy.py
python scripts/generate_prisma.py
```

Generated tables and figures are written to `results/`.

## Data and privacy policy

This release contains derived bibliographic metadata, screening decisions, extraction annotations, scripts, and documentation. It does not redistribute publisher PDFs, protected files, local Zotero attachments, local file paths, credentials, or private working files. Third-party metadata and quoted evidence remain subject to their original rights.

## Taxonomy note

Group D is named **Runtime plan adaptation and recovery**. Verification Formality Level describes the formal verification dimension; it is not a claim of physical-world safety or a guarantee beyond the encoded model and specification.
