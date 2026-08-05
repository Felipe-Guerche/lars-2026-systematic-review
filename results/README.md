# Generated results

Run `python scripts/generate_results.py` to regenerate the CSV tables and the standard figures. Run `python scripts/generate_taxonomy_tree.py` and `python scripts/generate_prisma.py` for the two publication diagrams.

All percentages in the tables use 35 studies as the denominator unless explicitly marked otherwise. LLM-family and challenge counts are multi-label counts, so their percentages can sum to more than 100%.

The current generated outputs include the following linked tables and figures:

| Analysis | Table | Figure |
|---|---|---|
| Taxonomy distribution | [`taxonomy_groups.csv`](tables/taxonomy_groups.csv) | [`taxonomy_groups.png`](figures/taxonomy_groups.png) · [`taxonomy_groups.pdf`](figures/taxonomy_groups.pdf) |
| Interface modalities | [`interface_modalities.csv`](tables/interface_modalities.csv) | [`interface_modalities.png`](figures/interface_modalities.png) · [`interface_modalities.pdf`](figures/interface_modalities.pdf) |
| LLM-family mentions | [`llm_families.csv`](tables/llm_families.csv) | [`llm_families.png`](figures/llm_families.png) · [`llm_families.pdf`](figures/llm_families.pdf) |
| Validation environments | [`validation_methods.csv`](tables/validation_methods.csv) | [`validation_environments.png`](figures/validation_environments.png) · [`validation_environments.pdf`](figures/validation_environments.pdf) |
| Top-ten challenges | [`challenge_frequency_top10.csv`](tables/challenge_frequency_top10.csv) | [`challenges_pareto.png`](figures/challenges_pareto.png) · [`challenges_pareto.pdf`](figures/challenges_pareto.pdf) |
| Publication years | [`publication_years.csv`](tables/publication_years.csv) | — |
| Taxonomy × validation | [`taxonomy_by_validation.csv`](tables/taxonomy_by_validation.csv) | — |
| Expertise/safety by group | [`expertise_safety_by_group.csv`](tables/expertise_safety_by_group.csv) | [`expertise_safety.png`](figures/expertise_safety.png) · [`expertise_safety.pdf`](figures/expertise_safety.pdf) |
| PRISMA flow | — | [`prisma.png`](figures/prisma.png) · [`prisma.pdf`](figures/prisma.pdf) |
| Taxonomy tree | — | [`taxonomy_tree.png`](figures/taxonomy_tree.png) · [`taxonomy_tree.pdf`](figures/taxonomy_tree.pdf) |
