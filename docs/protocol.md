# Review protocol snapshot

## Objective

Identify empirical studies that combine large language models or vision-language models with robot planning, control, task decomposition, hallucination mitigation, formal verification, or autonomous error recovery.

## Search

The final search/update was completed on 3 November 2025. The publication window was January 2020 through 3 November 2025, with partial coverage of November.

Searches covered Scopus, IEEE Xplore, and ACM Digital Library. The nine database-specific strings are in `data/search/search_strings.md`; the reported yields are in `data/search/database_yields.csv`.

## Eligibility

### Inclusion

- Uses or proposes an LLM/VLM for robot planning, control, task decomposition, or semantic interpretation of robot task state (e.g., execution logs).
- Includes empirical validation in simulation, physical hardware, hybrid evaluation, or an offline benchmark.
- Addresses hallucination mitigation, formal verification, grounding, or error recovery.

### Exclusion

- Robotic manipulation without a relevant mobile-robot, planning, verification, or recovery contribution.
- Purely theoretical work without implementation or empirical evaluation.
- No relevant safety, verification, grounding, hallucination-mitigation, or recovery mechanism.

## Selection snapshot

```text
183 records identified
 35 duplicates removed
148 screening units screened by title/abstract
 82 screening units excluded at screening
 66 full-text reports sought
 28 reports not retrieved in the original retrieval
 18 open-access candidates identified in the supplementary retrieval round (Aug 2026)
 17 of those full texts retrieved and assessed (11 included, 6 excluded); 1 unobtainable
 11 reports not retrieved in total
 55 reports assessed for eligibility
  9 reports excluded at full text (3 original + 6 supplementary)
 46 studies included
```

The numerical flow is reproduced by `scripts/generate_prisma.py`. The 148 screening units comprise 147 bibliographic records plus the original `AdjunctProceedings*` aggregate row; the 82 exclusions comprise 65 non-included screening rows and 17 grouped proceedings records. The supplementary open-access retrieval round (August 2026) is a retrieval step documented separately from the search snapshot (ended 3 November 2025); its per-report coding is in `data/screening/oa_retrieval_coding.csv`, under the frozen protocol with anti-exclusion rules (missing information coded as "not determined"). The provenance limitation is documented in `docs/provenance.md`.
