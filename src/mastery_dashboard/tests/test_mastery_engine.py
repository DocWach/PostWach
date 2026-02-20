import uuid

import pytest

from mastery_dashboard.data.repositories import AuditRepo, MasteryRepo, SubmissionRepo
from mastery_dashboard.logic.mastery_engine import MasteryEngine
from mastery_dashboard.models.domain import Student, Submission
from mastery_dashboard.models.enums import FlagSource, MasteryStatus, SubmissionStatus


@pytest.fixture
def engine(db, minimal_config):
    from mastery_dashboard.data.repositories import StudentRepo
    student_repo = StudentRepo(db)
    student_repo.create(Student(id="s1", name="Test Student", email="test@example.edu"))
    return MasteryEngine(
        config=minimal_config,
        mastery_repo=MasteryRepo(db),
        submission_repo=SubmissionRepo(db),
        audit_repo=AuditRepo(db),
    )


class TestProcessSubmission:
    def test_high_score_masters_outcome(self, engine, submission_repo):
        sub = Submission(
            id=str(uuid.uuid4()), student_id="s1", outcome_id="A1",
            score=0.90, status=SubmissionStatus.PENDING,
        )
        submission_repo.create(sub)
        record = engine.process_submission(sub)
        assert record.status == MasteryStatus.MASTERED

    def test_low_score_sets_in_progress(self, engine, submission_repo):
        sub = Submission(
            id=str(uuid.uuid4()), student_id="s1", outcome_id="A1",
            score=0.50, status=SubmissionStatus.PENDING,
        )
        submission_repo.create(sub)
        record = engine.process_submission(sub)
        assert record.status == MasteryStatus.IN_PROGRESS

    def test_no_auto_demotion(self, engine, submission_repo, mastery_repo):
        # First submission masters it
        sub1 = Submission(
            id=str(uuid.uuid4()), student_id="s1", outcome_id="A1",
            score=0.95, status=SubmissionStatus.PENDING,
        )
        submission_repo.create(sub1)
        engine.process_submission(sub1)

        # Second submission with lower score should not demote
        sub2 = Submission(
            id=str(uuid.uuid4()), student_id="s1", outcome_id="A1",
            score=0.30, status=SubmissionStatus.PENDING,
        )
        submission_repo.create(sub2)
        record = engine.process_submission(sub2)
        assert record.status == MasteryStatus.MASTERED

    def test_creates_audit_entry(self, engine, submission_repo, audit_repo):
        sub = Submission(
            id=str(uuid.uuid4()), student_id="s1", outcome_id="A1",
            score=0.90, status=SubmissionStatus.PENDING,
        )
        submission_repo.create(sub)
        engine.process_submission(sub)
        entries = audit_repo.list_by_student("s1")
        assert len(entries) == 1
        assert entries[0].new_status == MasteryStatus.MASTERED
        assert entries[0].source == FlagSource.AUTO

    def test_unknown_outcome_raises(self, engine, submission_repo):
        sub = Submission(
            id=str(uuid.uuid4()), student_id="s1", outcome_id="UNKNOWN",
            score=0.90, status=SubmissionStatus.PENDING,
        )
        submission_repo.create(sub)
        with pytest.raises(ValueError, match="Unknown outcome"):
            engine.process_submission(sub)


class TestInstructorOverride:
    def test_can_promote(self, engine):
        record = engine.instructor_override("s1", "C1", MasteryStatus.MASTERED, "Demonstrated in class")
        assert record.status == MasteryStatus.MASTERED
        assert record.flag_source == FlagSource.INSTRUCTOR

    def test_can_demote(self, engine, submission_repo):
        # First master via submission
        sub = Submission(
            id=str(uuid.uuid4()), student_id="s1", outcome_id="A1",
            score=0.95, status=SubmissionStatus.PENDING,
        )
        submission_repo.create(sub)
        engine.process_submission(sub)

        # Instructor demotes
        record = engine.instructor_override("s1", "A1", MasteryStatus.IN_PROGRESS, "Plagiarism detected")
        assert record.status == MasteryStatus.IN_PROGRESS

    def test_override_creates_audit(self, engine, audit_repo):
        engine.instructor_override("s1", "A1", MasteryStatus.MASTERED)
        entries = audit_repo.list_by_student("s1")
        assert len(entries) == 1
        assert entries[0].source == FlagSource.INSTRUCTOR
