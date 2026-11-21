# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: DonorTrack
def validate_records(contacts, gifts, campaigns, notes):
    warnings = []
    errors = []
    contact_ids = set()
    for c in contacts:
        cid = c.get("id")
        contact_ids.add(cid)
        if not cid:
            errors.append("contact missing id")
        if not c.get("name"):
            warnings.append("contact with missing name")
        if c.get("email") and not c["email"].strip():
            warnings.append("contact with blank email")
        if c.get("phone") and not c["phone"].strip():
            warnings.append("contact with blank phone")
    gift_counts = {}
    for g in gifts:
        gid = g.get("id")
        gift_counts[gid] = gift_counts.get(gid, 0) + 1
        if gid not in contact_ids:
            warnings.append("gift linked to unknown contact id")
        if g.get("amount") is not None and float(g["amount"]) <= 0:
            errors.append("gift with non-positive amount")
        if g.get("date") and not isinstance(g["date"], str):
            warnings.append("gift with non-string date")
    for camp in campaigns:
        if not camp.get("name"):
            warnings.append("campaign with missing name")
    for note in notes:
        if not note.get("contact_id") or note["contact_id"] not in contact_ids:
            warnings.append("note linked to unknown contact id")
        if not note.get("message"):
            warnings.append("thank-you note with missing message")
    for cid, count in gift_counts.items():
        if count > 1:
            warnings.append("duplicate gift id")
    return warnings, errors
