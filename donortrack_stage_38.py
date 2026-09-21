# === Stage 38: Add data integrity checks for broken references ===
# Project: DonorTrack
def check_references(db):
    """Verify that every foreign-key reference in all tables points to an existing row."""
    tables = ["contacts", "gifts", "campaigns", "thankyou_notes"]
    for t in tables:
        col = t + "_id"
        ref_table = {
            "contacts": "contacts",
            "gifts": "contacts",
            "campaigns": "campaigns",
            "thankyou_notes": "contacts"
        }[t]
        refs = [r for r in db[t] if r[col] is not None]
        for r in refs:
            if r[col] not in db[ref_table]:
                raise ValueError(f"Broken reference in {t}: {r[col]} not in {ref_table}")
