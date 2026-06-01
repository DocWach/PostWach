"""Generate INSIGHT Figure 1: Six paradigms of AI evolution.

V6.1 layout (2026-05-04):
  - Top half (compact): paradigm header, prominent date row, timeline arrow.
  - Bottom half (~30% smaller than v6, ~3.0 units): three info rows per paradigm
    (method / character / limitation) on a pale tint with BLACK bold text for readability.
  - Top half: white text on saturated paradigm color (high impact identification).
  - Bottom half: black text on ~15%-saturation paradigm tint (substantive body content).
  - Row dividers in info box: paradigm color at 50% alpha (visible against pale bg).
  - Transparent figure background.
"""
from __future__ import annotations

import sys

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


PARADIGMS = [
    {
        "name": "Expert\nSystems",
        "dates": "1970s–1980s",
        "color": "#2C5F8D",
        "method": "Rule-based\nif-then logic",
        "character": "Human-encoded\nknowledge",
        "limitation": "Brittle, narrow,\nno learning",
    },
    {
        "name": "Machine\nLearning",
        "dates": "1990s–2010s",
        "color": "#2E7D5C",
        "method": "Learning patterns\nfrom data",
        "character": "Statistical methods,\nearly neural nets",
        "limitation": "Feature engineering;\none task per model",
    },
    {
        "name": "Deep\nLearning",
        "dates": "2012–2020",
        "color": "#7A4F2A",
        "method": "Multi-layer\nneural networks",
        "character": "Auto feature\nlearning",
        "limitation": "Single-task;\ndata-hungry",
    },
    {
        "name": "Large Language\nModels",
        "dates": "2018–2023",
        "color": "#1F7A6B",
        "method": "Transformers\nat scale",
        "character": "Generation,\nnot classification",
        "limitation": "Hallucination;\nspecialist trade-off",
    },
    {
        "name": "Agentic\nAI",
        "dates": "2023–2024",
        "color": "#5E3D87",
        "method": "LLM + tools\n+ memory",
        "character": "Goal-directed\ncontrol loops",
        "limitation": "Designer-specified\npipelines",
    },
    {
        "name": "Agentic\nSwarms",
        "dates": "2024–Present",
        "color": "#9C4D9F",
        "method": "Multiple coordinating\nagents",
        "character": "Shared memory;\nconsensus",
        "limitation": "Validation methods\nnascent",
    },
]


def _hex_to_rgb01(h: str) -> tuple[float, float, float]:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))


def _pale(hex_color: str, mix: float = 0.15) -> tuple[float, float, float]:
    """Return RGB of paradigm color blended with white at `mix` weight."""
    r, g, b = _hex_to_rgb01(hex_color)
    return (r * mix + 1.0 * (1 - mix),
            g * mix + 1.0 * (1 - mix),
            b * mix + 1.0 * (1 - mix))


def main(out_path: str) -> None:
    fig, ax = plt.subplots(figsize=(13, 5.0))
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5.5)
    ax.axis("off")

    col_w = 0.94
    n = len(PARADIGMS)

    # Y bands (top down) -- bottom half ~30% smaller than v6
    header_top = 5.40
    header_h = 0.70
    date_top = 4.55
    date_h = 0.85
    arrow_y = 3.45

    info_top = 3.15
    info_bottom = 0.15
    info_h = info_top - info_bottom  # 3.0 units (vs ~5.3 in v6)

    for i, p in enumerate(PARADIGMS):
        cx = i + 0.5

        # Header (white text on saturated paradigm color)
        header = mpatches.FancyBboxPatch(
            (cx - col_w / 2, header_top - header_h),
            col_w, header_h,
            boxstyle="round,pad=0.02",
            facecolor=p["color"],
            edgecolor="none",
        )
        ax.add_patch(header)
        ax.text(
            cx, header_top - header_h / 2,
            p["name"],
            ha="center", va="center",
            color="white",
            fontsize=12,
            fontweight="bold",
        )

        # Date row (prominent; white text on near-saturated paradigm color)
        date_bg = mpatches.FancyBboxPatch(
            (cx - col_w / 2, date_top - date_h),
            col_w, date_h,
            boxstyle="round,pad=0.02",
            facecolor=p["color"],
            edgecolor="none",
            alpha=0.85,
        )
        ax.add_patch(date_bg)
        ax.text(
            cx, date_top - date_h / 2,
            p["dates"],
            ha="center", va="center",
            color="white",
            fontsize=15,
            fontweight="bold",
        )

        # Bottom info box (PALE tint of paradigm color, BLACK bold text)
        pale_bg = _pale(p["color"], mix=0.15)
        info_bg = mpatches.FancyBboxPatch(
            (cx - col_w / 2, info_bottom),
            col_w, info_h,
            boxstyle="round,pad=0.02",
            facecolor=pale_bg,
            edgecolor="none",
        )
        ax.add_patch(info_bg)

        # Three rows of black bold text inside the pale info box
        rows = [p["method"], p["character"], p["limitation"]]
        n_rows = len(rows)
        for j, txt in enumerate(rows):
            frac = (j + 0.5) / n_rows
            y = info_top - frac * info_h
            ax.text(
                cx, y,
                txt,
                ha="center", va="center",
                color="black",
                fontsize=11,
                fontweight="bold",
                linespacing=1.10,
            )

        # Row dividers in info box: paradigm color at 50% alpha (visible against pale bg)
        for j in range(1, n_rows):
            y = info_top - (j / n_rows) * info_h
            ax.plot(
                [cx - col_w / 2 + 0.06, cx + col_w / 2 - 0.06],
                [y, y],
                color=p["color"],
                alpha=0.50,
                linewidth=0.9,
            )

    # Timeline arrow across the figure between date row and info boxes
    arrow = FancyArrowPatch(
        (0.05, arrow_y), (n - 0.05, arrow_y),
        arrowstyle="->",
        mutation_scale=24,
        linewidth=2.4,
        color="#222222",
    )
    ax.add_patch(arrow)

    plt.tight_layout(pad=0.4)
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    plt.savefig(out_path, dpi=200, bbox_inches="tight", transparent=True)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "AI_history_overview_v5.png"
    main(out)
