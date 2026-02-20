from typing import Dict, Optional, Set

import streamlit as st

from ..config.schema import CourseConfig
from ..models.enums import MasteryStatus

_GRADE_COLORS = {
    "D": "#E67E22",
    "C": "#F39C12",
    "B": "#2E86AB",
    "A": "#27AE60",
}


def grade_pathway_cards(
    config: CourseConfig,
    completed_blocks: Set[str],
    mastery_map: Dict[str, MasteryStatus],
    grade_goal: Optional[str] = None,
) -> None:
    sorted_rules = sorted(config.grade_rules, key=lambda r: r.display_order, reverse=True)

    cols = st.columns(len(sorted_rules))
    for col, rule in zip(cols, sorted_rules):
        required = set(rule.required_blocks)
        is_complete = required.issubset(completed_blocks)
        color = _GRADE_COLORS.get(rule.grade, "#95A5A6")
        is_goal = rule.grade == grade_goal

        # Count mastered outcomes across required blocks
        total = 0
        mastered = 0
        for bid in rule.required_blocks:
            for oid in config.outcome_ids_for_block(bid):
                total += 1
                if mastery_map.get(oid) == MasteryStatus.MASTERED:
                    mastered += 1

        remaining = total - mastered

        # Build checkmark row
        checks = ""
        for i in range(total):
            if i < mastered:
                checks += '<span style="color:#27AE60; font-size:1.1rem;">&#10004;</span> '
            else:
                checks += '<span style="color:#ccc; font-size:1.1rem;">&#9675;</span> '

        if is_complete:
            status_html = '<div style="color:#27AE60; font-weight:600; font-size:0.8rem;">&#10003; MASTERED!</div>'
        else:
            # Find which blocks are incomplete and what outcomes remain
            needed_blocks = required - completed_blocks
            needed_names = []
            for bid in needed_blocks:
                block = config.get_block(bid)
                if block:
                    needed_names.append(block.name.split(":")[0].strip())
            hint = ", ".join(needed_names) if needed_names else ""
            status_html = (
                f'<div style="color:#555; font-size:0.75rem;">'
                f'{remaining} more to master'
                f'</div>'
            )

        border = f"3px solid {color}" if is_goal else "1px solid #ddd"
        goal_badge = ""
        if is_goal:
            goal_badge = '<div style="font-size:0.65rem; color:#fff; background:#555; padding:1px 6px; border-radius:3px; margin-top:2px;">YOUR GOAL</div>'

        with col:
            st.markdown(
                f"""<div style="text-align:center; padding:0.8rem 0.5rem; border:{border};
                                border-radius:10px; background:#fff; min-height:140px;">
                    <div style="background:{color}; color:#fff; font-weight:800; font-size:1.3rem;
                                padding:0.3rem 0.8rem; border-radius:6px; display:inline-block;
                                margin-bottom:0.4rem;">{rule.grade} Pathway</div>
                    {goal_badge}
                    <div style="margin:0.5rem 0; line-height:1.6;">{checks}</div>
                    {status_html}
                </div>""",
                unsafe_allow_html=True,
            )


def overall_progress_bar(
    config: CourseConfig,
    mastery_map: Dict[str, MasteryStatus],
    grade_goal: Optional[str] = None,
) -> None:
    """Single progress bar toward the grade goal."""
    if not grade_goal:
        return

    sorted_rules = sorted(config.grade_rules, key=lambda r: r.display_order)
    target_rule = None
    for rule in sorted_rules:
        if rule.grade == grade_goal:
            target_rule = rule
            break

    if not target_rule:
        return

    total = 0
    mastered = 0
    for bid in target_rule.required_blocks:
        for oid in config.outcome_ids_for_block(bid):
            total += 1
            if mastery_map.get(oid) == MasteryStatus.MASTERED:
                mastered += 1

    pct = mastered / total if total > 0 else 0
    color = _GRADE_COLORS.get(grade_goal, "#2E86AB")

    st.markdown(
        f"""<div style="margin:0.5rem 0;">
            <div style="font-size:0.85rem; color:#555; margin-bottom:0.3rem;">
                Complete the remaining outcomes to reach your grade goal!
            </div>
            <div style="background:#e0e0e0; border-radius:8px; height:14px; overflow:hidden;">
                <div style="background:{color}; width:{pct*100:.0f}%; height:100%; border-radius:8px;
                            transition: width 0.3s;"></div>
            </div>
            <div style="font-size:0.75rem; color:#777; margin-top:0.2rem; text-align:right;">
                {mastered}/{total} outcomes mastered ({pct:.0%})
            </div>
        </div>""",
        unsafe_allow_html=True,
    )
