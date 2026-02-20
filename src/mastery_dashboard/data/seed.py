import random
import uuid
from datetime import datetime, timedelta

from ..config.schema import CourseConfig
from ..data.repositories import MasteryRepo, StudentRepo, SubmissionRepo
from ..logic.mastery_engine import MasteryEngine
from ..models.domain import MasteryRecord, Student, Submission
from ..models.enums import FlagSource, MasteryStatus, SubmissionStatus
from .database import init_schema
from .repositories import AuditRepo


_DEMO_STUDENTS = [
    ("Alice Chen", "achen@example.edu"),
    ("Bob Martinez", "bmartinez@example.edu"),
    ("Carol Johnson", "cjohnson@example.edu"),
    ("David Kim", "dkim@example.edu"),
    ("Eva Patel", "epatel@example.edu"),
    ("Frank Wilson", "fwilson@example.edu"),
    ("Grace Lee", "glee@example.edu"),
    ("Henry Brown", "hbrown@example.edu"),
    ("Irene Davis", "idavis@example.edu"),
    ("Jack Thompson", "jthompson@example.edu"),
]

# Profiles: each student gets a mastery probability per block
_PROFILES = [
    {"fundamentals": 1.0, "analysis": 1.0, "implementation": 1.0, "advanced": 0.8},  # A student
    {"fundamentals": 1.0, "analysis": 1.0, "implementation": 0.9, "advanced": 0.3},  # B student
    {"fundamentals": 1.0, "analysis": 1.0, "implementation": 0.7, "advanced": 0.1},  # B-/C+
    {"fundamentals": 1.0, "analysis": 0.8, "implementation": 0.3, "advanced": 0.0},  # C student
    {"fundamentals": 1.0, "analysis": 0.6, "implementation": 0.2, "advanced": 0.0},  # C-/D+
    {"fundamentals": 0.9, "analysis": 0.4, "implementation": 0.1, "advanced": 0.0},  # D student
    {"fundamentals": 1.0, "analysis": 1.0, "implementation": 1.0, "advanced": 1.0},  # A+ (all mastered)
    {"fundamentals": 0.7, "analysis": 0.3, "implementation": 0.0, "advanced": 0.0},  # Struggling
    {"fundamentals": 1.0, "analysis": 1.0, "implementation": 0.5, "advanced": 0.0},  # Mid-range
    {"fundamentals": 0.5, "analysis": 0.1, "implementation": 0.0, "advanced": 0.0},  # Early stage
]


def seed_demo_data(conn, config: CourseConfig) -> None:
    """Populate the database with demo students and mixed mastery states."""
    init_schema(conn)

    student_repo = StudentRepo(conn)
    mastery_repo = MasteryRepo(conn)
    submission_repo = SubmissionRepo(conn)
    audit_repo = AuditRepo(conn)

    random.seed(42)
    base_time = datetime.now() - timedelta(days=60)

    for i, (name, email) in enumerate(_DEMO_STUDENTS):
        student_id = f"student-{i+1:03d}"
        student = Student(id=student_id, name=name, email=email, created_at=base_time)
        student_repo.create(student)

        profile = _PROFILES[i]

        for block in config.blocks:
            prob = profile.get(block.id, 0.0)
            for outcome in block.outcomes:
                roll = random.random()
                if roll < prob:
                    status = MasteryStatus.MASTERED
                    score = random.uniform(0.80, 1.0)
                elif roll < prob + 0.15:
                    status = MasteryStatus.IN_PROGRESS
                    score = random.uniform(0.40, 0.79)
                else:
                    status = MasteryStatus.NOT_ATTEMPTED
                    score = 0.0

                if status != MasteryStatus.NOT_ATTEMPTED:
                    sub_time = base_time + timedelta(
                        days=random.randint(1, 55),
                        hours=random.randint(0, 23),
                    )
                    sub = Submission(
                        id=str(uuid.uuid4()),
                        student_id=student_id,
                        outcome_id=outcome.id,
                        score=round(score, 2),
                        status=SubmissionStatus.EVALUATED,
                        submitted_at=sub_time,
                        evaluated_at=sub_time + timedelta(hours=random.randint(1, 48)),
                    )
                    submission_repo.create(sub)

                    record = MasteryRecord(
                        student_id=student_id,
                        outcome_id=outcome.id,
                        status=status,
                        flag_source=FlagSource.AUTO,
                        updated_at=sub_time,
                    )
                    mastery_repo.upsert(record)

    # Add a few pending submissions for the review queue
    pending_students = ["student-004", "student-006", "student-008"]
    pending_outcomes = ["A2", "F3", "I1"]
    for sid, oid in zip(pending_students, pending_outcomes):
        sub = Submission(
            id=str(uuid.uuid4()),
            student_id=sid,
            outcome_id=oid,
            score=round(random.uniform(0.60, 0.90), 2),
            status=SubmissionStatus.PENDING,
            submitted_at=datetime.now() - timedelta(hours=random.randint(1, 12)),
        )
        submission_repo.create(sub)
