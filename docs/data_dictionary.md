# Data dictionary

## `data/studies.csv`

| Field | Meaning |
|---|---|
| `study_id` | Stable internal identifier used by the extraction files |
| `screening_status` | `included` or `excluded_full_text` |
| `exclusion_reason` | Reason for a full-text exclusion, when applicable |
| `title` | Published title |
| `authors` | Author string from the bibliographic record |
| `publication_year` | Publication year |
| `publication_date` | Date available in the bibliographic record |
| `item_type` | Journal article, conference paper, or other Zotero type |
| `publication_title` | Journal or venue |
| `doi` | DOI, when available |
| `url` | DOI or publisher URL |

## `data/extraction/study_extraction.csv`

The 35 included studies are coded in English. Each evidence field preserves a bounded quotation or evidence note from the source record. The main fields are:

- `study_id`, `title`, `publication_year`, `authors`;
- `interface_modality`, `interface_details`;
- `uses_llm`, `llm_family`, `llm_version`, `mitigation_strategy`;
- `performed_validation`, `validation_method`, `validation_metrics`;
- `application_domain`, `robotic_platform`;
- `main_challenges`, `future_work`;
- `symbolic_method_role`, `mitigated_error`, `required_expertise`;
- `taxonomy_group` and `classification_note`.

Evidence columns use the prefix `evidence_` and correspond to the associated field.

## Taxonomy groups

- **A — Direct generation:** LLM use without a formal symbolic parser or verifier.
- **B — Static neuro-symbolic translation:** lightweight symbolic structure or one-shot translation without formal verification and autonomous recovery.
- **C — Formal verification without autonomous feedback:** formal planning, verification, or unrealizability checking without an autonomous execution-recovery loop.
- **D — Execution-aware recovery:** an execution-feedback loop changes or repairs the plan without a human decision at the recovery step. All three Group-D studies in this corpus also use formal symbolic verification, but that is an observed property rather than the defining criterion.

The group is a mutually exclusive study-level classification. It is not a measure of overall paper quality.
