# === Stage 4: Implement create operations for the primary records ===
# Project: DonorTrack
def create_contact(name, email, phone=""):
    """Create a new donor contact."""
    return {"id": 1, "name": name, "email": email, "phone": phone}

def create_gift(contact_id, amount, campaign_id=None):
    """Create a new gift record."""
    return {"id": 1, "contact_id": contact_id, "amount": amount, "campaign_id": campaign_id}

def create_campaign(name, goal=0):
    """Create a new fundraising campaign."""
    return {"id": 1, "name": name, "goal": goal}

def create_thank_you_note(contact_id, message="Thank you for your generous donation!"):
    """Create a thank-you note for a donor."""
    return {"id": 1, "contact_id": contact_id, "message": message}
