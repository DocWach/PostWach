"""
Mastery-Based Assessment Dashboard
===================================
Entry point: streamlit run src/mastery_dashboard/app.py
"""
from pathlib import Path

import streamlit as st

from mastery_dashboard.config.loader import load_course_config
from mastery_dashboard.data.database import get_connection, init_schema
from mastery_dashboard.data.provider import MasteryDataProvider
from mastery_dashboard.data.repositories import AuditRepo, MasteryRepo, SubmissionRepo
from mastery_dashboard.data.seed import seed_demo_data
from mastery_dashboard.logic.mastery_engine import MasteryEngine
from mastery_dashboard.pages.instructor_overview import render_instructor_overview
from mastery_dashboard.pages.student_assignments import render_student_assignments
from mastery_dashboard.pages.student_compass import render_student_compass

_CONFIG_PATH = Path(__file__).parent / "config" / "sample_course.yaml"
_DB_PATH = Path(__file__).parent / "data" / "mastery.db"


def main():
    st.set_page_config(
        page_title="Mastery Progress Tracker",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Load config
    config = load_course_config(_CONFIG_PATH)

    # Database
    conn = get_connection(str(_DB_PATH))
    init_schema(conn)

    # Providers and engines
    provider = MasteryDataProvider(conn, config)
    engine = MasteryEngine(
        config=config,
        mastery_repo=MasteryRepo(conn),
        submission_repo=SubmissionRepo(conn),
        audit_repo=AuditRepo(conn),
    )

    # Sidebar
    with st.sidebar:
        st.title("Mastery Dashboard")
        st.caption(f"{config.name} — {config.semester}")

        st.divider()

        role = st.radio("Role", ["Student", "Instructor"], index=0)

        students = provider.students.list_all()

        selected_id = None
        student_page = "Dashboard"

        if role == "Student" and students:
            selected_name = st.selectbox(
                "Student",
                options=[s.name for s in students],
            )
            selected_id = next(s.id for s in students if s.name == selected_name)

            st.divider()

            # Student page tabs (change #5 — submission history on separate page)
            student_page = st.radio(
                "Page",
                ["Dashboard", "Assignments"],
                index=0,
                horizontal=True,
            )

        st.divider()

        if st.button("Seed Demo Data", use_container_width=True):
            seed_demo_data(conn, config)
            st.success("Demo data loaded!")
            st.rerun()

    # Page routing
    if role == "Student":
        if selected_id:
            if student_page == "Dashboard":
                render_student_compass(provider, config, selected_id)
            else:
                render_student_assignments(provider, config, selected_id)
        elif not students:
            st.info("No students found. Use 'Seed Demo Data' in the sidebar to load sample data.")
    else:
        if students:
            render_instructor_overview(provider, config, engine)
        else:
            st.info("No students found. Use 'Seed Demo Data' in the sidebar to load sample data.")


if __name__ == "__main__":
    main()
