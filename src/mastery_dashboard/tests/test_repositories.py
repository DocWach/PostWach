import uuid
from datetime import datetime

import pytest

from mastery_dashboard.models.domain import AuditEntry, MasteryRecord, Student, Submission
from mastery_dashboard.models.enums import FlagSource, MasteryStatus, SubmissionStatus


class TestStudentRepo:
    def test_create_and_get(self, student_repo):
        s = Student(id="s1", name="Alice", email="alice@example.edu")
        student_repo.create(s)
        result = student_repo.get("s1")
        assert result is not None
        assert result.name == "Alice"

    def test_get_nonexistent(self, student_repo):
        assert student_repo.get("nope") is None

    def test_list_all(self, student_repo):
        student_repo.create(Student(id="s1", name="Alice", email="a@example.edu"))
        student_repo.create(Student(id="s2", name="Bob", email="b@example.edu"))
        result = student_repo.list_all()
        assert len(result) == 2

    def test_delete(self, student_repo):
        student_repo.create(Student(id="s1", name="Alice", email="a@example.edu"))
        assert student_repo.delete("s1") is True
        assert student_repo.get("s1") is None

    def test_delete_nonexistent(self, student_repo):
        assert student_repo.delete("nope") is False


class TestSubmissionRepo:
    def _make_student(self, student_repo):
        student_repo.create(Student(id="s1", name="Alice", email="a@example.edu"))

    def test_create_and_get(self, student_repo, submission_repo):
        self._make_student(student_repo)
        sub = Submission(
            id="sub1", student_id="s1", outcome_id="A1",
            score=0.85, status=SubmissionStatus.PENDING,
        )
        submission_repo.create(sub)
        result = submission_repo.get("sub1")
        assert result is not None
        assert result.score == 0.85

    def test_list_by_student(self, student_repo, submission_repo):
        self._make_student(student_repo)
        submission_repo.create(Submission(
            id="sub1", student_id="s1", outcome_id="A1",
            score=0.85, status=SubmissionStatus.PENDING,
        ))
        submission_repo.create(Submission(
            id="sub2", student_id="s1", outcome_id="A2",
            score=0.70, status=SubmissionStatus.EVALUATED,
        ))
        result = submission_repo.list_by_student("s1")
        assert len(result) == 2

    def test_list_pending(self, student_repo, submission_repo):
        self._make_student(student_repo)
        submission_repo.create(Submission(
            id="sub1", student_id="s1", outcome_id="A1",
            score=0.85, status=SubmissionStatus.PENDING,
        ))
        submission_repo.create(Submission(
            id="sub2", student_id="s1", outcome_id="A2",
            score=0.70, status=SubmissionStatus.EVALUATED,
        ))
        result = submission_repo.list_pending()
        assert len(result) == 1
        assert result[0].id == "sub1"

    def test_update_status(self, student_repo, submission_repo):
        self._make_student(student_repo)
        submission_repo.create(Submission(
            id="sub1", student_id="s1", outcome_id="A1",
            score=0.85, status=SubmissionStatus.PENDING,
        ))
        submission_repo.update_status("sub1", SubmissionStatus.EVALUATED, datetime.now(), "Good work")
        result = submission_repo.get("sub1")
        assert result.status == SubmissionStatus.EVALUATED
        assert result.evaluator_notes == "Good work"


class TestMasteryRepo:
    def _make_student(self, student_repo):
        student_repo.create(Student(id="s1", name="Alice", email="a@example.edu"))

    def test_upsert_and_get(self, student_repo, mastery_repo):
        self._make_student(student_repo)
        record = MasteryRecord(
            student_id="s1", outcome_id="A1", status=MasteryStatus.IN_PROGRESS,
        )
        mastery_repo.upsert(record)
        result = mastery_repo.get("s1", "A1")
        assert result is not None
        assert result.status == MasteryStatus.IN_PROGRESS

    def test_upsert_overwrites(self, student_repo, mastery_repo):
        self._make_student(student_repo)
        mastery_repo.upsert(MasteryRecord(
            student_id="s1", outcome_id="A1", status=MasteryStatus.IN_PROGRESS,
        ))
        mastery_repo.upsert(MasteryRecord(
            student_id="s1", outcome_id="A1", status=MasteryStatus.MASTERED,
        ))
        result = mastery_repo.get("s1", "A1")
        assert result.status == MasteryStatus.MASTERED

    def test_list_by_student(self, student_repo, mastery_repo):
        self._make_student(student_repo)
        mastery_repo.upsert(MasteryRecord(student_id="s1", outcome_id="A1", status=MasteryStatus.MASTERED))
        mastery_repo.upsert(MasteryRecord(student_id="s1", outcome_id="A2", status=MasteryStatus.IN_PROGRESS))
        result = mastery_repo.list_by_student("s1")
        assert len(result) == 2

    def test_get_matrix(self, student_repo, mastery_repo):
        student_repo.create(Student(id="s1", name="A", email="a@example.edu"))
        student_repo.create(Student(id="s2", name="B", email="b@example.edu"))
        mastery_repo.upsert(MasteryRecord(student_id="s1", outcome_id="A1", status=MasteryStatus.MASTERED))
        mastery_repo.upsert(MasteryRecord(student_id="s2", outcome_id="A1", status=MasteryStatus.IN_PROGRESS))

        matrix = mastery_repo.get_matrix(["s1", "s2"], ["A1", "A2"])
        assert matrix["s1"]["A1"] == MasteryStatus.MASTERED
        assert matrix["s1"]["A2"] == MasteryStatus.NOT_ATTEMPTED
        assert matrix["s2"]["A1"] == MasteryStatus.IN_PROGRESS

    def test_get_matrix_empty_inputs(self, mastery_repo):
        assert mastery_repo.get_matrix([], []) == {}


class TestAuditRepo:
    def _make_student(self, student_repo):
        student_repo.create(Student(id="s1", name="Alice", email="a@example.edu"))

    def test_create_and_list(self, student_repo, audit_repo):
        self._make_student(student_repo)
        entry = AuditEntry(
            id=str(uuid.uuid4()), student_id="s1", outcome_id="A1",
            old_status=MasteryStatus.NOT_ATTEMPTED,
            new_status=MasteryStatus.MASTERED,
            source=FlagSource.INSTRUCTOR,
            reason="Override",
        )
        audit_repo.create(entry)
        result = audit_repo.list_by_student("s1")
        assert len(result) == 1
        assert result[0].source == FlagSource.INSTRUCTOR

    def test_list_all_with_limit(self, student_repo, audit_repo):
        self._make_student(student_repo)
        for i in range(5):
            audit_repo.create(AuditEntry(
                id=str(uuid.uuid4()), student_id="s1", outcome_id=f"A{i}",
                old_status=MasteryStatus.NOT_ATTEMPTED,
                new_status=MasteryStatus.MASTERED,
                source=FlagSource.AUTO,
            ))
        result = audit_repo.list_all(limit=3)
        assert len(result) == 3
