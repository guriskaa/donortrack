# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: DonorTrack
def seed_demo_data(db):
    from collections import defaultdict
    db["contacts"] = [
        {"id": 1, "name": "Alice Johnson", "email": "alice@example.com", "phone": "555-0101"},
        {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "phone": "555-0102"},
        {"id": 3, "name": "Carol White", "email": "carol@example.com", "phone": "555-0103"},
    ]
    db["campaigns"] = [
        {"id": 1, "name": "Winter Gala 2024", "goal": 100000},
        {"id": 2, "name": "Community Scholarship Fund", "goal": 50000},
    ]
    db["gifts"] = [
        {"id": 1, "contact_id": 1, "campaign_id": 1, "amount": 2500, "date": "2024-01-15"},
        {"id": 2, "contact_id": 2, "campaign_id": 1, "amount": 5000, "date": "2024-01-16"},
        {"id": 3, "contact_id": 3, "campaign_id": 2, "amount": 1000, "date": "2024-02-01"},
    ]
    db["thank_you_notes"] = [
        {"id": 1, "gift_id": 1, "contact_id": 1, "message": "Thank you for your generous support of the Winter Gala.", "sent": "2024-01-20"},
        {"id": 2, "gift_id": 2, "contact_id": 2, "message": "Your contribution makes a real difference. Thank you!", "sent": "2024-01-21"},
    ]
    db["campaign_progress"] = defaultdict(int)
    for gift in db["gifts"]:
        db["campaign_progress"][gift["campaign_id"]] += gift["amount"]
