# Numerical audit of article results

The tables generated from `data/extraction/study_extraction.csv` were compared with the numerical claims currently present in the manuscript.

| Result | Canonical table | Manuscript claim | Status |
|---|---:|---:|---|
| Group A | 14 (40.0%) | 14 (40.0%) | Match |
| Group B | 16 (45.7%) | 16 (45.7%) | Match |
| Group C | 2 (5.7%) | 2 (5.7%) | Match |
| Group D | 3 (8.6%) | 3 (8.6%) | Match |
| Text interface | 17 (48.6%) | 48.6% | Match |
| Voice interface | 8 (22.9%) | 22.9% | Match |
| Multimodal interface | 5 (14.3%) | 14.3% | Match |
| Other interface | 3 (8.6%) | 8.6% | Match |
| Unspecified interface | 2 (5.7%) | 5.7% | Match |
| GPT family | 21 (60.0%) | 21 (60.0%) | Match |
| Llama family | 9 (25.7%) | 9 (25.7%) | Match |
| Mistral family | 2 (5.7%) | 2 (5.7%) | Match |
| Simulation validation | 8 (22.9%) | 8 (22.9%) | Match |
| Real validation | 12 (34.3%) | 12 (34.3%) | Match |
| Hybrid validation | 8 (22.9%) | 8 (22.9%) | Match |
| Other/offline validation | 7 (20.0%) | 7 (20.0%) | Match |
| Hallucination challenge | 22 (62.9%) | 22 (62.9%) | Match |
| Latency challenge | 15 (42.9%) | 15 | Match |
| Generalization challenge | 11 (31.4%) | 11 | Match |
| Misinterpretation | 7 (20.0%) | 7 | Match |
| Physical constraints | 7 (20.0%) | 7 | Match |

## Resolved provenance note

- The 147 bibliographic records and the original `AdjunctProceedings*` grouped row account for the reported 148 screening units. The 17 grouped proceedings records and 28 not-retrieved candidates are explicit in `data/screening/`.
- The article treats all cross-study comparisons as descriptive/exploratory and reports no inferential statistics.
