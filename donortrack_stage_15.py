# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: DonorTrack
def dispatch_command(command):
    """Simple dispatcher for text commands."""
    command = command.strip().lower()
    if command in ('add_contact', 'add_gift', 'add_campaign'):
        return 'add'
    elif command in ('list_contacts', 'list_gifts', 'list_campaigns'):
        return 'list'
    elif command in ('show_thanks', 'generate_thanks'):
        return 'thank'
    elif command in ('save', 'export'):
        return 'save'
    elif command in ('help', 'info'):
        return 'help'
    elif command == 'quit':
        return 'quit'
    else:
        return 'unknown'
