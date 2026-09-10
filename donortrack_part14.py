# === Stage 14: Add file load support with fallback demo data ===
# Project: DonorTrack
def load_data(path):
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
    else:
        data = {
            "contacts": [
                {"id": 1, "name": "Alice Johnson", "email": "alice@example.com", "phone": "555-0101"},
                {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "phone": "555-0102"},
            ],
            "gifts": [
                {"id": 1, "contact_id": 1, "amount": 500.00, "date": "2024-01-15"},
                {"id": 2, "contact_id": 2, "amount": 250.00, "date": "2024-02-20"},
            ],
            "campaigns": [
                {"id": 1, "name": "Spring Fundraiser", "goal": 10000, "raised": 3500, "start_date": "2024-03-01"},
            ],
            "thank_you_notes": [
                {"id": 1, "contact_id": 1, "gift_id": 1, "message": "Thank you for your generous donation!", "date": "2024-01-16"},
            ],
        }
    return data
