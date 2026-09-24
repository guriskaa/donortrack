# === Stage 46: Add a schema version field and migration helper ===
# Project: DonorTrack
SCHEMA_VERSION = 2


def migrate_to_v2(db_path):
    """Upgrade schema: add 'campaign_id' column to gifts table."""
    import sqlite3
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("ALTER TABLE gifts ADD COLUMN campaign_id TEXT")
        conn.commit()
    except sqlite3.OperationalError:
        pass
    finally:
        conn.close()
    return SCHEMA_VERSION
