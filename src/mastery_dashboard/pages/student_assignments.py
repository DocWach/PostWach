import pandas as pd
import streamlit as st

from ..config.schema import CourseConfig
from ..data.provider import MasteryDataProvider


def render_student_assignments(
    provider: MasteryDataProvider,
    config: CourseConfig,
    student_id: str,
) -> None:
    student = provider.students.get(student_id)
    if not student:
        st.error("Student not found.")
        return

    st.header(f"Assignments: {student.name}")

    submissions = provider.get_student_submissions(student_id)

    if not submissions:
        st.info("No submissions yet.")
        return

    # Summary metrics
    cols = st.columns(3)
    evaluated = [s for s in submissions if s.status.value == "evaluated"]
    pending = [s for s in submissions if s.status.value == "pending"]
    needs_review = [s for s in submissions if s.status.value == "needs_review"]

    with cols[0]:
        st.metric("Total Submissions", len(submissions))
    with cols[1]:
        st.metric("Evaluated", len(evaluated))
    with cols[2]:
        st.metric("Pending", len(pending) + len(needs_review))

    st.divider()

    # Submission table
    st.subheader("Submission History")
    rows = []
    for sub in submissions:
        outcome = config.get_outcome(sub.outcome_id)
        block = config.get_block_for_outcome(sub.outcome_id)
        rows.append({
            "Submitted": sub.submitted_at.strftime("%Y-%m-%d %H:%M"),
            "Block": block.name.split(":")[0].strip() if block else "—",
            "Outcome": sub.outcome_id,
            "Name": outcome.name if outcome else "—",
            "Score": f"{sub.score:.0%}",
            "Status": sub.status.value.replace("_", " ").title(),
            "Notes": sub.evaluator_notes or "—",
        })
    st.table(pd.DataFrame(rows))
