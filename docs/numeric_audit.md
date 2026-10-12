# Numerical audit of article results

The tables generated from `data/extraction/study_extraction.csv` were compared with the numerical claims
in the manuscript after the supplementary open-access retrieval round (corpus frozen 2026-08-06).

| Result | Canonical table | Manuscript claim | Status |
|---|---:|---:|---|
| Group A | 18 (39.1%) | 18 (39.1%) | Match |
| Group B | 18 (39.1%) | 18 (39.1%) | Match |
| Group C | 4 (8.7%) | 4 (8.7%) | Match |
| Group D | 6 (13.0%) | 6 (13.0%) | Match |
| Text interface | 21 (45.7%) | 45.7% | Match |
| Voice interface | 8 (17.4%) | 17.4% | Match |
| Multimodal interface | 11 (23.9%) | 23.9% | Match |
| Other interface | 4 (8.7%) | 8.7% | Match |
| Unspecified interface | 2 (4.3%) | 4.3% | Match |
| GPT family | 30 (65.2%) | 30 (65.2%) | Match |
| Llama family | 11 (23.9%) | 11 (23.9%) | Match |
| Mistral family | 2 (4.3%) | 2 (4.3%) | Match |
| Simulation validation | 9 (19.6%) | 9 (19.6%) | Match |
| Real validation | 19 (41.3%) | 19 (41.3%) | Match |
| Hybrid validation | 10 (21.7%) | 10 (21.7%) | Match |
| Other/offline validation | 8 (17.4%) | 8 (17.4%) | Match |
| Verification Level 1 | 20 (43.5%) | 20 | Match |
| Verification Level 2 | 19 (41.3%) | 19 | Match |
| Verification Level 3 | 7 (15.2%) | 7 (15.2%) | Match |
| Hallucination challenge | 25 (54.3%) | 25 (54.3%) | Match |
| Latency challenge | 17 (37.0%) | 17 | Match |
| Generalization challenge | 16 (34.8%) | 16 | Match |
| Complexity | 9 (19.6%) | 9 | Match |
| Physical constraints | 9 (19.6%) | 9 | Match |
| Misinterpretation | 7 (15.2%) | 7 | Match |

## Screening flow (PRISMA)

| Step | Canonical files | Manuscript claim | Status |
|---|---:|---:|---|
| Records identified | 183 | 183 | Match |
| Screening units | 148 (147 + 1 grouped row) | 148 | Match |
| Reports sought | 66 | 66 | Match |
| Assessed (full text) | 55 (`data/studies.csv`) | 55 | Match |
| Included | 46 (`study_extraction.csv`) | 46 | Match |
| Excluded (full text) | 9 | 9 | Match |
| Not retrieved | 11 (`not_retrieved.csv`) | 11 | Match |

## Resolved provenance note

- The 147 bibliographic records and the original `AdjunctProceedings*` grouped row account for the reported
  148 screening units. The 17 grouped proceedings records are explicit in `data/screening/grouped_exclusions.csv`.
- The supplementary open-access retrieval round (August 2026) recovered 18 of the 28 originally
  not-retrieved reports; 17 were assessed (11 included, 6 excluded) and 1 (liuSPECTRA) remains not
  retrieved. Per-report coding is in `data/screening/oa_retrieval_coding.csv`.
- The article treats all cross-study comparisons as descriptive/exploratory and reports no inferential
  statistics. Single-coder screening/extraction/adjudication is a declared limitation.
