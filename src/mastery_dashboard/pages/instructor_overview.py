import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

from ..components.heatmap import mastery_heatmap
from ..components.metric_cards import metric_card
from ..components.submission_table import submission_review_table
from ..config.schema import CourseConfig
from ..data.provider import MasteryDataProvider
from ..logic.mastery_engine import MasteryEngine
from ..models.enums import MasteryStatus


def render_instructor_overview(
    provider: MasteryDataProvider,
    config: CourseConfig,
    engine: MasteryEngine,
) -> None:
    st.header("Instructor Overview")

    students = provider.students.list_all()
    student_names = {s.id: s.name for s in students}
    student_ids = [s.id for s in students]

    # 1. Class metrics row
    st.subheader("Class Metrics")
    outcome_stats = provider.get_class_outcome_stats()
    grade_dist = provider.get_grade_distribution()

    total_students = len(students)
    avg_mastery = 0.0
    if outcome_stats:
        avg_mastery = sum(s.mastery_rate for s in outcome_stats) / len(outcome_stats)

    cols = st.columns(4)
    with cols[0]:
        metric_card("Total Students", total_students)
    with cols[1]:
        metric_card("Avg Mastery Rate", f"{avg_mastery:.0%}")
    with cols[2]:
        graded = total_students - grade_dist.get("No Grade", 0)
        metric_card("Students Graded", f"{graded}/{total_students}")
    with cols[3]:
        pending_count = len(provider.get_pending_submissions())
        metric_card("Pending Reviews", pending_count)

    st.divider()

    # 2. Mastery heatmap
    st.subheader("Mastery Heatmap")
    outcome_ids = config.all_outcome_ids()
    matrix = provider.mastery.get_matrix(student_ids, outcome_ids)
    if matrix:
        fig = mastery_heatmap(matrix, student_names, config)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No mastery data to display.")

    st.divider()

    # 3. Outcome difficulty + grade distribution side by side
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Outcome Difficulty")
        if outcome_stats:
            sorted_stats = sorted(outcome_stats, key=lambda s: s.mastery_rate)
            fig = go.Figure(go.Bar(
                x=[s.mastery_rate * 100 for s in sorted_stats],
                y=[f"{s.outcome_id}: {s.outcome_name}" for s in sorted_stats],
                orientation="h",
                marker_color=["#E74C3C" if s.mastery_rate < 0.3
                              else "#F39C12" if s.mastery_rate < 0.6
                              else "#2ECC71" for s in sorted_stats],
            ))
            fig.update_layout(
                height=max(300, len(sorted_stats) * 28 + 60),
                margin=dict(l=180, r=20, t=10, b=40),
                xaxis_title="Mastery Rate (%)",
                xaxis=dict(range=[0, 100]),
            )
            st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("Grade Distribution")
        grades = [g for g in grade_dist if g != "No Grade"]
        grades_sorted = sorted(grades) + (["No Grade"] if grade_dist.get("No Grade", 0) > 0 else [])
        colors = {"A": "#27AE60", "B": "#2E86AB", "C": "#F39C12", "D": "#E67E22", "No Grade": "#95A5A6"}

        fig = go.Figure(go.Bar(
            x=grades_sorted,
            y=[grade_dist.get(g, 0) for g in grades_sorted],
            marker_color=[colors.get(g, "#95A5A6") for g in grades_sorted],
        ))
        fig.update_layout(
            height=300,
            margin=dict(l=40, r=20, t=10, b=40),
            yaxis_title="Students",
            xaxis_title="Grade",
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # 5. Submission review queue
    st.subheader("Submission Review Queue")
    pending = provider.get_pending_submissions()
    if pending:
        df = submission_review_table(pending, student_names, config)
        display_df = df.drop(columns=["submission_id", "student_id"])
        st.table(display_df)
    else:
        st.success("No pending submissions.")

    st.divider()

    # 6. Student drill-down with override controls
    st.subheader("Student Drill-Down")
    selected_name = st.selectbox(
        "Select student",
        options=[s.name for s in students],
        index=0 if students else None,
    )
    if selected_name:
        selected = next(s for s in students if s.name == selected_name)
        view = provider.get_student_grade_view(selected.id)
        if view:
            st.markdown(f"**Grade:** {view.current_grade or '—'} | "
                        f"**Completed blocks:** {', '.join(sorted(view.completed_blocks)) or 'None'}")

            # Override form
            with st.expander("Instructor Override"):
                override_outcome = st.selectbox(
                    "Outcome", options=config.all_outcome_ids(), key="override_outcome"
                )
                override_status = st.selectbox(
                    "New Status",
                    options=[s.value for s in MasteryStatus],
                    key="override_status",
                )
                override_reason = st.text_input("Reason", key="override_reason")

                if st.button("Apply Override"):
                    engine.instructor_override(
                        selected.id,
                        override_outcome,
                        MasteryStatus(override_status),
                        override_reason or None,
                    )
                    st.success(f"Override applied: {override_outcome} -> {override_status}")
                    st.rerun()

            # Per-block detail
            for bp in view.block_progress:
                block = config.get_block(bp.block_id)
                if not block:
                    continue
                with st.expander(f"{block.name} ({bp.mastered}/{bp.total_outcomes} mastered)"):
                    rows = []
                    for outcome in block.outcomes:
                        status = view.mastery_records.get(outcome.id, MasteryStatus.NOT_ATTEMPTED)
                        rows.append({
                            "Outcome": outcome.id,
                            "Name": outcome.name,
                            "Status": status.value.replace("_", " ").title(),
                        })
                    st.table(pd.DataFrame(rows))
