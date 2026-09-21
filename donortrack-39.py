# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: DonorTrack
def repair_data():
    """Repair simple data integrity issues: remove duplicates, fill missing values, and validate records."""
    contacts = [
        {"name": "John Doe", "email": "john@example.com", "phone": "1234567890", "gifts": [100, 200]},
        {"name": "Jane Smith", "email": "jane@example.com", "phone": "9876543210", "gifts": [50, 150]},
        {"name": "John Doe", "email": "john@example.com", "phone": "1234567890", "gifts": [100, 200]},
        {"name": "Bob Johnson", "email": "bob@example.com", "phone": "5555555555", "gifts": []},
        {"name": "Alice Brown", "email": "", "phone": "3333333333", "gifts": [75]},
    ]

    seen = set()
    repaired_contacts = []
    for contact in contacts:
        if contact["name"] in seen:
            continue
        seen.add(contact["name"])
        if not contact["email"]:
            contact["email"] = "unknown@example.com"
        if not contact["phone"]:
            contact["phone"] = "0000000000"
        if "gifts" not in contact:
            contact["gifts"] = []
        repaired_contacts.append(contact)

    print("Repaired contacts:", repaired_contacts)
    return repaired_contacts
