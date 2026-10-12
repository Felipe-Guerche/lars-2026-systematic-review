# Taxonomy audit

The canonical extraction assigns the 46 included studies as follows (corpus frozen 2026-08-06):

| Group | Definition | Studies | Share |
|---|---|---:|---:|
| A | Direct generation | 18 | 39.1% |
| B | Static neuro-symbolic translation | 18 | 39.1% |
| C | Formal verification without autonomous feedback | 4 | 8.7% |
| D | Runtime plan adaptation and recovery | 6 | 13.0% |
| **Total** |  | **46** | **100.0%** |

Verification formality levels (per study, not per group): Level 1 (no formal verification) = 20 studies
(43.5%); Level 2 (lightweight symbolic consistency) = 19 (41.3%); Level 3 (formal verification against an
explicit model or specification) = 7 (15.2%).

## Boundary cases checked

- `Chalvatzaki2023` remains in **C**: GPT-2 produces PDDL subproblems solved by Fast Downward, but the paper does not provide autonomous execution-error recovery.
- `Patton2024` remains in **C**: the LLM-guided program-synthesis method includes unrealizability checking, but no autonomous robot execution-recovery loop.
- `kanazawaRealworldCookingRobot2024` is in **C** (adjudicated 2026-08-06): PDDL classical planning against an explicit formal model (17 typed actions with preconditions/effects) without autonomous recovery feedback; error-feedback replanning is future work. Consistent with Chalvatzaki2023.
- `gonzalez-santamartaUsingLargeLanguage2023` is in **C** (adjudicated): MERLIN2 performs formal PDDL planning; the LLM interprets failure logs post-hoc (offline), so there is no autonomous execution feedback. Inclusion under IC1 uses the extended scope (semantic interpretation of robot task state).
- `Capitanelli2024` is in **D**: SPEM uses PDDL/VAL precondition checks before execution and resets/replans when the current state is incompatible.
- `Zhang2023` is in **D**: the system continuously checks the current state and replans when it is inconsistent with expectations.
- `Wang2025Conformal` is in **D** under the operational definition used here: the LTL planner receives execution obstacles and issues alternative subtasks automatically. The limitation that human assistance may be needed for non-singleton uncertainty sets is recorded in the classification note.
- `driessPaLMEEmbodiedMultimodal2023` is in **D** (Level 1): prompted skill-failure detection (F1 0.91) and replan-on-failure inside the control loop, without formal symbolic verification.
- `tziafasOpenWorldGraspingLarge2024` is in **D** (Level 1): failed or blocked grasps autonomously trigger re-grounding and re-planning (Algorithm 1 loop; recovery ablation in Table 4), without formal symbolic verification.
- `wangCanTellWhat2024` (RONAR) is in **D** (Level 2, adjudicated): runtime failure states map to query-user/teleoperation states (state-machine behavior); the physical recovery is human-executed, so the system has autonomous escalation but not autonomous replanning. Runtime scene graph is lightweight symbolic structure, not a formal verifier.
- `laiNVPHRIZeroShot2025` is in **B** (adjudicated): the geometric cross-check/revision loop closes before physical execution; execution itself is open-loop (rule R4 of the A7b protocol).
- `liangIntrospectivePlanningAligning2024` is in **A** (adjudicated): uncertainty-triggered clarification is a pre-execution one-shot decision (offline benchmark evaluation), not runtime recovery.

## Matrix note

The taxonomy figure crosses Verification Formality Level (1/2/3) with autonomous feedback (absent/present).
Within the original search corpus the two non-formal feedback cells were empty and Group D occupied only the
formal-plus-feedback cell. The supplementary open-access retrieval round changed this: Group D now spans all
three feedback cells (Level 1: PaLM-E, open-world grasping; Level 2: RONAR; Level 3: the three earliest
studies). No cell is empty in the 46-study corpus. The research gap is the absence of a Group-D system
combining semantic failure diagnosis, formal-constraint updating, and autonomous replanning in dynamic,
unstructured environments.

Older reports describing Group C=4/Group D=1 or the 14/16/2/3 distribution are stale and must not be used
for tables or figures.
