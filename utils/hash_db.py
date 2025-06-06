import sqlite3
from datetime import datetime
from config import HIDS_HASHES_FILE


def init_db():
    with sqlite3.connect(HIDS_HASHES_FILE) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS file_hashes (
                path TEXT PRIMARY KEY,
                hash TEXT NOT NULL,
                last_checked TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS watch_directories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT NOT NULL UNIQUE,
                last_scanned TIMESTAMP
            );
        """
        )


def write_hash(path, hash_value):
    with sqlite3.connect(HIDS_HASHES_FILE) as conn:
        conn.execute(
            "REPLACE INTO file_hashes (path, hash, last_checked) VALUES (?, ?, ?)",
            (path, hash_value, datetime.now()),
        )


def get_hash(path):
    with sqlite3.connect(HIDS_HASHES_FILE) as conn:
        cur = conn.execute("SELECT hash FROM file_hashes WHERE path = ?", (path,))
        row = cur.fetchone()
        return row[0] if row else None


def get_all_hashes() -> dict[str, str]:
    with sqlite3.connect(HIDS_HASHES_FILE) as conn:
        cur = conn.execute("SELECT path, hash FROM file_hashes")
        return {row[0]: row[1] for row in cur.fetchall()}


def get_all_watch_directories() -> list[str]:
    with sqlite3.connect(HIDS_HASHES_FILE) as conn:
        cur = conn.execute("SELECT path FROM watch_directories")
        return [row[0] for row in cur.fetchall()]


def add_watch_directory(path: str):
    with sqlite3.connect(HIDS_HASHES_FILE) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO watch_directories (path, last_scanned) VALUES (?, ?)",
            (path, datetime.now()),
        )
        conn.commit()


def remove_watch_directory(path: str):
    with sqlite3.connect(HIDS_HASHES_FILE) as conn:
        conn.execute("DELETE FROM watch_directories WHERE path = ?", (path,))
        conn.commit()
