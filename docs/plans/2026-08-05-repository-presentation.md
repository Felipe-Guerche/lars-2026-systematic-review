# Repository Presentation Implementation Plan

> **REQUIRED SUB-SKILL:** Use the executing-plans skill to implement this plan task-by-task.

**Goal:** Make the local reproducibility repository ready for a later GitHub push without changing its data or analysis.

**Architecture:** Improve discoverability in the root README using links and existing generated figures; remove the empty test directory and ignored build artifacts. Create a local version tag for the verified package; do not push it.

**Tech Stack:** Markdown, existing PNG/PDF figures, Git, Python validation scripts.

---

### Task 1: Improve the root README

**Files:**
- Modify: `README.md`

Add quick navigation, clickable links to the data/docs/scripts, the complete reproduction command, and three existing explanatory figures: PRISMA, taxonomy distribution, and challenge frequencies. Link the remaining generated figures through `results/README.md` rather than duplicating all previews.

### Task 2: Remove empty/generated local artifacts

**Files:**
- Delete: empty `tests/` directory locally
- Delete: ignored `scripts/__pycache__/` locally

Do not add a test framework; `scripts/validate_data.py` and `scripts/doublecheck_taxonomy.py` remain the lightweight checks.

### Task 3: Verify and version locally

Run the validation scripts, check Markdown links and repository status, commit only the README/plan changes, and create annotated local tag `v1.0.0`. The remote remains unchanged until the user authorizes the push.
