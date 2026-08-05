#!/usr/bin/env python3
"""Generate result tables and figures from the canonical English extraction.

Adapted from corpus/scripts/generate_figures_en.py. The original analysis logic
is retained, but paths are repository-relative and all counts are data-driven.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/extraction/study_extraction.csv"
TABLES = ROOT / "results/tables"
FIGURES = ROOT / "results/figures"
GROUP_ORDER = ["A", "B", "C", "D"]
GROUP_LABELS = {
    "A": "Group A — Direct generation",
    "B": "Group B — Static neuro-symbolic",
    "C": "Group C — Formal verification",
    "D": "Group D — Runtime plan adaptation and recovery",
}


def save_figure(fig: plt.Figure, name: str) -> None:
    for suffix in ("png", "pdf"):
        fig.savefig(FIGURES / f"{name}.{suffix}", dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def save_counts(name: str, counts: pd.Series, order: list[str] | None = None) -> pd.DataFrame:
    if order:
        counts = counts.reindex(order).fillna(0).astype(int)
    table = counts.rename("count").reset_index()
    table.columns = ["category", "count"]
    table["percentage"] = (table["count"] / len(df) * 100).round(1)
    table.to_csv(TABLES / f"{name}.csv", index=False)
    return table


def plot_taxonomy() -> None:
    counts = df["taxonomy_group"].value_counts().reindex(GROUP_ORDER).fillna(0)
    fig, ax = plt.subplots(figsize=(9, 5.5))
    bars = ax.bar([f"{g}\n(n={int(counts[g])})" for g in GROUP_ORDER], counts.values,
                  color=["#3498db", "#2ecc71", "#e67e22", "#9b59b6"])
    ax.set_ylabel("Number of studies")
    ax.set_title("Taxonomy of LLM–robot integration (n=35)")
    ax.set_ylim(0, max(counts) * 1.25)
    for bar, group in zip(bars, GROUP_ORDER):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.2,
                f"{counts[group] / len(df) * 100:.1f}%", ha="center", va="bottom")
    save_figure(fig, "taxonomy_groups")


def plot_interfaces() -> None:
    order = ["Text", "Voice", "Multimodal", "Other", "Unspecified"]
    counts = df["interface_modality"].value_counts().reindex(order).dropna()
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar(counts.index, counts.values, color="#3498db")
    ax.set_ylabel("Number of studies")
    ax.set_title("Interface modalities (RQ1)")
    ax.tick_params(axis="x", rotation=20)
    for i, value in enumerate(counts.values):
        ax.text(i, value + 0.2, f"{int(value)}\n({value / len(df) * 100:.1f}%)", ha="center")
    save_figure(fig, "interface_modalities")


def plot_families() -> None:
    families = Counter()
    for value in df["llm_family"].fillna(""):
        families.update(x.strip() for x in str(value).split(";") if x.strip())
    table = pd.DataFrame(sorted(families.items(), key=lambda x: (-x[1], x[0])), columns=["category", "count"])
    table["percentage"] = (table["count"] / len(df) * 100).round(1)
    table.to_csv(TABLES / "llm_families.csv", index=False)
    fig, ax = plt.subplots(figsize=(9, 5.5))
    view = table.head(10).sort_values("count")
    ax.barh(view["category"], view["count"], color="#3498db")
    ax.set_xlabel("Study mentions (multi-label)")
    ax.set_title("LLM families used (RQ2)")
    for i, value in enumerate(view["count"]): ax.text(value + 0.1, i, str(value), va="center")
    save_figure(fig, "llm_families")


def plot_validation() -> None:
    order = ["Simulation", "Real", "Hybrid", "Other"]
    counts = df["validation_method"].value_counts().reindex(order).dropna()
    save_counts("validation_methods", df["validation_method"].value_counts(), order)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar(counts.index, counts.values, color=["#9b59b6", "#e74c3c", "#2ecc71", "#95a5a6"])
    ax.set_ylabel("Number of studies")
    ax.set_title("Validation environments (RQ4)")
    for i, value in enumerate(counts.values): ax.text(i, value + 0.2, f"{int(value)}", ha="center")
    save_figure(fig, "validation_environments")


def plot_challenges() -> None:
    challenges = Counter()
    for value in df["main_challenges"].fillna(""):
        challenges.update(x.strip() for x in str(value).split(";") if x.strip() and x.strip() != "Not applicable")
    top = challenges.most_common(10)
    table = pd.DataFrame(top, columns=["category", "count"])
    table["percentage_of_studies"] = (table["count"] / len(df) * 100).round(1)
    table.to_csv(TABLES / "challenge_frequency_top10.csv", index=False)
    fig, ax = plt.subplots(figsize=(12, 6))
    labels = [x[0] for x in top]
    values = [x[1] for x in top]
    ax.bar(range(len(labels)), values, color="#e74c3c", alpha=0.8)
    ax.set_xticks(range(len(labels)), labels, rotation=45, ha="right")
    ax.set_ylabel("Number of studies")
    ax.set_title("Top technical challenges reported (RQ5)")
    for i, value in enumerate(values): ax.text(i, value + 0.2, str(value), ha="center")
    cumulative = [sum(values[:i + 1]) / sum(values) * 100 for i in range(len(values))]
    ax2 = ax.twinx()
    ax2.plot(range(len(labels)), cumulative, color="#2980b9", marker="o")
    ax2.set_ylabel("Cumulative percentage of top-10 mentions")
    ax2.set_ylim(0, 105)
    save_figure(fig, "challenges_pareto")


def plot_tradeoff() -> None:
    levels = {"A": 1, "B": 2, "C": 3, "D": 3}
    counts = df["taxonomy_group"].value_counts().reindex(GROUP_ORDER).fillna(0)
    table = pd.DataFrame({"group": GROUP_ORDER, "label": [GROUP_LABELS[g] for g in GROUP_ORDER],
                          "verification_formality_level": [levels[g] for g in GROUP_ORDER],
                          "count": counts.astype(int).values})
    table["percentage"] = (table["count"] / len(df) * 100).round(1)
    table.to_csv(TABLES / "expertise_safety_by_group.csv", index=False)
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.bar(GROUP_ORDER, table["verification_formality_level"], color=["#3498db", "#2ecc71", "#e67e22", "#9b59b6"])
    ax.set_xlabel("Taxonomy group")
    ax.set_ylabel("Verification formality level")
    ax.set_title("Verification formality level by taxonomy group")
    ax.set_ylim(0, 3.5)
    for i, row in table.iterrows(): ax.text(i, row["verification_formality_level"] + .08, f"n={row['count']}", ha="center")
    save_figure(fig, "expertise_safety")


def main() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    global df
    df = pd.read_csv(DATA).fillna("")
    if len(df) != 35: raise ValueError(f"expected 35 studies, got {len(df)}")

    save_counts("taxonomy_groups", df["taxonomy_group"].value_counts(), GROUP_ORDER)
    save_counts("interface_modalities", df["interface_modality"].value_counts(), ["Text", "Voice", "Multimodal", "Other", "Unspecified"])
    save_counts("publication_years", df["publication_year"].astype(str).value_counts().sort_index())
    cross = pd.crosstab(df["taxonomy_group"], df["validation_method"]).reindex(index=GROUP_ORDER, fill_value=0)
    cross.to_csv(TABLES / "taxonomy_by_validation.csv")
    plot_taxonomy(); plot_interfaces(); plot_families(); plot_validation(); plot_challenges(); plot_tradeoff()
    print(f"Generated {len(list(TABLES.glob('*.csv')))} tables and {len(list(FIGURES.glob('*.png')))} PNG/PDF figure pairs.")

if __name__ == "__main__":
    main()
