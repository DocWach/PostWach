from typing import Dict, List

import pandas as pd
import streamlit as st

from ..config.schema import CourseConfig
from ..models.domain import Submission


_STATUS_BADGES = {
    "pending": "🟡 Pending",
    "evaluated": "✅ Evaluated",
    "needs_review": "🔴 Needs Review",
}


def submission_review_table(
    submissions: List[Submission],
    student_names: Dict[str, str],
    config: CourseConfig,
) -> pd.DataFrame:
    rows = []
    for sub in submissions:
        outcome = config.get_outcome(sub.outcome_id)
        rows.append({
            "Student": student_names.get(sub.student_id, sub.student_id),
            "Outcome": sub.outcome_id,
            "Outcome Name": outcome.name if outcome else "—",
            "Score": f"{sub.score:.0%}",
            "Status": _STATUS_BADGES.get(sub.status.value, sub.status.value),
            "Submitted": sub.submitted_at.strftime("%Y-%m-%d %H:%M"),
            "submission_id": sub.id,
            "student_id": sub.student_id,
        })
    return pd.DataFrame(rows)
