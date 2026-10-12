# Systematic Review Supplementary Material

This document contains the complete search strings referenced in the 6-page LARS 2026 manuscript `1-Systematic-Review.pdf`.

## Complete Search Strings

The systematic search was conducted across three databases (Scopus, IEEE Xplore, and ACM Digital Library) with three search strings per database, totaling nine search queries. The final search/update was completed on 3 November 2025, covering publications from January 2020 through 3 November 2025. November 2025 represents partial-year coverage. The query set combines broad LLM--robot and vision--language strings with mobile/hospital-specific strings; the final corpus is therefore interpreted under an embodied-robotics umbrella that includes mobile, mobile-manipulation, fixed-base, tabletop, humanoid, and embodied-simulation platforms.

### Scopus

**String 1:**
```
TITLE-ABS-KEY(("large language model" OR LLM) W/5 robot*) OR TITLE-ABS-KEY(("large language model" OR LLM) W/5 "autonomous agent") AND TITLE-ABS(pddl OR "formal verification" OR grounding OR hallucination OR "neuro-symbolic")
```

**String 2:**
```
TITLE-ABS((("vision" OR "visual") AND ("language" OR "linguistic")) AND (("Large Language Model" OR "LLM") W/8 ("robot*" OR "action")) AND ("Hallucination" OR "alignment" OR "Grounding"))
```

**String 3:**
```
("Mobile Robot" OR "Autonomous Robot") AND ("Hospital Logistics" OR "Healthcare Environment" OR "Critical Domain") AND ("ROS 2" OR Gazebo)
```

### IEEE Xplore

**String 1:**
```
((("All Metadata":"large language model" OR "All Metadata":LLM) NEAR/5 "All Metadata":robot*) OR (("All Metadata":"large language model" OR "All Metadata":LLM) NEAR/5 "All Metadata":"autonomous agent")) AND ("Document Title":pddl OR "Document Title":"formal verification" OR "Document Title":grounding OR "Document Title":hallucination OR "Document Title":"neuro-symbolic" OR "Abstract":pddl OR "Abstract":"formal verification" OR "Abstract":grounding OR "Abstract":hallucination OR "Abstract":"neuro-symbolic")
```

**String 2:**
```
("All Metadata":vision OR "All Metadata":visual) AND ("All Metadata":language OR "All Metadata":linguistic) AND (("All Metadata":"Large Language Model" OR "All Metadata":LLM) NEAR/8 ("All Metadata":robot* OR "All Metadata":action)) AND ("All Metadata":Hallucination OR "All Metadata":alignment OR "All Metadata":Grounding)
```

**String 3:**
```
((("All Metadata":robot* OR "All Metadata":autonomous) NEAR/5 "All Metadata":mobile) AND (("All Metadata":hospital* OR "All Metadata":clinical) NEAR/5 ("All Metadata":logistics OR "All Metadata":health*)) AND ("All Metadata":ROS* OR "All Metadata":Gazebo))
```

### ACM Digital Library

**String 1:**
```
Full-Text:((("large language model" OR LLM) AND robot*) OR (("large language model" OR LLM) NEAR/5 "autonomous agent")) AND (Title:(pddl OR "formal verification" OR grounding OR hallucination OR "neuro-symbolic") OR Abstract:(pddl OR "formal verification" OR grounding OR hallucination OR "neuro-symbolic"))
```

**String 2:**
```
Abstract:(("vision" OR "visual") AND ("language" OR "linguistic")) AND (("Large Language Model" OR "LLM") AND (robot* OR "action")) AND ("Hallucination" OR "alignment" OR "Grounding")
```

**String 3:**
```
Anywhere:("Mobile Robot" OR "Autonomous Robot") AND ("Hospital Logistics" OR "Healthcare Environment" OR "Critical Domain") AND ("ROS 2" OR Gazebo)
```

## Search Execution Details

- **Databases searched:** Scopus, IEEE Xplore, ACM Digital Library
- **Total search strings:** 9 (3 per database)
- **Publication window:** January 2020--3 November 2025 (partial coverage of November)
- **Final search/update date:** 3 November 2025
- **Screening protocol:** Screening, full-text assessment, study-level extraction, and taxonomy coding were performed by the first author. No auditable independent second-reviewer decision series was retained; therefore, no inter-rater agreement statistic is reported. Backward snowballing was used only to audit counter-examples

### Per-Database Yield Breakdown

| Database | Records |
|----------|---------|
| Scopus | 99 |
| IEEE Xplore | 45 |
| ACM Digital Library | 39 |
| **Combined (pre-dedup)** | **183** |

**Original screening flow before supplementary retrieval** (historical; the flow cited in the article):

