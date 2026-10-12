#!/usr/bin/env python3
"""Fail-fast integrity checks for the public review data."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

def main() -> None:
    studies = read_csv(ROOT / "data/studies.csv")
    extraction = read_csv(ROOT / "data/extraction/study_extraction.csv")
    taxonomy = read_csv(ROOT / "data/extraction/taxonomy_membership.csv")
    all_records = read_csv(ROOT / "data/screening/all_records.csv")
    grouped = read_csv(ROOT / "data/screening/grouped_exclusions.csv")
    not_retrieved = read_csv(ROOT / "data/screening/not_retrieved.csv")

    assert len(all_records) == 147  # search archive unchanged
    assert Counter(row["screening_decision"] for row in all_records) == Counter({
        "include": 66,
        "exclude": 62,
        "exclude_grouped": 17,
        "uncertain (potential exclusion)": 2,
    })
    assert len(grouped) == 17
    assert all(row["group_id"] == "AdjunctProceedings*" for row in grouped)
    assert len(not_retrieved) == 11
    assert all(row["screening_decision"] == "include" for row in not_retrieved)
    assert all(row["retrieval_reason"] for row in not_retrieved)

    assert len(studies) == 55, f"expected 55 full-text records, got {len(studies)}"
    assert Counter(row["screening_status"] for row in studies) == Counter({"included": 46, "excluded_full_text": 9})
    assert len(extraction) == 46, f"expected 46 extracted studies, got {len(extraction)}"
    assert len(taxonomy) == 46
    assert len({row["study_id"] for row in studies}) == 55
    assert len({row["study_id"] for row in extraction}) == 46
    assert {row["study_id"] for row in extraction} <= {row["study_id"] for row in studies if row["screening_status"] == "included"}
    assert Counter(row["taxonomy_group"] for row in extraction) == Counter({"A": 18, "B": 18, "C": 4, "D": 6})
    # validation-method totals are regenerated from data (see results/tables/validation_methods.csv)
    assert all(row["uses_llm"] == "Yes" for row in extraction)
    assert all(row["doi"] for row in studies), "a final record has no DOI"

    forbidden = ("Yesulation", "Nao Especificado", "Nao se aplica", "Alucinacao", "Simulacao", "Hibrido")
    main_fields = [field for field in extraction[0] if not field.startswith("evidence_")]
    leftovers = [(row["study_id"], field, row[field]) for row in extraction for field in main_fields if any(token in row[field] for token in forbidden)]
    assert not leftovers, f"non-English labels remain: {leftovers[:3]}"

    missing_evidence = []
    for row in extraction:
        for field in main_fields:
            if field.startswith(("study_id", "title", "publication_", "authors", "classification_")):
                continue
            evidence = "evidence_" + field
            if row[field] and evidence in row and not row[evidence]:
                missing_evidence.append((row["study_id"], field))
    print(f"OK: {len(all_records)} bibliographic records; {len(grouped)} grouped exclusions; {len(not_retrieved)} not retrieved")
    print(f"OK: {len(studies)} full-text records, {len(extraction)} included studies")
    print(f"Groups: {dict(Counter(row['taxonomy_group'] for row in extraction))}")
    print(f"Validation: {dict(Counter(row['validation_method'] for row in extraction))}")
    if missing_evidence:
        print(f"WARNING: {len(missing_evidence)} populated fields lack evidence: {missing_evidence}")

if __name__ == "__main__":
    main()
