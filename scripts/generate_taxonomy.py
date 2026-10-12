#!/usr/bin/env python3
"""Generate the two-dimensional taxonomy matrix from the canonical extraction."""
from __future__ import annotations

from pathlib import Path
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/extraction/study_extraction.csv"
OUT = ROOT / "results/figures"


def cell(ax, x0: float, y0: float, width: float, height: float, *,
         facecolor: str = "white", edgecolor: str = "#A0A0A0", linewidth: float = 0.9) -> None:
    ax.add_patch(patches.Rectangle(
        (x0, y0), width, height, facecolor=facecolor,
        edgecolor=edgecolor, linewidth=linewidth
    ))


def main() -> None:
    data = pd.read_csv(DATA).fillna("")
    if len(data) != 46:
        raise ValueError(f"expected 35 included studies, got {len(data)}")

    counts = data["taxonomy_group"].value_counts().to_dict()
    expected = {"A": 18, "B": 18, "C": 4, "D": 6}
    if {key: counts.get(key, 0) for key in expected} != expected:
        raise ValueError(f"unexpected taxonomy counts: {counts}")

    # Group D spans the three feedback cells (adjudication 2026-08-06):
    # no symbolic structure: PaLM-E, OWG; lightweight: RONAR; formal: Zhang, Capitanelli, Wang.
    d_cells = {(0, 1): 2, (1, 1): 1, (2, 1): 3}
    if sum(d_cells.values()) != counts["D"]:
        raise ValueError("Group D cell breakdown does not match total")

    fig, ax = plt.subplots(figsize=(13, 8.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.5, 0.965, "Taxonomy of Symbolic Structure and Autonomous Feedback",
             ha="center", va="center", fontsize=22, fontweight="bold")
    fig.text(0.5, 0.92,
             "Distribution of the 46 included studies across two independent dimensions",
             ha="center", va="center", fontsize=15, color="#666666")

    x = [0.03, 0.285, 0.63, 0.97]
    y_top, y_bottom = 0.84, 0.28
    header_h = 0.095
    row_h = (y_top - y_bottom - header_h) / 3

    for i in range(3):
        cell(ax, x[i], y_top - header_h, x[i + 1] - x[i], header_h)
    for row in range(3):
        y = y_top - header_h - (row + 1) * row_h
        cell(ax, x[0], y, x[1] - x[0], row_h)
        cell(ax, x[1], y, x[2] - x[1], row_h)
        cell(ax, x[2], y, x[3] - x[2], row_h)

    header_y = y_top - header_h / 2
    ax.text((x[0] + x[1]) / 2, header_y, "Symbolic structure",
            ha="center", va="center", fontsize=14, fontweight="bold")
    ax.text((x[1] + x[2]) / 2, header_y, "Without autonomous feedback",
            ha="center", va="center", fontsize=14, fontweight="bold")
    ax.text((x[2] + x[3]) / 2, header_y, "With autonomous feedback",
            ha="center", va="center", fontsize=14, fontweight="bold")

    row_labels = [
        "No symbolic structure",
        "Lightweight or static\nsymbolic structure",
        "Formal symbolic\nstructure",
    ]
    for row, label in enumerate(row_labels):
        y = y_top - header_h - (row + 0.5) * row_h
        ax.text((x[0] + x[1]) / 2, y, label, ha="center", va="center",
                fontsize=13, fontweight="bold", linespacing=1.2)

    colors = {"A": "#E6F2FD", "B": "#EAF7E5", "C": "#FDE5E5", "D": "#EEE9FA"}
    entries = {
        (0, 0): ("A", "Direct Generation"),
        (1, 0): ("B", "Static Neuro-Symbolic"),
        (2, 0): ("C", "Formal Verification"),
        (0, 1): ("D", "Runtime Recovery"),
        (1, 1): ("D", "Runtime Recovery"),
        (2, 1): ("D", "Runtime Plan Adaptation and Recovery"),
    }
    for row in range(3):
        for col in range(2):
            y = y_top - header_h - (row + 1) * row_h
            cx = (x[col + 1] + x[col + 2]) / 2
            cy = y + row_h / 2
            group, label = entries[(row, col)]
            n = d_cells[(row, col)] if col == 1 else counts[group]
            ax.add_patch(patches.Rectangle(
                (x[col + 1], y), x[col + 2] - x[col + 1], row_h,
                facecolor=colors[group], edgecolor="#A0A0A0", linewidth=0.9,
                alpha=0.85, zorder=2
            ))
            ax.text(cx, cy + 0.055, f"Group {group}", ha="center", va="center",
                    fontsize=15, fontweight="bold")
            ax.text(cx, cy, label, ha="center", va="center", fontsize=12.5)
            ax.text(cx, cy - 0.055,
                    f"{n} included studies ({n / len(data) * 100:.1f}%)",
                    ha="center", va="center", fontsize=12.5)

    gap_x, gap_y, gap_w, gap_h = 0.075, 0.06, 0.85, 0.135
    ax.add_patch(patches.FancyBboxPatch(
        (gap_x, gap_y), gap_w, gap_h,
        boxstyle="round,pad=0.012,rounding_size=0.012",
        facecolor="#FFFDF8", edgecolor="#999999", linewidth=1.0
    ))
    ax.text(gap_x + 0.03, gap_y + gap_h * 0.62, "Research gap:",
            ha="left", va="center", fontsize=13.5, fontweight="bold")
    gap = ("No included study demonstrates a complete closed-loop neuro-symbolic recovery "
           "cycle combining dynamic-world change, semantic diagnosis of physical failure, "
           "formal model updating, and autonomous replanning.")
    lines = textwrap.wrap(gap, width=92)
    ax.text(gap_x + 0.20, gap_y + gap_h * 0.62, "\n".join(lines),
            ha="left", va="center", fontsize=12.2, linespacing=1.35)

    OUT.mkdir(parents=True, exist_ok=True)
    for suffix in ("png", "pdf"):
        fig.savefig(OUT / f"taxonomy.{suffix}", dpi=300, bbox_inches="tight",
                    facecolor="white", edgecolor="none")
    plt.close(fig)
    print(f"Taxonomy matrix saved for {len(data)} studies: {dict(counts)}")


if __name__ == "__main__":
    main()
