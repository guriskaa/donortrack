# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: DonorTrack
import sqlite3
from contextlib import contextmanager

DB_PATH = "donortrack.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT
            );
            CREATE TABLE IF NOT EXISTS gifts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contact_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                currency TEXT DEFAULT 'USD',
                date TEXT,
                FOREIGN KEY (contact_id) REFERENCES contacts(id)
            );
            CREATE TABLE IF NOT EXISTS campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                start_date TEXT,
                end_date TEXT
            );
            CREATE TABLE IF NOT EXISTS thank_you_notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gift_id INTEGER NOT NULL,
                message TEXT,
                sent_date TEXT,
                FOREIGN KEY (gift_id) REFERENCES gifts(id)
            );
        """)
