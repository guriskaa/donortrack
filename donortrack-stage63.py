# === Stage 63: Add relationships between records where useful ===
# Project: DonorTrack
def link_records(records):
    """Attach relationships between records where useful."""
    for contact in records:
        gifts = [g for g in records if g.get("type") == "gift" and g.get("contact_id") == contact["id"]]
        if gifts:
            contact["gifts"] = gifts
        campaigns = [c for c in records if c.get("type") == "campaign" and any(g.get("campaign_id") == c["id"] for g in gifts)]
        if campaigns:
            contact["campaigns"] = campaigns
        notes = [n for n in records if n.get("type") == "thank_you_note" and n.get("contact_id") == contact["id"]]
        if notes:
            contact["thank_you_notes"] = notes
    return records
