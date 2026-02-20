import sqlite3
import uuid
from datetime import datetime
from typing import Dict, List, Optional

from ..models.domain import AuditEntry, MasteryRecord, Student, Submission
from ..models.enums import FlagSource, MasteryStatus, SubmissionStatus


class StudentRepo:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create(self, student: Student) -> Student:
        self.conn.execute(
            "INSERT INTO students (id, name, email, created_at) VALUES (?, ?, ?, ?)",
            (student.id, student.name, student.email, student.created_at.isoformat()),
        )
        self.conn.commit()
        return student

    def get(self, student_id: str) -> Optional[Student]:
        row = self.conn.execute(
            "SELECT * FROM students WHERE id = ?", (student_id,)
        ).fetchone()
        if not row:
            return None
        return Student(
            id=row["id"],
            name=row["name"],
            email=row["email"],
            created_at=datetime.fromisoformat(row["created_at"]),
        )

    def list_all(self) -> List[Student]:
        rows = self.conn.execute("SELECT * FROM students ORDER BY name").fetchall()
        return [
            Student(
                id=r["id"], name=r["name"], email=r["email"],
                created_at=datetime.fromisoformat(r["created_at"]),
            )
            for r in rows
        ]

    def delete(self, student_id: str) -> bool:
        cursor = self.conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.conn.commit()
        return cursor.rowcount > 0


