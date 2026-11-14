# === Stage 64: Add validation for relationship references ===
# Project: DonorTrack
VALID_RELATIONSHIPS = ("friend", "family", "colleague", "mentor", "volunteer", "donor", "board_member", "other")


def validate_relationship(relationship, contact_id=None):
    if relationship is None:
        return False, "Relationship is required."
    if relationship.strip() == "":
        return False, "Relationship cannot be empty."
    if relationship not in VALID_RELATIONSHIPS:
        return False, "Invalid relationship. Choose from: " + ", ".join(VALID_RELATIONSHIPS)
    if contact_id is not None:
        contacts = get_contacts()
        if contact_id not in [c["id"] for c in contacts]:
            return False, "Reference contact_id does not exist."
    return True, ""


def validate_relationships(contacts):
    invalid = []
    for contact in contacts:
        ok, msg = validate_relationship(contact.get("relationship"), contact.get("contact_id"))
        if not ok:
            invalid.append((contact.get("id"), msg))
    return invalid


def update_relationship(contact_id, relationship):
    contacts = get_contacts()
    for contact in contacts:
        if contact["id"] == contact_id:
            ok, msg = validate_relationship(relationship, contact.get("contact_id"))
            if not ok:
                return False, msg
            contact["relationship"] = relationship
            save_contacts(contacts)
            return True, ""
    return False, "Contact not found."
