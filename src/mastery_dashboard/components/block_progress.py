from typing import List

import plotly.graph_objects as go

from ..models.domain import BlockProgress


_STATUS_COLORS = {
    "mastered": "#2ECC71",
    "in_progress": "#F39C12",
    "not_attempted": "#BDC3C7",
}


def block_gauge(bp: BlockProgress) -> go.Figure:
    pct = bp.completion_ratio * 100
    if pct >= 100:
        bar_color = _STATUS_COLORS["mastered"]
    elif pct > 0:
        bar_color = _STATUS_COLORS["in_progress"]
    else:
        bar_color = _STATUS_COLORS["not_attempted"]

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=pct,
        number={"suffix": "%", "font": {"size": 24}},
        domain={"x": [0, 1], "y": [0, 1]},
        title={"text": bp.block_name, "font": {"size": 13}},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 1},
            "bar": {"color": bar_color, "thickness": 0.75},
            "bgcolor": "#ECEFF1",
            "steps": [
                {"range": [0, 100], "color": "#ECEFF1"},
            ],
        },
    ))
    fig.update_layout(
        height=180,
        margin=dict(l=20, r=20, t=40, b=10),
    )
    return fig


def block_progress_row(blocks: List[BlockProgress]) -> List[go.Figure]:
    return [block_gauge(bp) for bp in blocks]
