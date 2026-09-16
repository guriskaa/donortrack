# === Stage 28: Add overdue item detection based on due dates ===
# Project: DonorTrack
def check_overdue_items(contacts, gifts):
    """Return a list of (contact_name, gift_id, due_date, days_overdue) for gifts past their due date."""
    overdue = []
    for gift in gifts:
        if gift.get("due_date") and gift.get("due_date") != "":
            due = datetime.strptime(gift["due_date"], "%Y-%m-%d")
            if due < datetime.now().date():
                contact = next((c for c in contacts if c["contact_id"] == gift["contact_id"]), {})
                overdue.append((contact.get("name", "Unknown"), gift["gift_id"], gift["due_date"], (datetime.now().date() - due).days))
    return overdue
