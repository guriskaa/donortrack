# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: DonorTrack
def archive_completed_records(db_path="donor.db"):
    """Move completed records older than 90 days to an archive table."""
    import sqlite3, datetime
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT id, gift_date FROM gifts WHERE status = 'completed' AND gift_date < date('now', '-90 days')")
    rows = c.fetchall()
    if not rows:
        return
    c.execute("CREATE TABLE IF NOT EXISTS gifts_archive (id INTEGER, gift_date TEXT)")
    for r in rows:
        c.execute("INSERT INTO gifts_archive (id, gift_date) VALUES (?, ?)", r)
    c.execute("DELETE FROM gifts WHERE id IN (SELECT id FROM gifts_archive)")
    conn.commit()
    conn.close()
    print(f"Archived {len(rows)} completed gift records.")
