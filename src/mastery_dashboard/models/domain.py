from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Set

from .enums import FlagSource, MasteryStatus, SubmissionStatus


@dataclass
class Student:
    id: str
    name: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class Submission:
    id: str
    student_id: str
    outcome_id: str
    score: float
    status: SubmissionStatus
    submitted_at: datetime = field(default_factory=datetime.now)
    evaluated_at: Optional[datetime] = None
    evaluator_notes: Optional[str] = None


@dataclass
class MasteryRecord:
    student_id: str
    outcome_id: str
    status: MasteryStatus
    flag_source: FlagSource = FlagSource.AUTO
    updated_at: datetime = field(default_factory=datetime.now)
    notes: Optional[str] = None


@dataclass
class AuditEntry:
    id: str
    student_id: str
    outcome_id: str
    old_status: MasteryStatus
    new_status: MasteryStatus
    source: FlagSource
    timestamp: datetime = field(default_factory=datetime.now)
    reason: Optional[str] = None


# Computed views

@dataclass
class BlockProgress:
    block_id: str
    block_name: str
    total_outcomes: int
    mastered: int
    in_progress: int
    not_attempted: int

    @property
    def completion_ratio(self) -> float:
        return self.mastered / self.total_outcomes if self.total_outcomes > 0 else 0.0

    @property
    def is_complete(self) -> bool:
        return self.mastered == self.total_outcomes


@dataclass
class StudentGradeView:
    student: Student
    current_grade: Optional[str]
    completed_blocks: Set[str]
    block_progress: List[BlockProgress]
    mastery_records: Dict[str, MasteryStatus]  # outcome_id -> status
    next_grade: Optional[str] = None
    outcomes_to_next_grade: Optional[List[str]] = None


@dataclass
class ClassOutcomeStats:
    outcome_id: str
    outcome_name: str
    block_id: str
    total_students: int
    mastered_count: int
    in_progress_count: int
    not_attempted_count: int

    @property
    def mastery_rate(self) -> float:
        return self.mastered_count / self.total_students if self.total_students > 0 else 0.0
