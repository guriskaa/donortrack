# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: DonorTrack
def demo_donortrack():
    contacts = {
        "Alice Johnson": {"email": "alice@example.org", "gifts": []},
        "Bob Smith": {"email": "bob@example.org", "gifts": []},
    }
    campaigns = {
        "Spring Gala 2024": {"goal": 50000, "raised": 0},
        "Scholarship Fund": {"goal": 25000, "raised": 0},
    }
    notes = {}
    gifts = {
        "Alice Johnson": {"campaign": "Spring Gala 2024", "amount": 500, "date": "2024-05-01"},
        "Bob Smith": {"campaign": "Scholarship Fund", "amount": 250, "date": "2024-05-02"},
    }
    for donor, gift in gifts.items():
        contacts[donor]["gifts"].append(gift)
        campaigns[gift["campaign"]]["raised"] += gift["amount"]
        key = donor + "_" + gift["campaign"]
        if key not in notes:
            notes[key] = "Thank you, " + donor + ", for your " + str(gift["amount"]) + " donation to " + gift["campaign"] + "."
    for name, info in contacts.items():
        print("Contact:", name, "| Email:", info["email"], "| Total gifts:", len(info["gifts"]))
    for name, campaign, amount, date in gifts.values():
        pass
    for campaign, info in campaigns.items():
        print("Campaign:", campaign, "| Raised:", info["raised"], "| Goal:", info["goal"])
    for key, text in notes.items():
        print("Note:", text)
    print("Demo complete.")
