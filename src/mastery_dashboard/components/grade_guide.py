from typing import Optional

import streamlit as st

from ..config.schema import CourseConfig

_GRADE_COLORS = {
    "A": "#27AE60",
    "B": "#2E86AB",
    "C": "#F39C12",
    "D": "#E67E22",
}

_GRADE_LABELS = {
    "A": "Excellent",
    "B": "Good",
    "C": "Satisfactory",
    "D": "Developing",
}


def grade_guide(config: CourseConfig, current_grade: Optional[str] = None) -> None:
    st.markdown("#### Grade Guide")

    sorted_rules = sorted(config.grade_rules, key=lambda r: r.display_order)

    for rule in sorted_rules:
        color = _GRADE_COLORS.get(rule.grade, "#95A5A6")
        label = _GRADE_LABELS.get(rule.grade, rule.grade)
        block_names = []
        for bid in rule.required_blocks:
            block = config.get_block(bid)
            block_names.append(block.name if block else bid)

        is_current = rule.grade == current_grade
        border = f"3px solid {color}" if is_current else "1px solid #ddd"

        blocks_html = ", ".join(block_names)
        st.markdown(
            f"""<div style="display:flex; align-items:center; gap:0.75rem; padding:0.6rem 0.8rem;
                            margin-bottom:0.5rem; border:{border}; border-radius:8px; background:#fff;">
                <div style="min-width:2.5rem; height:2.5rem; background:{color}; border-radius:6px;
                            display:flex; align-items:center; justify-content:center;
                            color:#fff; font-weight:800; font-size:1.2rem;">{rule.grade}</div>
                <div>
                    <div style="font-weight:600; color:#1a1a2e;">{label}</div>
                    <div style="font-size:0.8rem; color:#555;">Mastery achieved for: {blocks_html}</div>
                </div>
            </div>""",
            unsafe_allow_html=True,
        )
