# === Stage 27: Add monthly summary calculations ===
# Project: DonorTrack
def monthly_summary(db):
    """Return a dict of month->total_gifts for the current year."""
    import sqlite3
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT strftime('%Y-%m', date) as month, SUM(amount) as total FROM gifts GROUP BY month ORDER BY month")
    rows = cur.fetchall()
    summary = {}
    for row in rows:
        summary[row[0]] = row[1]
    conn.close()
    return summary
