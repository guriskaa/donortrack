# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: DonorTrack
def upcoming_items(contacts, gifts, campaigns, days_away=7):
    """Return upcoming items within the next N days."""
    today = datetime.date.today()
    upcoming = []
    for contact in contacts:
        if contact.get("next_follow_up", 0) > 0:
            due = today + timedelta(days=int(contact["next_follow_up"]))
            if due - today <= timedelta(days=days_away):
                upcoming.append({"type": "follow_up", "name": contact["name"], "due": due})
    for gift in gifts:
        if gift.get("thank_you_by", 0) > 0:
            due = today + timedelta(days=int(gift["thank_you_by"]))
            if due - today <= timedelta(days=days_away):
                upcoming.append({"type": "thank_you", "name": gift["donor"], "due": due})
    for campaign in campaigns:
        if campaign.get("start_date") and campaign.get("end_date"):
            start = datetime.date.fromisoformat(campaign["start_date"])
            end = datetime.date.fromisoformat(campaign["end_date"])
            if start <= today <= end and (end - today) <= timedelta(days=days_away):
                upcoming.append({"type": "campaign", "name": campaign["name"], "due": end})
    upcoming.sort(key=lambda x: x["due"])
    return upcoming
