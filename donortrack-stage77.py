# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: DonorTrack
def format_gift_summary(gift):
    amount = gift.get("amount", 0)
    currency = gift.get("currency", "USD")
    return f"{amount} {currency}"


def calculate_total_by_status(gifts, status):
    total = 0
    for gift in gifts:
        if gift.get("status") == status:
            total += gift.get("amount", 0)
    return total


def find_matching_contacts(contacts, keyword):
    matches = []
    for contact in contacts:
        name = contact.get("name", "").lower()
        if keyword.lower() in name:
            matches.append(contact)
    return matches


def summarize_campaign(campaign):
    name = campaign.get("name", "")
    goal = campaign.get("goal", 0)
    raised = calculate_total_by_status(campaign.get("gifts", []), "pledged")
    return f"{name}: {raised}/{goal}"


def count_gifts_by_year(gifts):
    years = {}
    for gift in gifts:
        year = gift.get("year")
        if year:
            years[year] = years.get(year, 0) + 1
    return years


def build_thank_you_message(contact, gift):
    name = contact.get("name", "Dear Donor")
    message = f"Dear {name},\n\nThank you for your generous gift of {format_gift_summary(gift)}.\n\nWith gratitude,\nThe DonorTrack Team"
    return message


def is_duplicate_contact(contacts, new_contact):
    name = new_contact.get("name", "")
    for contact in contacts:
        if contact.get("name", "") == name:
            return True
    return False


def get_donation_history(contact_id, gifts):
    history = []
    for gift in gifts:
        if gift.get("contact_id") == contact_id:
            history.append(gift)
    history.sort(key=lambda g: g.get("date", ""), reverse=True)
    return history
