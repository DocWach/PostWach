import streamlit as st

from ..components.block_progress import block_progress_row
from ..components.grade_guide import grade_guide
from ..components.grade_indicator import grade_indicator
from ..components.grade_pathway import grade_pathway_cards, overall_progress_bar
from ..components.outcome_checklist import outcome_checklist
from ..config.schema import CourseConfig
from ..data.provider import MasteryDataProvider
from ..models.enums import MasteryStatus


def render_student_compass(
    provider: MasteryDataProvider,
    config: CourseConfig,
    student_id: str,
) -> None:
    view = provider.get_student_grade_view(student_id)
    if view is None:
        st.error("Student not found.")
        return

    # Title bar
    st.markdown(
        f"""<div style="text-align:center; padding:0.8rem 0; margin-bottom:0.5rem;">
            <div style="font-size:1.8rem; font-weight:700; color:#1a1a5e;">Mastery Progress Tracker</div>
            <div style="font-size:0.95rem; color:#666;">Track Your Learning Outcomes</div>
        </div>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div style="text-align:right; color:#555; margin-bottom:0.5rem;">'
        f'Hello, {view.student.name}!</div>',
        unsafe_allow_html=True,
    )

    # Grade Goal selector (change #4)
    available_grades = sorted(
        [r.grade for r in config.grade_rules],
        key=lambda g: next(r.display_order for r in config.grade_rules if r.grade == g),
    )
    goal_key = f"grade_goal_{student_id}"
    if goal_key not in st.session_state:
        # Default to one grade above current, or highest
        if view.next_grade:
            st.session_state[goal_key] = view.next_grade
        elif view.current_grade:
            st.session_state[goal_key] = view.current_grade
        else:
            st.session_state[goal_key] = available_grades[-1] if available_grades else None

    # --- Main layout: left panel + right panel ---
    left, right = st.columns([1, 2])

    with left:
        # Current grade + goal (change #1 framing)
        grade_indicator(
            current_grade=view.current_grade,
            grade_goal=st.session_state.get(goal_key),
        )

        st.markdown("")  # spacer
        grade_goal = st.selectbox(
            "Set your grade goal",
            options=available_grades,
            index=available_grades.index(st.session_state[goal_key])
            if st.session_state.get(goal_key) in available_grades else 0,
            key=f"goal_select_{student_id}",
        )
        st.session_state[goal_key] = grade_goal

        st.divider()

        # Grade Guide (change #1)
        grade_guide(config, current_grade=view.current_grade)

    with right:
        # Learning Objectives Mastery checklist (change #3)
        st.markdown("#### Learning Objectives Mastery")
        outcome_checklist(config, view.mastery_records)

    st.divider()

    # Grade Pathway Progress (change #2)
    st.markdown("#### Grade Pathway Progress")
    grade_pathway_cards(
        config,
        view.completed_blocks,
        view.mastery_records,
        grade_goal=st.session_state.get(goal_key),
    )
    overall_progress_bar(
        config,
        view.mastery_records,
        grade_goal=st.session_state.get(goal_key),
    )

    # Block detail with radial gauges (change #6 — secondary view)
    with st.expander("Block Detail (gauges)"):
        gauges = block_progress_row(view.block_progress)
        cols = st.columns(len(gauges))
        for col, fig in zip(cols, gauges):
            with col:
                st.plotly_chart(fig, use_container_width=True)
