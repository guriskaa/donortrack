# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: DonorTrack
def run_demo():
    contacts = {
        "1001": {"name": "Alice Chen", "email": "alice@example.org"},
        "1002": {"name": "Bob Diaz", "email": "bob@example.org"},
    }
    campaigns = {
        "c1": {"name": "Spring Gala", "goal": 100000, "raised": 0},
    }
    gifts = {
        "g1": {"contact_id": "1001", "campaign_id": "c1", "amount": 500, "date": "2024-01-15"},
        "g2": {"contact_id": "1002", "campaign_id": "c1", "amount": 300, "date": "2024-01-16"},
    }
    notes = {
        "g1": {"gift_id": "g1", "text": "Thank you for your generous support!"},
        "g2": {"gift_id": "g2", "text": "We truly appreciate your contribution."},
    }

    total = sum(g["amount"] for g in gifts.values())
    print("Total gifts:", total)
    print("Campaign c1 raised:", sum(g["amount"] for g in gifts.values() if g["campaign_id"] == "c1"))
    for g in gifts:
        note = notes.get(g, {}).get("text", "No note sent.")
        contact = contacts.get(gifts[g]["contact_id"], {}).get("name", "Unknown")
        print("Gift", g, "->", contact, ":", note)

    print("Campaign c1 reached goal:", campaigns["c1"]["raised"] >= campaigns["c1"]["goal"])

run_demo()
