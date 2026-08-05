from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/figures'
FLOW = {'identified': 183, 'duplicates': 35, 'screened': 148, 'screening_excluded': 82,
        'screening_nonincluded_rows': 65, 'grouped_proceedings': 17,
        'retrieval_sought': 66, 'not_retrieved': 28, 'assessed': 38,
        'full_text_excluded': 3, 'included': 35}
assert FLOW['identified'] - FLOW['duplicates'] == FLOW['screened']
assert FLOW['screened'] - FLOW['screening_excluded'] == FLOW['retrieval_sought']
assert FLOW['screening_nonincluded_rows'] + FLOW['grouped_proceedings'] == FLOW['screening_excluded']
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
box_h = 1.05
excl_w = 3.8
excl_h = 1.15
layout_shift = -0.30
flow_x = 5.0 + layout_shift
excl_x = 9.5 + layout_shift
header_x, header_y, header_w, header_h = 0.5 + layout_shift, 14.2, 9.0, 0.7
phase_gap = 0.08
id_y, screening_y, retrieval_y, eligibility_y, included_y = 12.6, 10.1, 7.6, 5.1, 2.6
main_centers = (id_y, screening_y, retrieval_y, eligibility_y, included_y)
assert header_y - header_h / 2 > id_y + box_h / 2, 'header overlaps identification box'
assert all(upper - box_h / 2 > lower + box_h / 2 for upper, lower in zip(main_centers, main_centers[1:])), 'main boxes overlap'
assert excl_x - excl_w / 2 > flow_x + box_w / 2, 'side boxes overlap main boxes'

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
    if y1 <= y2:
        raise ValueError('downward arrow endpoints must be ordered from top to bottom')
    ax.annotate('', xy=(x, y2), xytext=(x, y1),
        arrowprops=dict(arrowstyle='->', color=border_color, lw=1.5))

def arrow_right(x_tail, y, x_head):
    if x_tail >= x_head:
        raise ValueError('rightward arrow endpoints must be ordered left to right')
    ax.annotate('', xy=(x_head, y), xytext=(x_tail, y),
        arrowprops=dict(arrowstyle='->', color=border_color, lw=1.5))
# === HEADER ===
ax.add_patch(patches.FancyBboxPatch((header_x, header_y - header_h / 2), header_w, header_h,
    boxstyle="round,pad=0.05", facecolor=header_color, edgecolor=border_color, linewidth=1.5))
ax.text(header_x + header_w / 2, header_y, 'Identification of studies via databases',
    ha='center', va='center', fontsize=11, fontweight='bold')

# === PHASE LABELS ===
phase_data = [
    ('Identification', id_y, 1.8),
    ('Screening', screening_y, 1.5),
    ('Retrieval', retrieval_y, 1.5),
    ('Eligibility', eligibility_y, 1.5),
    ('Included', included_y, 1.5),
]
for label, cy, h in phase_data:
    ax.add_patch(patches.FancyBboxPatch((0.05, cy - h/2), 0.35, h,
        boxstyle="round,pad=0.02", facecolor=phase_color, edgecolor=border_color, linewidth=1))
    ax.text(0.225, cy, label, ha='center', va='center',
        fontsize=8, fontweight='bold', color='white', rotation=90)

# === IDENTIFICATION ===
draw_box(flow_x, id_y, box_w, box_h,
    f'Records identified from databases\nScopus 99 | IEEE Xplore 45 | ACM DL 39\n(n = {FLOW["identified"]})', fontsize=7.8)
draw_excl(excl_x, id_y, excl_w, excl_h,
    ['Records removed before', 'screening:', 'Duplicate records removed', f'(n = {FLOW["duplicates"]})'],
    bold_idx=None, fontsize=7.5)
arrow_right(flow_x + box_w/2 + phase_gap, id_y, excl_x - excl_w/2 - phase_gap)

# === SCREENING ===
draw_box(flow_x, screening_y, box_w, box_h,
    f'Records screened\n(n = {FLOW["screened"]})\n147 records + 1 aggregate row', fontsize=7.5)
draw_excl(excl_x, screening_y, excl_w, excl_h,
    ['Records excluded', f'(n = {FLOW["screening_excluded"]})',
     f'{FLOW["screening_nonincluded_rows"]} screening rows + {FLOW["grouped_proceedings"]} grouped records'], fontsize=7.2)
arrow_right(flow_x + box_w/2 + phase_gap, screening_y, excl_x - excl_w/2 - phase_gap)

# === RETRIEVAL ===
draw_box(flow_x, retrieval_y, box_w, box_h, f'Reports sought for retrieval\n(n = {FLOW["retrieval_sought"]})')
draw_excl(excl_x, retrieval_y, excl_w, excl_h,
    ['Reports not retrieved', f'(n = {FLOW["not_retrieved"]})', 'UFSCar access unavailable'], fontsize=7.5)
arrow_right(flow_x + box_w/2 + phase_gap, retrieval_y, excl_x - excl_w/2 - phase_gap)

# === ELIGIBILITY ===
draw_box(flow_x, eligibility_y, box_w, box_h, f'Reports assessed for eligibility\n(n = {FLOW["assessed"]})')
draw_excl(excl_x, eligibility_y, excl_w, excl_h,
    [f'Reports excluded with reasons (n = {FLOW["full_text_excluded"]})',
     'EC3: no safety/verification/', 'hallucination focus'],
    bold_idx=0, fontsize=7.2)
arrow_right(flow_x + box_w/2 + phase_gap, eligibility_y, excl_x - excl_w/2 - phase_gap)

# === INCLUDED ===
draw_box(flow_x, included_y, box_w, box_h, f'Studies included in review\n(n = {FLOW["included"]})', bold=True)

# === ARROWS DOWN ===
# Endpoints stop short of both boxes so no arrowhead touches a border.
arrow_down(flow_x, id_y - box_h/2 - phase_gap, screening_y + box_h/2 + phase_gap)
arrow_down(flow_x, screening_y - box_h/2 - phase_gap, retrieval_y + box_h/2 + phase_gap)
arrow_down(flow_x, retrieval_y - box_h/2 - phase_gap, eligibility_y + box_h/2 + phase_gap)
arrow_down(flow_x, eligibility_y - box_h/2 - phase_gap, included_y + box_h/2 + phase_gap)

plt.tight_layout()
OUT.mkdir(parents=True, exist_ok=True)
for suffix in ('png', 'pdf'):
    fig.savefig(OUT / f'prisma.{suffix}', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print('PRISMA figure saved successfully.')