class SubmissionRepo:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create(self, sub: Submission) -> Submission:
        self.conn.execute(
            """INSERT INTO submissions
               (id, student_id, outcome_id, score, status, submitted_at, evaluated_at, evaluator_notes)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                sub.id, sub.student_id, sub.outcome_id, sub.score,
                sub.status.value, sub.submitted_at.isoformat(),
                sub.evaluated_at.isoformat() if sub.evaluated_at else None,
                sub.evaluator_notes,
            ),
        )
        self.conn.commit()
        return sub

    def get(self, submission_id: str) -> Optional[Submission]:
        row = self.conn.execute(
            "SELECT * FROM submissions WHERE id = ?", (submission_id,)
        ).fetchone()
        if not row:
            return None
        return self._row_to_submission(row)

    def list_by_student(self, student_id: str) -> List[Submission]:
        rows = self.conn.execute(
            "SELECT * FROM submissions WHERE student_id = ? ORDER BY submitted_at DESC",
            (student_id,),
        ).fetchall()
        return [self._row_to_submission(r) for r in rows]

    def list_pending(self) -> List[Submission]:
        rows = self.conn.execute(
            "SELECT * FROM submissions WHERE status = ? ORDER BY submitted_at",
            (SubmissionStatus.PENDING.value,),
        ).fetchall()
        return [self._row_to_submission(r) for r in rows]

    def update_status(self, submission_id: str, status: SubmissionStatus,
                      evaluated_at: Optional[datetime] = None,
                      notes: Optional[str] = None) -> bool:
        cursor = self.conn.execute(
            """UPDATE submissions SET status = ?, evaluated_at = ?, evaluator_notes = ?
               WHERE id = ?""",
            (status.value, evaluated_at.isoformat() if evaluated_at else None,
             notes, submission_id),
        )
        self.conn.commit()
        return cursor.rowcount > 0

    def _row_to_submission(self, row) -> Submission:
        return Submission(
            id=row["id"],
            student_id=row["student_id"],
            outcome_id=row["outcome_id"],
            score=row["score"],
            status=SubmissionStatus(row["status"]),
            submitted_at=datetime.fromisoformat(row["submitted_at"]),
            evaluated_at=datetime.fromisoformat(row["evaluated_at"]) if row["evaluated_at"] else None,
            evaluator_notes=row["evaluator_notes"],
        )


class MasteryRepo:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def upsert(self, record: MasteryRecord) -> MasteryRecord:
        self.conn.execute(
            """INSERT INTO mastery_records (student_id, outcome_id, status, flag_source, updated_at, notes)
               VALUES (?, ?, ?, ?, ?, ?)
               ON CONFLICT(student_id, outcome_id)
               DO UPDATE SET status=excluded.status, flag_source=excluded.flag_source,
                             updated_at=excluded.updated_at, notes=excluded.notes""",
            (
                record.student_id, record.outcome_id, record.status.value,
                record.flag_source.value, record.updated_at.isoformat(), record.notes,
            ),
        )
        self.conn.commit()
        return record

    def get(self, student_id: str, outcome_id: str) -> Optional[MasteryRecord]:
        row = self.conn.execute(
            "SELECT * FROM mastery_records WHERE student_id = ? AND outcome_id = ?",
            (student_id, outcome_id),
        ).fetchone()
        if not row:
            return None
        return self._row_to_record(row)

    def list_by_student(self, student_id: str) -> List[MasteryRecord]:
        rows = self.conn.execute(
            "SELECT * FROM mastery_records WHERE student_id = ?", (student_id,)
        ).fetchall()
        return [self._row_to_record(r) for r in rows]

    def get_matrix(self, student_ids: List[str], outcome_ids: List[str]) -> Dict[str, Dict[str, MasteryStatus]]:
        """Return {student_id: {outcome_id: status}} for the given IDs."""
        if not student_ids or not outcome_ids:
            return {}
        placeholders_s = ",".join("?" for _ in student_ids)
        placeholders_o = ",".join("?" for _ in outcome_ids)
        rows = self.conn.execute(
            f"""SELECT student_id, outcome_id, status FROM mastery_records
                WHERE student_id IN ({placeholders_s}) AND outcome_id IN ({placeholders_o})""",
            student_ids + outcome_ids,
        ).fetchall()

        matrix: Dict[str, Dict[str, MasteryStatus]] = {
            sid: {oid: MasteryStatus.NOT_ATTEMPTED for oid in outcome_ids}
            for sid in student_ids
        }
        for r in rows:
            matrix[r["student_id"]][r["outcome_id"]] = MasteryStatus(r["status"])
        return matrix

    def _row_to_record(self, row) -> MasteryRecord:
        return MasteryRecord(
            student_id=row["student_id"],
            outcome_id=row["outcome_id"],
            status=MasteryStatus(row["status"]),
            flag_source=FlagSource(row["flag_source"]),
            updated_at=datetime.fromisoformat(row["updated_at"]),
            notes=row["notes"],
        )


class AuditRepo:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create(self, entry: AuditEntry) -> AuditEntry:
        self.conn.execute(
            """INSERT INTO audit_log (id, student_id, outcome_id, old_status, new_status, source, timestamp, reason)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                entry.id, entry.student_id, entry.outcome_id,
                entry.old_status.value, entry.new_status.value,
                entry.source.value, entry.timestamp.isoformat(), entry.reason,
            ),
        )
        self.conn.commit()
        return entry

    def list_by_student(self, student_id: str) -> List[AuditEntry]:
        rows = self.conn.execute(
            "SELECT * FROM audit_log WHERE student_id = ? ORDER BY timestamp DESC",
            (student_id,),
        ).fetchall()
        return [self._row_to_entry(r) for r in rows]

    def list_all(self, limit: int = 100) -> List[AuditEntry]:
        rows = self.conn.execute(
            "SELECT * FROM audit_log ORDER BY timestamp DESC LIMIT ?", (limit,)
        ).fetchall()
        return [self._row_to_entry(r) for r in rows]

    def _row_to_entry(self, row) -> AuditEntry:
        return AuditEntry(
            id=row["id"],
            student_id=row["student_id"],
            outcome_id=row["outcome_id"],
            old_status=MasteryStatus(row["old_status"]),
            new_status=MasteryStatus(row["new_status"]),
            source=FlagSource(row["source"]),
            timestamp=datetime.fromisoformat(row["timestamp"]),
            reason=row["reason"],
        )
