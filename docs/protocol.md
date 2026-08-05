# Review protocol snapshot

## Objective

Identify empirical studies that combine large language models or vision-language models with robot planning, control, task decomposition, hallucination mitigation, formal verification, or autonomous error recovery.

## Search

The final search/update was completed on 3 November 2025. The publication window was January 2020 through 3 November 2025, with partial coverage of November.

Searches covered Scopus, IEEE Xplore, and ACM Digital Library. The nine database-specific strings are in `data/search/search_strings.md`; the reported yields are in `data/search/database_yields.csv`.

## Eligibility

### Inclusion

- Uses or proposes an LLM/VLM for robot planning, control, or task decomposition.
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
148 records screened by title/abstract
 82 records excluded at screening
 66 full-text reports sought
 28 reports not retrieved
 38 reports assessed for eligibility
  3 reports excluded at full text
 35 studies included
```

The numerical flow is reproduced by `scripts/generate_prisma.py`. The provenance limitation concerning the 147 available bibliographic entries versus 148 reported screened records is documented in `docs/provenance.md`.
