from enum import Enum


class MasteryStatus(str, Enum):
    NOT_ATTEMPTED = "not_attempted"
    IN_PROGRESS = "in_progress"
    MASTERED = "mastered"


class FlagSource(str, Enum):
    AUTO = "auto"
    INSTRUCTOR = "instructor"


class SubmissionStatus(str, Enum):
    PENDING = "pending"
    EVALUATED = "evaluated"
    NEEDS_REVIEW = "needs_review"
