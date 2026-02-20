import pytest

from mastery_dashboard.config.schema import (
    BlockConfig,
    CourseConfig,
    GradeRuleConfig,
    MasteryCriteria,
    OutcomeConfig,
)
from mastery_dashboard.data.database import get_memory_connection, init_schema
from mastery_dashboard.data.repositories import (
    AuditRepo,
    MasteryRepo,
    StudentRepo,
    SubmissionRepo,
)


@pytest.fixture
def db():
    conn = get_memory_connection()
    init_schema(conn)
    yield conn
    conn.close()


@pytest.fixture
def student_repo(db):
    return StudentRepo(db)


@pytest.fixture
def submission_repo(db):
    return SubmissionRepo(db)


@pytest.fixture
def mastery_repo(db):
    return MasteryRepo(db)


@pytest.fixture
def audit_repo(db):
    return AuditRepo(db)


@pytest.fixture
def minimal_config():
    return CourseConfig(
        name="Test Course",
        id="test-101",
        semester="Spring 2026",
        default_evaluator="threshold",
        blocks=(
            BlockConfig(
                id="block_a",
                name="Block A",
                description="First block",
                outcomes=(
                    OutcomeConfig(id="A1", name="Outcome A1", description="",
                                  mastery_criteria=MasteryCriteria(type="threshold", min_score=0.80)),
                    OutcomeConfig(id="A2", name="Outcome A2", description="",
                                  mastery_criteria=MasteryCriteria(type="threshold", min_score=0.80)),
                ),
            ),
            BlockConfig(
                id="block_b",
                name="Block B",
                description="Second block",
                outcomes=(
                    OutcomeConfig(id="B1", name="Outcome B1", description="",
                                  mastery_criteria=MasteryCriteria(type="threshold", min_score=0.80)),
                    OutcomeConfig(id="B2", name="Outcome B2", description="",
                                  mastery_criteria=MasteryCriteria(type="checklist")),
                ),
            ),
            BlockConfig(
                id="block_c",
                name="Block C",
                description="Third block",
                outcomes=(
                    OutcomeConfig(id="C1", name="Outcome C1", description="",
                                  mastery_criteria=MasteryCriteria(type="manual")),
                ),
            ),
        ),
        grade_rules=(
            GradeRuleConfig(grade="A", required_blocks=("block_a", "block_b", "block_c"), display_order=1),
            GradeRuleConfig(grade="B", required_blocks=("block_a", "block_b"), display_order=2),
            GradeRuleConfig(grade="C", required_blocks=("block_a",), display_order=3),
        ),
    )
