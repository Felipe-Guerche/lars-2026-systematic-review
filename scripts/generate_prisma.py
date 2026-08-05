from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/figures'
FLOW = {'identified': 183, 'duplicates': 35, 'screened': 148, 'screening_excluded': 82,
        'retrieval_sought': 66, 'not_retrieved': 28, 'assessed': 38,
        'full_text_excluded': 3, 'included': 35}
assert FLOW['identified'] - FLOW['duplicates'] == FLOW['screened']
assert FLOW['screened'] - FLOW['screening_excluded'] == FLOW['retrieval_sought']
assert FLOW['retrieval_sought'] - FLOW['not_retrieved'] == FLOW['assessed']
assert FLOW['assessed'] - FLOW['full_text_excluded'] == FLOW['included']

fig, ax = plt.subplots(figsize=(10, 15))
ax.set_xlim(0, 12)
ax.set_ylim(0, 16)
ax.set_aspect('equal')
ax.axis('off')

border_color = '#333333'
header_color = '#FFC107'
phase_color = '#5B9BD5'
box_w = 4.2
box_h = 1.0
excl_w = 3.8
excl_h = 0.95
excl_x = 9.5

def draw_box(cx, cy, w, h, text, bold=False, italic=False, fontsize=9):
    ax.add_patch(patches.FancyBboxPatch((cx - w/2, cy - h/2), w, h,
        boxstyle="round,pad=0.05", facecolor='white', edgecolor=border_color, linewidth=1.2))
    fw = 'bold' if bold else 'normal'
    fi = 'italic' if italic else 'normal'
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fontsize,
        fontweight=fw, fontstyle=fi)

def draw_excl(cx, cy, w, h, text_lines, bold_idx=None, fontsize=8):
    ax.add_patch(patches.Rectangle((cx - w/2, cy - h/2), w, h,
        facecolor='white', edgecolor=border_color, linewidth=1.2))
    n = len(text_lines)
    for i, line in enumerate(text_lines):
        y_off = (n/2 - 0.5 - i) * 0.28
        fw = 'bold' if (bold_idx is not None and i == bold_idx) else 'normal'
        ax.text(cx, cy + y_off, line, ha='center', va='center',
            fontsize=fontsize, fontweight=fw)

def arrow_down(x, y1, y2):
    ax.annotate('', xy=(x, y2), xytext=(x, y1),
        arrowprops=dict(arrowstyle='->', color=border_color, lw=1.5))

def arrow_right(x_tail, y, x_head):
    ax.annotate('', xy=(x_head, y), xytext=(x_tail, y),
        arrowprops=dict(arrowstyle='->', color=border_color, lw=1.5))
# === HEADER ===
ax.add_patch(patches.FancyBboxPatch((0.5, 13.3), 9, 0.7,
    boxstyle="round,pad=0.05", facecolor=header_color, edgecolor=border_color, linewidth=1.5))
ax.text(5, 13.65, 'Identification of studies via databases and registers',
    ha='center', va='center', fontsize=11, fontweight='bold')

# === PHASE LABELS ===
phase_data = [
    ('Identification', 12.8, 2.0),
    ('Screening', 10.2, 1.5),
    ('Retrieval', 7.6, 1.5),
    ('Eligibility', 5.0, 1.5),
    ('Included', 2.4, 1.5),
]
for label, cy, h in phase_data:
    ax.add_patch(patches.FancyBboxPatch((0.05, cy - h/2), 0.35, h,
        boxstyle="round,pad=0.02", facecolor=phase_color, edgecolor=border_color, linewidth=1))
    ax.text(0.225, cy, label, ha='center', va='center',
        fontsize=8, fontweight='bold', color='white', rotation=90)

# === IDENTIFICATION ===
draw_box(5.0, 12.8, box_w, box_h,
    f'Records identified from databases\nScopus 99 | IEEE Xplore 45 | ACM DL 39\n(n = {FLOW["identified"]})', fontsize=7.8)
draw_excl(excl_x, 12.8, excl_w, excl_h,
    ['Records removed before', 'screening:', 'Duplicate records removed', f'(n = {FLOW["duplicates"]})'],
    bold_idx=None, fontsize=7.5)
arrow_right(5.0 + box_w/2, 12.8, excl_x - excl_w/2)

# === SCREENING ===
draw_box(5.0, 10.2, box_w, box_h, f'Records screened\n(n = {FLOW["screened"]})')
draw_excl(excl_x, 10.2, excl_w, excl_h,
    ['Records excluded', f'(n = {FLOW["screening_excluded"]})'], fontsize=8)
arrow_right(5.0 + box_w/2, 10.2, excl_x - excl_w/2)

# === RETRIEVAL ===
draw_box(5.0, 7.6, box_w, box_h, f'Reports sought for retrieval\n(n = {FLOW["retrieval_sought"]})')
draw_excl(excl_x, 7.6, excl_w, excl_h,
    ['Reports not retrieved', f'(n = {FLOW["not_retrieved"]})', 'UFSCar access unavailable'], fontsize=7.5)
arrow_right(5.0 + box_w/2, 7.6, excl_x - excl_w/2)

# === ELIGIBILITY ===
draw_box(5.0, 5.0, box_w, box_h, f'Reports assessed for eligibility\n(n = {FLOW["assessed"]})')
draw_excl(excl_x, 5.0, excl_w, excl_h,
    [f'Reports excluded (n = {FLOW["full_text_excluded"]})', 'EC3: no safety/verification/', 'hallucination focus'],
    bold_idx=0, fontsize=7.5)
arrow_right(5.0 + box_w/2, 5.0, excl_x - excl_w/2)

# === INCLUDED ===
draw_box(5.0, 2.4, box_w, box_h, f'Studies included in review\n(n = {FLOW["included"]})', bold=True)

# === ARROWS DOWN ===
arrow_down(5.0, 12.8 - box_h/2, 10.2 + box_h/2)
arrow_down(5.0, 10.2 - box_h/2, 7.6 + box_h/2)
arrow_down(5.0, 7.6 - box_h/2, 5.0 + box_h/2)
arrow_down(5.0, 5.0 - box_h/2, 2.4 + box_h/2)

plt.tight_layout()
OUT.mkdir(parents=True, exist_ok=True)
for suffix in ('png', 'pdf'):
    fig.savefig(OUT / f'prisma.{suffix}', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print('PRISMA figure saved successfully.')
