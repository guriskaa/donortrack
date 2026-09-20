# === Stage 36: Add templates for quickly creating common records ===
# Project: DonorTrack
# DonorTrack - Templates for quickly creating common records
# Append to donortrack.py

from datetime import date, datetime
from donortrack import Contact, Gift, Campaign, ThankYouNote


def create_sample_contact(name: str, email: str, phone: str = "") -> Contact:
    """Create a sample Contact record with basic details."""
    return Contact(
        name=name,
        email=email,
        phone=phone
    )


def create_sample_gift(donor_name: str, amount: float, campaign_name: str = "",
                        date: date = None) -> Gift:
    """Create a sample Gift record with donor, amount, and campaign info."""
    if date is None:
        date = date.today()
    return Gift(
        donor_name=donor_name,
        amount=amount,
        campaign_name=campaign_name,
        date=date
    )


def create_sample_campaign(name: str, goal: float, start_date: date = None,
                            end_date: date = None) -> Campaign:
    """Create a sample Campaign record with name, goal, and dates."""
    if start_date is None:
        start_date = date.today()
    return Campaign(
        name=name,
        goal=goal,
        start_date=start_date,
        end_date=end_date
    )


def create_sample_thank_you_note(contact_name: str, gift_amount: float,
                                  campaign_name: str = "") -> ThankYouNote:
    """Create a sample ThankYouNote record for a donor."""
    return ThankYouNote(
        contact_name=contact_name,
        gift_amount=gift_amount,
        campaign_name=campaign_name
    )


# Example usage:
# contact1 = create_sample_contact("Alice Johnson", "alice@example.com", "555-0101")
# gift1 = create_sample_gift("Alice Johnson", 500.0, "Annual Fund", date(2024, 1, 15))
# campaign1 = create_sample_campaign("2024 Annual Fund", 100000.0)
# note1 = create_sample_thank_you_note("Alice Johnson", 500.0, "Annual Fund")
