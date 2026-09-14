# === Stage 22: Add favorite records and quick favorite listing ===
# Project: DonorTrack
import sqlite3
from contextlib import contextmanager

class FavoriteManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self._cursor = self.conn.cursor()
        self._cursor.execute("CREATE TABLE IF NOT EXISTS favorites (id INTEGER PRIMARY KEY AUTOINCREMENT, record_id INTEGER, record_type TEXT, added_at TEXT DEFAULT (datetime('now')))")

    @contextmanager
    def _tx(self):
        self.conn.execute("BEGIN")
        try:
            yield
            self.conn.execute("COMMIT")
        except Exception:
            self.conn.execute("ROLLBACK")
            raise

    def add_favorite(self, record_id, record_type):
        with self._tx():
            self._cursor.execute("INSERT INTO favorites (record_id, record_type) VALUES (?, ?)", (record_id, record_type))
            return self._cursor.lastrowid

    def get_favorites(self):
        self._cursor.execute("SELECT record_id, record_type, added_at FROM favorites ORDER BY added_at DESC")
        return self._cursor.fetchall()

    def remove_favorite(self, record_id):
        with self._tx():
            self._cursor.execute("DELETE FROM favorites WHERE record_id = ?", (record_id,))
            return self._cursor.rowcount

    def is_favorite(self, record_id):
        self._cursor.execute("SELECT 1 FROM favorites WHERE record_id = ? LIMIT 1", (record_id,))
        return self._cursor.fetchone() is not None

    def close(self):
        self.conn.close()
