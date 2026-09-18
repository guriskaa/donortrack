# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: DonorTrack
# settings.py – settings dictionary and update functions

SETTINGS = {
    "org_name": "DonorTrack Foundation",
    "contact_prefix": "Dear",
    "contact_suffix": "Sincerely",
    "thank_you_template": "Dear {name},\nThank you for your generous gift of ${amount}.\nWishing you all the best.\n\n{org_name}",
    "campaign_default_goal": 10000,
    "campaign_default_deadline": "2025-12-31",
    "gift_minimum_amount": 5,
    "email_from": "noreply@donortrack.org",
}


def get_setting(key):
    """Return the value for a given setting key."""
    return SETTINGS.get(key, None)


def update_setting(key, value):
    """Update the value of a given setting key, or add a new one."""
    if key in SETTINGS:
        SETTINGS[key] = value
    else:
        raise ValueError(f"Unknown setting key: {key}")


def set_all_settings(settings_dict):
    """Update multiple settings at once. Raises on unknown keys."""
    for key, value in settings_dict.items():
        update_setting(key, value)