| Step | Records |
|------|---------|
| Duplicate records removed | 35 |
| Records screened by title/abstract | 148 |
| Records excluded at title/abstract screening | 82 |
| Full-text reports sought | 66 |
| Reports not retrieved | 28 |
| Reports assessed for eligibility | 38 |
| Full-text reports excluded | 3 |
| **Studies included** | **35** |

**Final flow after the supplementary open-access retrieval round** (the counts used throughout the article):

| Step | Reports |
|------|---------|
| Full-text reports sought | 66 |
| Reports not retrieved | 11 |
| Reports assessed for eligibility | 55 |
| Full-text reports excluded | 9 |
| **Studies included** | **46** |

The 148 screening units comprise the 147 bibliographic records in the working archive plus the original aggregate `AdjunctProceedings*` row. The 82 excluded units comprise 65 non-included screening rows (63 explicit exclusions and 2 uncertain rows) and the 17 proceedings/companion-volume records covered by the grouped decision in `data/screening/grouped_exclusions.csv`; these administrative records are not additional primary studies. The grouped proceedings decision is separate from the EC1--EC3 full-text eligibility criteria.

In the original review, 28 reports could not be obtained because the first author's UFSCar institutional login did not provide access to the publisher PDFs. After the supplementary round, **11 reports remain not retrieved** (10 with no open-access version found and 1 bot-blocked); the record-level list is in `data/screening/not_retrieved.csv` (11 rows), and the round's per-report coding is in `data/screening/oa_retrieval_coding.csv`. Protected publisher files were not redistributed.

**Retrieval bias:** The observed absence of a complete closed-loop neuro-symbolic recovery architecture should be interpreted as a finding within the retrieved and assessed corpus, rather than as evidence of absence across the entire literature.

**Temporal coverage:** The search was last updated on 3 November 2025. Studies published or indexed after this date fall outside the scope of this review.

### Supplementary open-access retrieval round (August 2026)

