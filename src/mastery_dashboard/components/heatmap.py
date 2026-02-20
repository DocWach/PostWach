from typing import Dict, List

import plotly.graph_objects as go

from ..config.schema import CourseConfig
from ..models.enums import MasteryStatus


_STATUS_TO_NUM = {
    MasteryStatus.NOT_ATTEMPTED: 0,
    MasteryStatus.IN_PROGRESS: 1,
    MasteryStatus.MASTERED: 2,
}

_COLORSCALE = [
    [0.0, "#ECEFF1"],   # not attempted — grey
    [0.5, "#FFC107"],   # in progress — amber
    [1.0, "#4CAF50"],   # mastered — green
]


def mastery_heatmap(
    matrix: Dict[str, Dict[str, MasteryStatus]],
    student_names: Dict[str, str],
    config: CourseConfig,
) -> go.Figure:
    outcome_ids = config.all_outcome_ids()
    student_ids = sorted(matrix.keys())

    # Build labels grouped by block
    x_labels = []
    for block in config.blocks:
        for outcome in block.outcomes:
            x_labels.append(f"{outcome.id}")

    y_labels = [student_names.get(sid, sid) for sid in student_ids]

    z = []
    hover = []
    for sid in student_ids:
        row = []
        hover_row = []
        for oid in outcome_ids:
            status = matrix.get(sid, {}).get(oid, MasteryStatus.NOT_ATTEMPTED)
            row.append(_STATUS_TO_NUM[status])
            hover_row.append(f"{student_names.get(sid, sid)}<br>{oid}: {status.value.replace('_', ' ').title()}")
        z.append(row)
        hover.append(hover_row)

    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=x_labels,
        y=y_labels,
        colorscale=_COLORSCALE,
        zmin=0,
        zmax=2,
        hovertext=hover,
        hoverinfo="text",
        showscale=False,
    ))

    # Add block separator lines
    pos = 0
    for block in config.blocks:
        pos += len(block.outcomes)
        if pos < len(outcome_ids):
            fig.add_vline(x=pos - 0.5, line_dash="dash", line_color="#999", line_width=1)

    fig.update_layout(
        height=max(300, len(student_ids) * 30 + 100),
        margin=dict(l=120, r=20, t=40, b=80),
        xaxis=dict(side="bottom", tickangle=-45),
        yaxis=dict(autorange="reversed"),
    )

    return fig
