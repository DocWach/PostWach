from typing import Dict

import streamlit as st

from ..config.schema import BlockConfig, CourseConfig
from ..models.enums import MasteryStatus

_STATUS_BADGE = {
    MasteryStatus.MASTERED: ('<span style="color:#27AE60; font-weight:600;">&#10004; Mastered</span>'),
    MasteryStatus.IN_PROGRESS: ('<span style="color:#E67E22; font-weight:600;">&#9888; In Progress</span>'),
    MasteryStatus.NOT_ATTEMPTED: ('<span style="color:#aaa;">&#9675;</span>'),
}

_CHECK_ICON = {
    MasteryStatus.MASTERED: '<span style="color:#27AE60; font-size:1.1rem;">&#10004;</span>',
    MasteryStatus.IN_PROGRESS: '<span style="color:#E67E22; font-size:1.1rem;">&#10004;</span>',
    MasteryStatus.NOT_ATTEMPTED: '<span style="color:#ccc; font-size:1.1rem;">&#10004;</span>',
}

_BLOCK_COLORS = ["#1a1a5e", "#2a4a7f", "#3a6a5e", "#4a3a6e"]


def outcome_checklist(
    config: CourseConfig,
    mastery_map: Dict[str, MasteryStatus],
) -> None:
    for i, block in enumerate(config.blocks):
        color = _BLOCK_COLORS[i % len(_BLOCK_COLORS)]
        _render_block_section(block, mastery_map, color)


def _render_block_section(
    block: BlockConfig,
    mastery_map: Dict[str, MasteryStatus],
    header_color: str,
) -> None:
    st.markdown(
        f"""<div style="background:{header_color}; color:#fff; padding:0.5rem 0.8rem;
                        border-radius:6px 6px 0 0; margin-top:1rem; font-weight:600;">
            {block.name}
        </div>""",
        unsafe_allow_html=True,
    )

    for outcome in block.outcomes:
        status = mastery_map.get(outcome.id, MasteryStatus.NOT_ATTEMPTED)
        check = _CHECK_ICON[status]
        badge = _STATUS_BADGE[status]

        st.markdown(
            f"""<div style="display:flex; justify-content:space-between; align-items:center;
                            padding:0.45rem 0.8rem; border-bottom:1px solid #eee; background:#fff;">
                <div style="display:flex; align-items:center; gap:0.5rem;">
                    {check}
                    <span style="font-weight:600; color:#1a1a5e;">{outcome.id}</span>
                    <span style="color:#333;">{outcome.name}</span>
                </div>
                <div>{badge}</div>
            </div>""",
            unsafe_allow_html=True,
        )

    # Close the section visually
    st.markdown(
        '<div style="border-bottom:2px solid #e0e0e0; margin-bottom:0.5rem;"></div>',
        unsafe_allow_html=True,
    )
