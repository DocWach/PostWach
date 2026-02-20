from typing import Optional

import streamlit as st

_GRADE_COLORS = {
    "A": "#27AE60",
    "B": "#2E86AB",
    "C": "#F39C12",
    "D": "#E67E22",
}


def grade_indicator(
    current_grade: Optional[str],
    grade_goal: Optional[str] = None,
) -> None:
    col1, col2 = st.columns(2)

    with col1:
        display = current_grade if current_grade else "—"
        color = _GRADE_COLORS.get(current_grade or "", "#95A5A6")
        st.markdown(
            f"""<div style="text-align:center; padding:1.2rem; background:{color}; border-radius:12px;">
                <div style="font-size:0.85rem; color:#fff; opacity:0.85;">Current Grade</div>
                <div style="font-size:3.5rem; font-weight:800; color:#fff; line-height:1.1;">{display}</div>
            </div>""",
            unsafe_allow_html=True,
        )

    with col2:
        if grade_goal:
            goal_color = _GRADE_COLORS.get(grade_goal, "#95A5A6")
            st.markdown(
                f"""<div style="text-align:center; padding:1.2rem; background:#f8f9fa;
                                border:3px solid {goal_color}; border-radius:12px;">
                    <div style="font-size:0.85rem; color:#555;">Grade Goal</div>
                    <div style="font-size:3.5rem; font-weight:800; color:{goal_color}; line-height:1.1;">
                        {grade_goal}
                    </div>
                </div>""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """<div style="text-align:center; padding:1.2rem; background:#f8f9fa;
                               border:2px dashed #ccc; border-radius:12px;">
                    <div style="font-size:0.85rem; color:#555;">Grade Goal</div>
                    <div style="font-size:2rem; color:#aaa; line-height:1.5;">Select below</div>
                </div>""",
                unsafe_allow_html=True,
            )
