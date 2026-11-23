# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: DonorTrack
def self_check():
    errors = []
    for name, contact in contacts.items():
        if not isinstance(contact, dict):
            errors.append(f"contact {name} is not a dict")
        if not contact.get("email"):
            errors.append(f"contact {name} has no email")
    for gift in gifts:
        if gift.get("amount") <= 0:
            errors.append(f"gift has non-positive amount")
    for campaign in campaigns:
        if not campaign.get("name"):
            errors.append("campaign has no name")
    for note in thank_you_notes:
        if not note.get("to") or not note.get("message"):
            errors.append("thank-you note missing fields")
    if errors:
        raise SystemExit("self-check failed:\n" + "\n".join(errors))
    sample = sample_contact(1)
    if sample is None:
        raise SystemExit("sample_contact returned None")
    total = total_gifts()
    if total <= 0:
        raise SystemExit("total_gifts returned non-positive")
    for name in sample:
        print(f"contact: {name}")
    print(f"total gifts: {total}")
    print("self-check passed")
