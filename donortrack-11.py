# === Stage 11: Add JSON export for the current application state ===
# Project: DonorTrack
def export_to_json():
    """Export the full application state to a JSON file."""
    import json
    state = {
        "contacts": list(contacts.values()),
        "gifts": list(gifts.values()),
        "campaigns": list(campaigns.values()),
        "thank_you_notes": list(thank_you_notes.values()),
    }
    with open("donortrack_state.json", "w") as f:
        json.dump(state, f, indent=2)
    print("State exported to donortrack_state.json")
