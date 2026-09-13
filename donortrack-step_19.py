# === Stage 19: Add undo support for the last simple mutation ===
# Project: DonorTrack
def undo_last():
    """Undo the last simple mutation in the history."""
    if not history:
        print("Nothing to undo.")
        return
    action = history.pop()
    print(f"Undone: {action}")
    if action == "add_contact":
        contacts.pop()
    elif action == "add_gift":
        gifts.pop()
    elif action == "add_campaign":
        campaigns.pop()
    elif action == "add_note":
        notes.pop()
