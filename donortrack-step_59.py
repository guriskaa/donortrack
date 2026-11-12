# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: DonorTrack
def enable_bulk_delete_confirmation(db):
    with db.cursor() as cur:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='donors'")
        if cur.fetchone():
            cur.execute("ALTER TABLE donors ADD COLUMN bulk_delete_guard INTEGER DEFAULT 0")
        db.commit()

def bulk_delete_donors(db, donor_ids, confirm=False):
    if not confirm:
        raise PermissionError("Confirm before bulk delete")
    placeholders = ",".join("?" for _ in donor_ids)
    with db.cursor() as cur:
        cur.execute(f"DELETE FROM donors WHERE id IN ({placeholders})", donor_ids)
        db.commit()
        return cur.rowcount

def confirm_bulk_delete(db, donor_ids):
    return input(f"Delete {len(donor_ids)} donor(s)? [y/N]: ").strip().lower() == "y"
