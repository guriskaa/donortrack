# === Stage 67: Add a function that returns key project metrics ===
# Project: DonorTrack
def get_project_metrics(db):
    """Return key project metrics for DonorTrack."""
    contacts = db["contacts"]
    gifts = db["gifts"]
    campaigns = db["campaigns"]
    notes = db["notes"]

    total_donations = sum(row["amount"] for row in gifts)
    active_donors = len({row["donor_id"] for row in gifts if row["amount"] > 0})
    campaigns_running = sum(1 for c in campaigns if c["status"] == "active")
    notes_sent = len(notes)
    recent_gifts = [row for row in gifts if row["date"] >= "2023-01-01"]

    return {
        "total_contacts": len(contacts),
        "total_gifts": len(gifts),
        "total_donations": total_donations,
        "active_donors": active_donors,
        "campaigns_running": campaigns_running,
        "thank_you_notes_sent": notes_sent,
        "gifts_this_year": len(recent_gifts),
    }
