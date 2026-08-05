# Analysis scripts

The scripts are adapted from the working analysis files used for the manuscript:

- `generate_results.py` adapts `corpus/scripts/generate_figures_en.py` and adds reproducible CSV result tables.
- `generate_taxonomy.py` generates the two-dimensional taxonomy matrix; counts are read from the canonical extraction.
- `generate_prisma.py` adapts `figures/generate_prisma.py`; the flow arithmetic is asserted before rendering.
- `normalize_source.py` converts the local Portuguese extraction/source exports into the English public tables.
- `validate_data.py` is the lightweight integrity check for the public package.
- `doublecheck_taxonomy.py` checks the five formal-method boundary cases and the A/B/C/D totals.

The figure scripts use repository-relative paths. They do not read PDFs, Zotero attachments, or external absolute paths.
