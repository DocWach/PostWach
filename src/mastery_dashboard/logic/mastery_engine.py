import uuid
from datetime import datetime
from typing import Optional

from ..config.schema import CourseConfig
from ..data.repositories import AuditRepo, MasteryRepo, SubmissionRepo
from ..models.domain import AuditEntry, MasteryRecord, Submission
from ..models.enums import FlagSource, MasteryStatus, SubmissionStatus
from .evaluators import get_evaluator

# Valid auto transitions
_VALID_TRANSITIONS = {
    MasteryStatus.NOT_ATTEMPTED: {MasteryStatus.IN_PROGRESS, MasteryStatus.MASTERED},
    MasteryStatus.IN_PROGRESS: {MasteryStatus.MASTERED},
    MasteryStatus.MASTERED: set(),  # No auto demotion
}


class MasteryEngine:
    def __init__(
        self,
        config: CourseConfig,
        mastery_repo: MasteryRepo,
        submission_repo: SubmissionRepo,
        audit_repo: AuditRepo,
    ):
        self.config = config
        self.mastery = mastery_repo
        self.submissions = submission_repo
        self.audit = audit_repo

    def process_submission(self, submission: Submission) -> MasteryRecord:
        """Evaluate a submission and update mastery status if appropriate."""
        outcome = self.config.get_outcome(submission.outcome_id)
        if outcome is None:
            raise ValueError(f"Unknown outcome: {submission.outcome_id}")

        evaluator = get_evaluator(outcome.mastery_criteria.type)
        new_status = evaluator.evaluate(submission.score, outcome.mastery_criteria)

        current = self.mastery.get(submission.student_id, submission.outcome_id)
        old_status = current.status if current else MasteryStatus.NOT_ATTEMPTED

        # Only advance, never demote automatically — use transition table
        if new_status not in _VALID_TRANSITIONS.get(old_status, set()):
            self.submissions.update_status(
                submission.id, SubmissionStatus.EVALUATED, datetime.now()
            )
            return current or MasteryRecord(
                student_id=submission.student_id,
                outcome_id=submission.outcome_id,
                status=old_status,
            )

        # Advance mastery
        record = MasteryRecord(
            student_id=submission.student_id,
            outcome_id=submission.outcome_id,
            status=new_status,
            flag_source=FlagSource.AUTO,
            updated_at=datetime.now(),
        )
        self.mastery.upsert(record)

        self.audit.create(AuditEntry(
            id=str(uuid.uuid4()),
            student_id=submission.student_id,
            outcome_id=submission.outcome_id,
            old_status=old_status,
            new_status=new_status,
            source=FlagSource.AUTO,
            timestamp=datetime.now(),
            reason=f"Submission {submission.id} scored {submission.score}",
        ))

        self.submissions.update_status(
            submission.id, SubmissionStatus.EVALUATED, datetime.now()
        )
        return record

    def instructor_override(
        self,
        student_id: str,
        outcome_id: str,
        new_status: MasteryStatus,
        reason: Optional[str] = None,
    ) -> MasteryRecord:
        """Instructor can set any status (including demotions)."""
        current = self.mastery.get(student_id, outcome_id)
        old_status = current.status if current else MasteryStatus.NOT_ATTEMPTED

        record = MasteryRecord(
            student_id=student_id,
            outcome_id=outcome_id,
            status=new_status,
            flag_source=FlagSource.INSTRUCTOR,
            updated_at=datetime.now(),
            notes=reason,
        )
        self.mastery.upsert(record)

        self.audit.create(AuditEntry(
            id=str(uuid.uuid4()),
            student_id=student_id,
            outcome_id=outcome_id,
            old_status=old_status,
            new_status=new_status,
            source=FlagSource.INSTRUCTOR,
            timestamp=datetime.now(),
            reason=reason or "Instructor override",
        ))

        return record
