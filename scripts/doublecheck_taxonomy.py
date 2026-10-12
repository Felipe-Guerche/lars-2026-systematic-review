#!/usr/bin/env python3
"""Audit the boundary cases of the A/B/C/D taxonomy."""
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((ROOT / "data/extraction/study_extraction.csv").open(encoding="utf-8-sig", newline="")))
formal = re.compile(r"pddl|ltl|formal verification|unrealizability|conformal", re.I)

expected = {"A": 18, "B": 18, "C": 4, "D": 6}
actual = Counter(row["taxonomy_group"] for row in rows)
assert actual == expected, f"unexpected group counts: {actual}"

candidates = []
for row in rows:
    text = " ".join(row[field] for field in ("symbolic_method_role", "mitigation_strategy", "mitigated_error"))
    if formal.search(text):
        candidates.append(row)

expected_formal = {"Chalvatzaki2023": "C", "Patton2024": "C", "Capitanelli2024": "D", "Wang2025Conformal": "D", "Zhang2023": "D",
                   "kanazawaRealworldCookingRobot2024": "C", "gonzalez-santamartaUsingLargeLanguage2023": "C",
                   "liangIntrospectivePlanningAligning2024": "A", "chenBackboneLongHorizonRobot2025": "B"}
actual_formal = {row["study_id"]: row["taxonomy_group"] for row in candidates}
assert actual_formal == expected_formal, f"formal boundary cases changed: {actual_formal}"

print("Taxonomy counts:", dict(actual))
print("Formal-method boundary cases:")
for study_id, group in expected_formal.items():
    print(f"  {study_id}: Group {group}")
print("Taxonomy double-check passed.")
