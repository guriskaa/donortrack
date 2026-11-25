# === Stage 83: Add regression tests for the final demo workflow ===
# Project: DonorTrack
def run_final_demo_workflow():
    contacts = {
        "alice@example.com": {"name": "Alice", "gifts": [], "thankyou_notes": []},
        "bob@example.com": {"name": "Bob", "gifts": [], "thankyou_notes": []},
    }
    campaigns = {"spring": {"name": "Spring Gala", "goal": 10000, "raised": 0}}
    gifts = []
    notes = []

    def add_gift(email, amount, campaign=None):
        if email not in contacts:
            raise ValueError("unknown donor")
        if campaign is None or campaign not in campaigns:
            raise ValueError("unknown campaign")
        gifts.append({"email": email, "amount": amount, "campaign": campaign})
        contacts[email]["gifts"].append(amount)

    def send_thank_you(email, campaign):
        if email not in contacts:
            raise ValueError("unknown donor")
        if campaign not in campaigns:
            raise ValueError("unknown campaign")
        notes.append({"email": email, "campaign": campaign})
        contacts[email]["thankyou_notes"].append(campaign)

    add_gift("alice@example.com", 100, "spring")
    add_gift("bob@example.com", 250, "spring")
    campaigns["spring"]["raised"] = sum(g["amount"] for g in gifts if g["campaign"] == "spring")
    send_thank_you("alice@example.com", "spring")
    send_thank_you("bob@example.com", "spring")
    assert contacts["alice@example.com"]["gifts"] == [100]
    assert contacts["bob@example.com"]["gifts"] == [250]
    assert contacts["alice@example.com"]["thankyou_notes"] == ["spring"]
    assert contacts["bob@example.com"]["thankyou_notes"] == ["spring"]
    assert campaigns["spring"]["raised"] == 350
    assert len(notes) == 2
    return True