The original retrieval (via the first author's UFSCar institutional login) left 28 reports unobtained. A
supplementary round searched open-access sources (arXiv, publisher open access, institutional repositories;
verified against Semantic Scholar and OpenAlex) and identified 18 candidates with open-access versions.
Seventeen full texts were retrieved and assessed under the same eligibility criteria (11 included, 6
excluded: five EC3, one EC1); one (liuSPECTRA, ACM bronze OA behind bot protection) remained unobtainable
and is counted as not retrieved, not as an exclusion. Final counts: 55 assessed, 46 included, 9 excluded,
11 not retrieved. Per-report coding (five dimensions with textual evidence and page references;
anti-exclusion rules) is in `data/screening/oa_retrieval_coding.csv`. This round is distinct from the
bibliographic search (ended 3 November 2025) and does not extend its coverage window. Where only a preprint
was readable (e.g., the PEAP-LLM study, published in 2026 from a 2025 preprint within the search window),
the version read is recorded per report in the coding file.

### Query-level yields

| Database | String 1 | String 2 | String 3 | Total |
|----------|----------:|----------:|----------:|------:|
| Scopus | 39 | 33 | 27 | 99 |
| IEEE Xplore | 18 | 21 | 6 | 45 |
| ACM Digital Library | 18 | 4 | 17 | 39 |

### Excluded Full-Text Papers (9 papers)

Original review (EC3):
1. **Smith et al. (2025)** — *Humanoid Robotics Powered by Vision-Based LLM Zero Shot Interactions.* Focuses on code generation from vision but does not address validation, safety, or hallucination mitigation of the resulting behavior.
2. **Vitharana et al. (2025)** — *A Walk to Remember: MLLM Memory-Driven Visual Navigation.* Focuses on navigation efficiency using memory but does not discuss safety mechanisms or hallucination mitigation.
3. **Wang et al. (2025)** — *'Hi AirStar, Guide Me to the Badminton Court.'* Describes a UAV platform with LLM but does not discuss reliability, safety, or validation challenges.

Supplementary open-access retrieval round (August 2026):
4. **Huang et al. (2025)** — *IVLMap* (EC3): map denoising only; maps explicitly static at runtime.
5. **Kwon et al. (2024)** — *Grounded commonsense reasoning for robot tidying* (EC3): active perception for missing visual information; skills executed open-loop.
6. **Mavrogiannis et al. (2025)** — *Discovering object attributes with LLMs* (EC3): error recovery explicitly future work.
7. **Song et al. (2025)** — *Learning 6-DoF fine-grained grasping with language* (EC3): LLM as semantic interface; robustness tests are not hallucination mitigation.
8. **Wang et al. (2024)** — *Polaris* (EC3): no mitigation/verification/recovery mechanism; human confirmation is interaction design.
9. **Zhong et al. (2024)** — *Policy improvement using language feedback models* (EC1): no embodied robot system or robot-task simulation (language-grounding benchmarks).

### Snowballing

Five additional studies were identified through backward snowballing from the reference lists of the 35 included papers and audited as counter-examples (Section 3.5 of the main paper): Inner Monologue~\cite{huangInnerMonologue2022}, SayCan~\cite{ahnSayCan2022}, Code-as-Policies~\cite{liangCodeAsPolicies2023}, LLM+P~\cite{liuLLMP2023}, and Reflexion~\cite{shinnReflexion2023}. In every case, at least one of the taxonomy dimensions or the dynamic-environment requirements was unsatisfied.

These five studies were not captured by the systematic search because they were published on arXiv (not indexed in Scopus, IEEE Xplore, or ACM DL at the time of search). All five were cited by at least one of the included studies. None of the included studies came from snowballing; all were captured by the systematic search or the supplementary open-access retrieval round. Note: Inner Monologue demonstrates autonomous runtime recovery on real robots without formal verification — outside the corpus it would occupy the feedback-without-formal-verification cell; the supplementary retrieval round later found in-corpus instances of this configuration (PaLM-E, open-world grasping).

## Additional Figures and Tables (space budget)

PRISMA 2020 flow diagram of the study selection process: `results/figures/prisma.png`
(66 sought -> 55 assessed / 11 not retrieved -> 46 included, 9 excluded).

The following items were moved out of the main paper to respect the page limit; the corresponding counts
remain in the main text. Figures from the release v1.0.13 generation scripts:
- `results/figures/interface_modalities.png` — interface-modality distribution (RQ1)
- `results/figures/llm_families.png` — LLM-family ranking (RQ2)
- `results/figures/expertise_safety.png` — verification formality levels (RQ3): Level 1 = 20 studies (43.5%), Level 2 = 19 (41.3%), Level 3 = 7 (15.2%)
- `results/figures/validation_environments.png` — validation environments (RQ4)
- `results/figures/challenges_pareto.png` — Pareto diagram of reported technical challenges (RQ5)

Counter-example audit table (Section 3.5 of the main paper):

| System | Failed criterion |
|---|---|
| Inner Monologue (Huang et al., 2022) | No formal verification (autonomous recovery present) |
| SayCan (Ahn et al., 2022) | No formal verification; no runtime recovery |
| Code-as-Policies (Liang et al., 2023) | No formal verification; no failure-driven replanning |
| LLM+P (Liu et al., 2023) | No autonomous feedback (one-shot translation) |
| Reflexion (Shinn et al., 2023) | No formal verification; non-robotic benchmarks |

Traceability from corpus evidence to candidate requirements (Section V of the main paper):

| Barrier | Corpus evidence | Requirement |
|---|---|---|
| No failure semantics | Errors stay at the motor layer (Groups A/B) | R1 |
| Open-loop execution | 18/46 (Group B) have no autonomous runtime recovery | R2 |
| Latency and hallucination | 0.3--3 s per call; 25/46 report hallucination | R3 |
| No graceful degradation | Only 6/46 adapt at runtime | R4 |

## Data availability

The versioned [release v1.0.13](https://github.com/Felipe-Guerche/lars-2026-systematic-review/releases/tag/v1.0.13) contains the nine complete search strings, database yields, sanitized metadata and DOIs for the 55 full-text records, `grouped_exclusions.csv`, `not_retrieved.csv`, `oa_retrieval_coding.csv`, full-text decisions, English extraction table (46 studies), taxonomy audit, result tables, figure-generation scripts, and the sanitized Zotero-compatible BibTeX export. This supplement is included in the release as `docs/SR_supplement.md`. Repository development and maintenance are credited to Felipe Delduque Guerche (`Felipe-Guerche`). Publisher PDFs, local Zotero attachments, and the private Zotero database are not redistributed.

## Complete List of 46 Primary Studies

The following table lists all 46 primary studies grouped by taxonomy category. Each entry is cited at least once in the main paper or this supplement.

### Group A: Direct Generation (18 studies)
\cite{fangEnhancedHumanRobotInteraction2025}, \cite{gaoPhysicallyGroundedVisionLanguage2024}, \cite{garciaGeneralizableVisionLanguageRobotic2025}, \cite{gebelliPersonalisedExplainableRobots2025}, \cite{htetHeyMiroMultimodal2025}, \cite{irfanRealityDelusionChallenges2025}, \cite{laiVisionLanguageModelbasedPhysical2024}, \cite{liangIntrospectivePlanningAligning2024}, \cite{liuLLMPoweredEmbodiedIntelligence2025}, \cite{luanEnhancingRobotTask2024}, \cite{moncada-ramirezAgenticWorkflowsImproving2025}, \cite{mohammadiParameterefficientActionPlanning2026}, \cite{ranasingheLargeLanguageModels2025}, \cite{wangAffordStructWeaklySupervised2025}, \cite{xuDriveGPT4InterpretableEndtoEnd2024}, \cite{xuExploringGroundingAbilities2025}, \cite{zhangFlexVLNFlexibleAdaptation2025}, \cite{zhangMambaSlipNovelMultimodal2025}

### Group B: Static Neuro-Symbolic Translation (18 studies)
\cite{abboValuesSocialRobots2025}, \cite{aliRobotsCanMultitask2024}, \cite{allgeuerWhenRobotsGet2024}, \cite{chenBackboneLongHorizonRobot2025}, \cite{dingSCRAGCoTOptimizationMethod2025}, \cite{dorbalaCanEmbodiedAgent2024}, \cite{laiNaturalMultimodalFusionBased2025}, \cite{laiNVPHRIZeroShot2025}, \cite{liAlleviatingActionHallucination2024}, \cite{liDemandGroundedPlan2025}, \cite{merloHumaninTheLoopApproachRobot2025}, \cite{nakajimaCombiningOntologicalKnowledge2024}, \cite{nambiarDigitalTwinEnabledAdaptive2025}, \cite{pinto-bernalDesigningSocialRobots2025}, \cite{wangAintMisbehavinUsing2024}, \cite{wangLLMbasedRobotTask2024}, \cite{yamazakiBuildingHospitableReliable2023}, \cite{yangOceanPlanHierarchicalPlanning2025}

### Group C: Formal Verification Without Autonomous Feedback (4 studies)
\cite{chalvatzakiLearningReasonScene2023}, \cite{gonzalez-santamartaUsingLargeLanguage2023}, \cite{kanazawaRealworldCookingRobot2024}, \cite{pattonProgrammingbyDemonstrationLongHorizonRobot2024}

### Group D: Runtime Plan Adaptation and Recovery (6 studies)
\cite{capitanelliFrameworkNeurosymbolicRobot2024}, \cite{driessPaLMEEmbodiedMultimodal2023}, \cite{tziafasOpenWorldGraspingLarge2024}, \cite{wangCanTellWhat2024}, \cite{wangConformalTemporalLogic2025}, \cite{zhangBoostingRobotIntelligence2023}

Group D spans all three verification-formality levels: Zhang (2023), Capitanelli (2024), and Wang (2025) combine formal verification with autonomous execution feedback; RONAR combines runtime recovery with a lightweight runtime scene graph; PaLM-E and open-world grasping recover without formal symbolic structure. Closed-loop recovery without formal verification is therefore no longer an empty cell.

## Group D Studies vs. Criteria for Dynamic, Unstructured Environments

The following table compares each Group D study against the three criteria for dynamic, unstructured environments defined in Section V of the main paper. Group D includes systems in which runtime state changes, unmet preconditions, planning uncertainty, or updated environmental information can trigger plan revision, replanning, or escalation. Capitanelli and Mastrogiovanni monitor post-action state and next-action preconditions; Wang et al. address high-level planning uncertainty and infeasible subtasks while assuming error-free execution of low-level robot skills; PaLM-E detects skill failures through prompted visual judgment and replans in the control loop; open-world grasping re-runs grounding and grasp planning after failed or blocked grasps; RONAR maps runtime failure states to autonomous escalation, with recovery executed by a human operator.

| Study | C1: Unpredictable Obstacles | C2: State Changes Without Warning | C3: No Prior Map |
|-------|----------------------------|-----------------------------------|------------------|
| Zhang et al. (2023) | ✗ | ✓ | ✗ |
| Capitanelli et al. (2024) | ✗ | ✓ | ✗ |
| Wang et al. (2025) | ✗ | ✓ | ✓ |
| PaLM-E (2023) | n.d. | ✓ | ✓ |
| Tziafas \& Kasaei (2024) | ✓ | n.d. | ✓ |
| Wang et al. (2024, RONAR) | ✓ | ✓ | n.d. |

**C1:** Unpredictable obstacles that appear during execution (e.g., hospital stretchers, equipment left in corridors).
**C2:** State changes that invalidate the initial world model without warning (e.g., doors locked, rooms repurposed).
**C3:** No complete prior map or object inventory available to the planner. (n.d. = not determined from the text.)

Within the assessed Group D studies, none satisfies all three criteria simultaneously, and none combines semantic failure diagnosis, formal-constraint updating, and autonomous replanning: RONAR has diagnosis and runtime model updates but human-executed recovery; PaLM-E has diagnosis and autonomous replanning but no formal-constraint updating; open-world grasping has autonomous replanning without semantic failure diagnosis. This confirms the bounded structural gap identified in this review.
