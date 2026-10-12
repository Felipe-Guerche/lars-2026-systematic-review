# Screening archive

- `all_records.csv`: 147 bibliographic records available in the working archive, including 17 records mapped to the confirmed grouped `AdjunctProceedings*` exclusion.
- `first_screening.csv`: 131 explicit title/abstract decisions from the original triage export, including the `AdjunctProceedings*` group row.
- `grouped_exclusions.csv`: the 17 proceedings/companion-volume records covered by the grouped proceedings decision.
- `not_retrieved.csv`: the 11 records still not retrieved for full-text assessment (10 with no open-access version found + 1 bot-blocked: liuSPECTRA). The original set of 28 not-retrieved candidates was reduced by the supplementary open-access retrieval round (August 2026), which identified 18 candidates with open-access versions: 17 full texts were retrieved and assessed (11 included, 6 excluded) and 1 remained unobtainable.
- `oa_retrieval_coding.csv`: per-report coding of the 18 candidates identified in the supplementary retrieval round (eligibility decision; D1-D4 and C1-C3 dimensions with textual evidence and page references; single-coder adjudication flags).
- `full_text_decisions.csv`: 55 full-text decisions, including 46 included studies and 9 exclusions (3 in the original review, 6 in the supplementary round).

The grouped records are administrative proceedings metadata, not additional primary studies. Screening and extraction were performed by one primary reviewer; no independent second-reviewer decision series is included, so no agreement statistic is reported. The 148-unit PRISMA screening count includes the original grouped proceedings row in addition to the 147 bibliographic records; this representation is explained in `docs/provenance.md`.
