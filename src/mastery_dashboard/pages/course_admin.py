import streamlit as st

from ..config.schema import CourseConfig
from ..data.provider import MasteryDataProvider
from ..data.seed import seed_demo_data


def render_course_admin(
    provider: MasteryDataProvider,
    config: CourseConfig,
    conn,
) -> None:
    st.header("Course Administration")

    # Course info
    st.subheader("Course Configuration")
    st.markdown(f"**Name:** {config.name}")
    st.markdown(f"**ID:** {config.id}")
    st.markdown(f"**Semester:** {config.semester}")
    st.markdown(f"**Default Evaluator:** {config.default_evaluator}")

    st.divider()

    # Blocks and outcomes
    st.subheader("Blocks & Outcomes")
    for block in config.blocks:
        with st.expander(f"{block.name} ({len(block.outcomes)} outcomes)"):
            st.markdown(f"*{block.description}*" if block.description else "")
            for outcome in block.outcomes:
                criteria = outcome.mastery_criteria
                detail = f"type={criteria.type}"
                if criteria.min_score is not None:
                    detail += f", min_score={criteria.min_score}"
                st.markdown(f"- **{outcome.id}**: {outcome.name} [{detail}]")

    st.divider()

    # Grade rules
    st.subheader("Grade Rules")
    for rule in sorted(config.grade_rules, key=lambda r: r.display_order):
        blocks_str = ", ".join(rule.required_blocks)
        st.markdown(f"**{rule.grade}**: {blocks_str}")

    st.divider()

    # Actions
    st.subheader("Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Seed Demo Data", key="admin_seed"):
            seed_demo_data(conn, config)
            st.success("Demo data seeded!")
            st.rerun()
    with col2:
        if st.button("Reload Config", key="admin_reload"):
            st.rerun()
