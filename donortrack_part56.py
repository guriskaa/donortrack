# === Stage 56: Add compact error classes for domain failures ===
# Project: DonorTrack
class DomainError(Exception):
    """Base class for all domain-specific failures."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ContactNotFoundError(DomainError):
    """Raised when a requested contact does not exist."""

    def __init__(self, contact_id):
        super().__init__(f"Contact not found: {contact_id}")
        self.contact_id = contact_id


class GiftNotFoundError(DomainError):
    """Raised when a requested gift does not exist."""

    def __init__(self, gift_id):
        super().__init__(f"Gift not found: {gift_id}")
        self.gift_id = gift_id


class CampaignNotFoundError(DomainError):
    """Raised when a requested campaign does not exist."""

    def __init__(self, campaign_id):
        super().__init__(f"Campaign not found: {campaign_id}")
        self.campaign_id = campaign_id


class ThankYouNoteNotFoundError(DomainError):
    """Raised when a requested thank-you note does not exist."""

    def __init__(self, note_id):
        super().__init__(f"Thank-you note not found: {note_id}")
        self.note_id = note_id


class InvalidContactError(DomainError):
    """Raised when a contact record fails validation."""

    def __init__(self, message):
        super().__init__(f"Invalid contact: {message}")


class InvalidGiftError(DomainError):
    """Raised when a gift record fails validation."""

    def __init__(self, message):
        super().__init__(f"Invalid gift: {message}")


class InvalidCampaignError(DomainError):
    """Raised when a campaign record fails validation."""

    def __init__(self, message):
        super().__init__(f"Invalid campaign: {message}")


class InvalidThankYouNoteError(DomainError):
    """Raised when a thank-you note fails validation."""

    def __init__(self, message):
        super().__init__(f"Invalid thank-you note: {message}")
