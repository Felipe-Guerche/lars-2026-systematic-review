from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = pd.read_csv(ROOT / 'data/extraction/study_extraction.csv')
COUNTS = DATA['taxonomy_group'].value_counts()
TOTAL = len(DATA)

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(-9, 10)
ax.set_ylim(-9, 2)
ax.axis('off')

# Colors
root_color = '#E8E8E8'
q_color = '#F0F0F0'
A_color = '#D6EAF8'  # blue
B_color = '#D5F5E3'  # green
C_color = '#FADBD8'  # red/salmon
D_color = '#E8DAEF'  # purple (gap)
border_color = '#333333'
arrow_color = '#444444'

def rounded_box(ax, x, y, w, h, text, facecolor, edgecolor=border_color, lw=1.2,
                fontsize=9, bold=False, dashed=False, text_color='black'):
    linestyle = '--' if dashed else '-'
    box = patches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=facecolor, edgecolor=edgecolor,
                         linewidth=lw if not dashed else 2.0, linestyle=linestyle,
                         zorder=2)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontweight=weight, color=text_color, zorder=3)
    return box

def draw_arrow(ax, x1, y1, x2, y2, label=None, label_pos=0.35, label_offset=(0, 0.3)):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=arrow_color, lw=1.3,
                               connectionstyle="arc3,rad=0"),
                zorder=1)
    if label:
        mx = x1 + (x2 - x1) * label_pos + label_offset[0]
        my = y1 + (y2 - y1) * label_pos + label_offset[1]
        ax.text(mx, my, label, ha='center', va='center', fontsize=12,
                bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                         edgecolor='none', alpha=0.9), zorder=4)

# === LAYOUT ===
# Level 0: Root
q1_x, q1_y = 0, 0

# Level 1
gA_x, gA_y = -5.5, -2.5
q2_x, q2_y = 3, -2.5

# Level 2
q3_x, q3_y = 0, -5
gD_x, gD_y = 6, -5

# Level 3: Leaves
gB_x, gB_y = -2.5, -7.5
gC_x, gC_y = 2.5, -7.5

# Box sizes
root_w, root_h = 4.5, 1.1
q_w, q_h = 4.2, 1.0
leaf_w, leaf_h = 4.0, 1.3

# === DRAW NODES ===
# Level 0: Root question
rounded_box(ax, q1_x, q1_y, root_w, root_h,
            'Symbolic verification\nmethod?', root_color, fontsize=14, bold=True)

# Level 1
rounded_box(ax, gA_x, gA_y, leaf_w, leaf_h,
            f'Group A: Direct Generation\n(End-to-End) — {int(COUNTS["A"])} ({COUNTS["A"] / TOTAL * 100:.1f}%)',
            A_color, fontsize=12)
rounded_box(ax, q2_x, q2_y, q_w, q_h,
            'Autonomous feedback\nloop?', q_color, fontsize=13, bold=True)

# Level 2
rounded_box(ax, q3_x, q3_y, q_w, q_h,
            'Formal verification\n(PDDL, LTL, HTN)?', q_color, fontsize=13, bold=True)
rounded_box(ax, gD_x, gD_y, leaf_w, leaf_h,
            f'Group D: Closed-Loop Recovery\n(Research Gap) — {int(COUNTS["D"])} ({COUNTS["D"] / TOTAL * 100:.1f}%)',
            D_color, fontsize=12, bold=True, dashed=True)

# Level 3: Leaves
rounded_box(ax, gB_x, gB_y, leaf_w, leaf_h,
            f'Group B: Static Neuro-Symbolic\n(Lightweight) — {int(COUNTS["B"])} ({COUNTS["B"] / TOTAL * 100:.1f}%)',
            B_color, fontsize=12)
rounded_box(ax, gC_x, gC_y, leaf_w, leaf_h,
            f'Group C: Formal Verification\n(PDDL/LTL, no feedback) — {int(COUNTS["C"])} ({COUNTS["C"] / TOTAL * 100:.1f}%)',
            C_color, fontsize=12)

# === DRAW ARROWS ===
# Root -> Level 1
draw_arrow(ax, q1_x - 1.0, q1_y - root_h/2, gA_x, gA_y + leaf_h/2, 'No', label_pos=0.35, label_offset=(-0.3, 0.3))
draw_arrow(ax, q1_x + 1.0, q1_y - root_h/2, q2_x, q2_y + q_h/2, 'Yes', label_pos=0.35, label_offset=(0.3, 0.3))

# q2 -> Level 2
draw_arrow(ax, q2_x - 1.0, q2_y - q_h/2, q3_x, q3_y + q_h/2, 'No', label_pos=0.35, label_offset=(-0.3, 0.3))
draw_arrow(ax, q2_x + 1.0, q2_y - q_h/2, gD_x, gD_y + leaf_h/2, 'Yes', label_pos=0.35, label_offset=(0.3, 0.3))

# q3 -> Level 3: Leaves
draw_arrow(ax, q3_x - 1.0, q3_y - q_h/2, gB_x, gB_y + leaf_h/2, 'No', label_pos=0.35, label_offset=(-0.3, 0.3))
draw_arrow(ax, q3_x + 1.0, q3_y - q_h/2, gC_x, gC_y + leaf_h/2, 'Yes', label_pos=0.35, label_offset=(0.3, 0.3))

# === NOTE ===
note_text = ('Decision path: (1) symbolic verification presence, '
             '(2) autonomous feedback loop, '
             '(3) formal vs lightweight symbolic methods.')
ax.text(0, -8.8, note_text, ha='center', va='top', fontsize=10, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF9E7', edgecolor='#D4AC0D', alpha=0.7))

plt.tight_layout()
out = ROOT / 'results/figures'
out.mkdir(parents=True, exist_ok=True)
for suffix in ('png', 'pdf'):
    fig.savefig(out / f'taxonomy_tree.{suffix}', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print('Taxonomy tree figure saved successfully.')
