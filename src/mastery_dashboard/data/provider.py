import sqlite3
from typing import Dict, List, Optional, Set

from ..config.schema import CourseConfig
from ..logic.grade_engine import compute_grade, compute_next_grade
from ..models.domain import (
    BlockProgress,
    ClassOutcomeStats,
    StudentGradeView,
    Submission,
)
from ..models.enums import MasteryStatus
from .repositories import AuditRepo, MasteryRepo, StudentRepo, SubmissionRepo


class MasteryDataProvider:
    def __init__(self, conn: sqlite3.Connection, config: CourseConfig):
        self.config = config
        self.students = StudentRepo(conn)
        self.submissions = SubmissionRepo(conn)
        self.mastery = MasteryRepo(conn)
        self.audit = AuditRepo(conn)

    def get_student_grade_view(self, student_id: str) -> Optional[StudentGradeView]:
        student = self.students.get(student_id)
        if not student:
            return None

        records = self.mastery.list_by_student(student_id)
        mastery_map: Dict[str, MasteryStatus] = {
            r.outcome_id: r.status for r in records
        }

        block_progress = []
        completed_blocks: Set[str] = set()

        for block in self.config.blocks:
            mastered = 0
            in_progress = 0
            not_attempted = 0
            for outcome in block.outcomes:
                status = mastery_map.get(outcome.id, MasteryStatus.NOT_ATTEMPTED)
                if status == MasteryStatus.MASTERED:
                    mastered += 1
                elif status == MasteryStatus.IN_PROGRESS:
                    in_progress += 1
                else:
                    not_attempted += 1

            bp = BlockProgress(
                block_id=block.id,
                block_name=block.name,
                total_outcomes=len(block.outcomes),
                mastered=mastered,
                in_progress=in_progress,
                not_attempted=not_attempted,
            )
            block_progress.append(bp)
            if bp.is_complete:
                completed_blocks.add(block.id)

        current_grade = compute_grade(completed_blocks, self.config.grade_rules)
        next_info = compute_next_grade(completed_blocks, self.config.grade_rules)
        next_grade = next_info[0] if next_info else None

        outcomes_needed = None
        if next_info:
            _, needed_blocks = next_info
            outcomes_needed = []
            for bid in needed_blocks:
                if bid not in completed_blocks:
                    for oid in self.config.outcome_ids_for_block(bid):
                        status = mastery_map.get(oid, MasteryStatus.NOT_ATTEMPTED)
                        if status != MasteryStatus.MASTERED:
                            outcomes_needed.append(oid)

        return StudentGradeView(
            student=student,
            current_grade=current_grade,
            completed_blocks=completed_blocks,
            block_progress=block_progress,
            mastery_records=mastery_map,
            next_grade=next_grade,
            outcomes_to_next_grade=outcomes_needed,
        )

    def get_class_outcome_stats(self) -> List[ClassOutcomeStats]:
        students = self.students.list_all()
        if not students:
            return []

        student_ids = [s.id for s in students]
        outcome_ids = self.config.all_outcome_ids()
        matrix = self.mastery.get_matrix(student_ids, outcome_ids)
        total = len(students)

        stats = []
        for block in self.config.blocks:
            for outcome in block.outcomes:
                mastered = sum(
                    1 for sid in student_ids
                    if matrix.get(sid, {}).get(outcome.id) == MasteryStatus.MASTERED
                )
                in_prog = sum(
                    1 for sid in student_ids
                    if matrix.get(sid, {}).get(outcome.id) == MasteryStatus.IN_PROGRESS
                )
                stats.append(ClassOutcomeStats(
                    outcome_id=outcome.id,
                    outcome_name=outcome.name,
                    block_id=block.id,
                    total_students=total,
                    mastered_count=mastered,
                    in_progress_count=in_prog,
                    not_attempted_count=total - mastered - in_prog,
                ))
        return stats

    def get_grade_distribution(self) -> Dict[str, int]:
        students = self.students.list_all()
        dist: Dict[str, int] = {"No Grade": 0}
        for rule in self.config.grade_rules:
            dist[rule.grade] = 0

        for s in students:
            view = self.get_student_grade_view(s.id)
            if view and view.current_grade:
                dist[view.current_grade] = dist.get(view.current_grade, 0) + 1
            else:
                dist["No Grade"] += 1
        return dist

    def get_student_submissions(self, student_id: str) -> List[Submission]:
        return self.submissions.list_by_student(student_id)

    def get_pending_submissions(self) -> List[Submission]:
        return self.submissions.list_pending()
