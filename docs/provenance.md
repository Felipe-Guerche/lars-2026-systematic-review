# Provenance and data policy

## Search

The final search/update is recorded as 3 November 2025. The publication window is January 2020 through 3 November 2025, so November 2025 is incomplete.

The reported raw yields are 99 records from Scopus, 45 from IEEE Xplore, and 39 from ACM Digital Library (183 total). The query strings and query-level yields are in `data/search/`.

The Zotero CSV files available in the working archive contain 98 imported rows. They are preserved as sanitized imported metadata and are not used as raw database yields.

## Screening

The final full-text set has 38 records: 35 included and 3 excluded. The three full-text exclusions are retained with their reasons in `data/screening/full_text_decisions.csv` and `data/studies.csv`. Of the 66 reports sought for retrieval, 28 were inaccessible because UFSCar institutional access/login did not provide the publisher PDFs; protected files are not redistributed.

The working screening archive contains 147 bibliographic entries and 131 explicit title/abstract decisions. The manuscript reports 148 records after deduplication; the missing record and the 17 records without an explicit decision are not fabricated. Until they are reconciled, this package must not be described as a complete record-level reconstruction of the 183-record PRISMA flow.

Screening and extraction were performed by the primary reviewer. No independent second-reviewer decision series or audit table was retained, so inter-rater agreement statistics are not reported. Five snowballing papers are documented as counter-examples and are not part of the 35-study corpus.

## Analysis scope

Cross-study counts and group comparisons are descriptive/exploratory. The package does not support inferential or causal claims about time, robot type, validation environment, model family, or mitigation strategy.

## Copyright and privacy

Publisher PDFs, abstracts copied from publisher records, local file paths, and Zotero attachment fields are not redistributed. DOI links and derived study-level annotations are retained.

## Source-of-truth rule

A result is valid only when it can be regenerated from the files in `data/` by the scripts in `scripts/`. Hand-edited figures and stale Portuguese extraction files are not canonical sources.
