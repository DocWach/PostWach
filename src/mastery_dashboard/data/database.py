import sqlite3
from pathlib import Path
from typing import Optional

_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS submissions (
    id TEXT PRIMARY KEY,
    student_id TEXT NOT NULL REFERENCES students(id),
    outcome_id TEXT NOT NULL,
    score REAL NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    submitted_at TEXT NOT NULL DEFAULT (datetime('now')),
    evaluated_at TEXT,
    evaluator_notes TEXT
);

CREATE TABLE IF NOT EXISTS mastery_records (
    student_id TEXT NOT NULL REFERENCES students(id),
    outcome_id TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'not_attempted',
    flag_source TEXT NOT NULL DEFAULT 'auto',
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT,
    PRIMARY KEY (student_id, outcome_id)
);

CREATE TABLE IF NOT EXISTS audit_log (
    id TEXT PRIMARY KEY,
    student_id TEXT NOT NULL REFERENCES students(id),
    outcome_id TEXT NOT NULL,
    old_status TEXT NOT NULL,
    new_status TEXT NOT NULL,
    source TEXT NOT NULL,
    timestamp TEXT NOT NULL DEFAULT (datetime('now')),
    reason TEXT
);

CREATE INDEX IF NOT EXISTS idx_submissions_student ON submissions(student_id);
CREATE INDEX IF NOT EXISTS idx_submissions_outcome ON submissions(outcome_id);
CREATE INDEX IF NOT EXISTS idx_mastery_student ON mastery_records(student_id);
CREATE INDEX IF NOT EXISTS idx_audit_student ON audit_log(student_id);
"""


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    if db_path is None:
        db_path = str(Path(__file__).parent / "mastery.db")
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.row_factory = sqlite3.Row
    return conn


def get_memory_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    conn.execute("PRAGMA foreign_keys=ON")
    conn.row_factory = sqlite3.Row
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(_SCHEMA_SQL)
    conn.commit()
