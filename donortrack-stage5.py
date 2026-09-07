# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: DonorTrack
def update_contact(contact_id, **kwargs):
    """Update a contact's fields; raise KeyError if contact_id missing."""
    contacts = load_contacts()
    if contact_id not in contacts:
        raise KeyError(f"Contact '{contact_id}' not found")
    for field, value in kwargs.items():
        if field not in contacts[contact_id]:
            raise ValueError(f"Unknown field '{field}' for contact")
    contacts[contact_id].update(kwargs)
    save_contacts(contacts)
