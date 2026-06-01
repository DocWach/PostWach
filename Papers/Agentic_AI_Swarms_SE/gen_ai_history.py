"""Generate AI History Overview figure with black connector lines."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(20, 9))
ax.set_xlim(0, 20)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('none')
ax.patch.set_facecolor('none')

# Evenly spaced columns: 6 columns, col_w=2.4, gap=0.5 between boxes
col_w = 2.4
col_spacing = col_w + 0.5  # 2.9 center-to-center
cols = [2.2 + i * col_spacing for i in range(6)]
# cols = [2.2, 5.1, 8.0, 10.9, 13.8, 16.7]

# Colors for each era
era_colors = ['#2166AC', '#2A6E37', '#6B3A1F', '#1A6E5C', '#3B0F6F', '#6B1A8E']
cap_colors = ['#2166AC', '#2A6E37', '#7B4A20', '#1A6E5C', '#3B0F6F', '#8B1AAE']

# Labels
headers = ['Expert Systems', 'Machine Learning', 'Deep Learning',
           'Large Language Models', 'Agentic AI', 'Agentic Swarms']
dates = ['1970s-1980s', '1990s-2010s', '2012-2020',
         '2018-2023', '2023-2024', '2024-Present']

capabilities = [
    ['Rule-based "if-then"\nlogic', 'Human-encoded\nknowledge', 'MYCIN, XCON', 'Brittle, narrow, no\nlearning'],
    ['Learning patterns from\ndata', 'Statistical methods,\nneural nets', 'Feature engineering\nrequired', 'One model per task'],
    ['Multi-layer neural\nnetworks', 'AlexNet, CNNs, RNNs', 'Automatic feature\nlearning', 'Vision, speech, games\n(AlphaGo)'],
    ['Transformers at scale', 'GPT, BERT, Claude', 'Emergent reasoning &\ncoding', 'One model, many tasks'],
    ['LLMs + tools + memory', 'Goal-directed loops', 'Plans, acts,\nself-corrects', 'Single agent autonomy'],
    ['Multiple coordinating\nagents', 'Specialized roles\n(researcher, coder,\nreviewer)', 'Shared memory &\nconsensus', 'Collective intelligence'],
]


def draw_box(cx, cy, w, h, color, text, fontsize=10, fontweight='bold'):
    rect = patches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle="round,pad=0.05", facecolor=color, edgecolor='none'
    )
    ax.add_patch(rect)
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fontsize,
            color='white', fontweight=fontweight, linespacing=1.2)


# Header row (bold, larger font)
box_h = 0.55
y_header = 8.2
for i, (cx, label) in enumerate(zip(cols, headers)):
    draw_box(cx, y_header, col_w, box_h, era_colors[i], label, fontsize=13, fontweight='bold')

# Date row (bold, larger font)
y_date = 7.3
for i, (cx, label) in enumerate(zip(cols, dates)):
    draw_box(cx, y_date, col_w, box_h, era_colors[i], label, fontsize=12, fontweight='bold')

# Horizontal solid black timeline axis
y_line = 6.5
ax.plot([0.5, 19.5], [y_line, y_line], color='black', linewidth=1.5, linestyle='-')
ax.annotate('', xy=(19.5, y_line), xytext=(19.2, y_line),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# Capability boxes
cap_box_h = 0.75
y_start = 5.6
y_gap = 1.05

# Vertical dashed black lines (connectors from date row to first capability box)
y_cap_top = y_start + cap_box_h / 2
for cx in cols:
    ax.plot([cx, cx], [y_date - box_h/2, y_cap_top], color='black', linewidth=1.0, linestyle='--')

# Draw capability boxes (slightly smaller font than headers, still bold)
for col_i, cx in enumerate(cols):
    for row_i, cap_text in enumerate(capabilities[col_i]):
        cy = y_start - row_i * y_gap
        draw_box(cx, cy, col_w, cap_box_h, cap_colors[col_i], cap_text,
                 fontsize=10, fontweight='bold')

plt.tight_layout(pad=0.5)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'AI_history_overview_v4.png')
fig.savefig(out, dpi=200, bbox_inches='tight', transparent=True)
plt.close()
print(f'Saved: {out}')
