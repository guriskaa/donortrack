# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: DonorTrack
def format_gift_summary(gift):
    """Return a compact human-readable summary of a gift record."""
    return (
        f"{gift['gift_id']}: ${gift['amount']} "
        f"on {gift['gift_date']} "
        f"for campaign '{gift['campaign_name']}' "
        f"from {gift['donor_name']}"
    )


def find_gifts_by_campaign(gifts, campaign_name):
    """Return all gifts that belong to the given campaign name."""
    return [gift for gift in gifts if gift['campaign_name'] == campaign_name]


def total_amount_for_campaign(gifts, campaign_name):
    """Return the summed gift amounts for a single campaign."""
    return sum(
        gift['amount'] for gift in gifts if gift['campaign_name'] == campaign_name
    )


def generate_thank_you_message(contact, gift):
    """Compose a personalized thank-you note for a donor and their gift."""
    amount = gift['amount']
    campaign = gift['campaign_name']
    body = (
        f"Dear {contact['first_name']},\n\n"
        f"Thank you so much for your generous gift of ${amount}.\n"
        f"Your support of the '{campaign}' campaign makes a real difference.\n\n"
        f"With gratitude,\nThe DonorTrack Team"
    )
    return contact['email'], body


def tag_recent_gifts(gifts, days=30):
    """Tag gifts received within the last N days with 'recent'."""
    from datetime import datetime, timedelta
    cutoff = datetime.now() - timedelta(days=days)
    for gift in gifts:
        gift_date = datetime.strptime(gift['gift_date'], '%Y-%m-%d')
        gift['is_recent'] = gift_date >= cutoff
    return gifts
