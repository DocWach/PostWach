from typing import Optional, Union

import streamlit as st


def metric_card(
    title: str,
    value: Union[str, int, float],
    delta: Optional[str] = None,
    delta_color: str = "normal",
    help_text: Optional[str] = None,
) -> None:
    st.metric(
        label=title,
        value=value,
        delta=delta,
        delta_color=delta_color,
        help=help_text,
    )


def grade_metric(grade: Optional[str], label: str = "Current Grade") -> None:
    display = grade if grade else "—"
    st.markdown(
        f"""
        <div style="text-align:center; padding:1rem; background:#f0f2f6; border-radius:10px;">
            <div style="font-size:0.85rem; color:#555;">{label}</div>
            <div style="font-size:3.5rem; font-weight:700; color:#1f1f1f; line-height:1.2;">{display}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
