# Taxonomy audit

The canonical extraction currently assigns the 35 included studies as follows:

| Group | Definition | Studies | Share |
|---|---|---:|---:|
| A | Direct generation | 14 | 40.0% |
| B | Static neuro-symbolic translation | 16 | 45.7% |
| C | Formal verification without autonomous feedback | 2 | 5.7% |
| D | Execution-aware recovery | 3 | 8.6% |
| **Total** |  | **35** | **100.0%** |

## Boundary cases checked

- `Chalvatzaki2023` remains in **C**: GPT-2 produces PDDL subproblems solved by Fast Downward, but the paper does not provide autonomous execution-error recovery.
- `Patton2024` remains in **C**: the LLM-guided program-synthesis method includes unrealizability checking, but no autonomous robot execution-recovery loop.
- `Capitanelli2024` is in **D**: SPEM uses PDDL/VAL precondition checks before execution and resets/replans when the current state is incompatible.
- `Zhang2023` is in **D**: the system continuously checks the current state and replans when it is inconsistent with expectations.
- `Wang2025Conformal` is in **D** under the operational definition used here: the LTL planner receives execution obstacles and issues alternative subtasks automatically. The limitation that human assistance may be needed for non-singleton uncertainty sets is recorded in the classification note; it does not replace the automated physical-obstacle recovery loop.

The older verification report claiming Group C=4 and Group D=1 is stale. It must not be used for tables or figures.

The taxonomy figure crosses two dimensions: symbolic structure (none, lightweight/static, or formal) and autonomous feedback (absent or present). The two non-formal feedback cells are empty in the included corpus. Group D occupies the formal-plus-feedback cell in the observed corpus; formal verification is not the defining criterion of execution-aware recovery. The research gap is the absence of a Group-D system meeting the dynamic, unstructured deployment requirements.
