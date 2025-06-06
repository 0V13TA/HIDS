import sqlite3
from datetime import datetime

DB_PATH = "/secure/location/hids_hashes.db"


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS file_hashes (
                path TEXT PRIMARY KEY,
                hash TEXT NOT NULL,
                last_checked TIMESTAMP
            )
        """
        )


def write_hash(path, hash_value):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "REPLACE INTO file_hashes (path, hash, last_checked) VALUES (?, ?, ?)",
            (path, hash_value, datetime.now()),
        )


def get_hash(path):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT hash FROM file_hashes WHERE path = ?", (path,))
        row = cur.fetchone()
        return row[0] if row else None


def get_all_hashes() -> dict[str, str]:
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT path, hash FROM file_hashes")
        return {row[0]: row[1] for row in cur.fetchall()}
