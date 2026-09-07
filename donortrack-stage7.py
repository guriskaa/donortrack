# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: DonorTrack
def format_contact(contact: dict) -> str:
    lines = [f"Name: {contact.get('name', 'Unknown')}", f"Email: {contact.get('email', 'N/A')}"]
    if contact.get('phone'):
        lines.append(f"Phone: {contact['phone']}")
    if contact.get('address'):
        lines.append(f"Address: {contact['address']}")
    if contact.get('notes'):
        lines.append(f"Notes: {contact['notes']}")
    return "\n".join(lines)

def format_gift(gift: dict) -> str:
    lines = [f"Amount: ${gift.get('amount', 0):,.2f}", f"Date: {gift.get('date', 'N/A')}", f"Type: {gift.get('type', 'Unknown')}"]
    if gift.get('description'):
        lines.append(f"Description: {gift['description']}")
    return "\n".join(lines)

def format_campaign(campaign: dict) -> str:
    lines = [f"Title: {campaign.get('title', 'Untitled')}", f"Target: ${campaign.get('target', 0):,.2f}", f"Raised: ${campaign.get('raised', 0):,.2f}"]
    if campaign.get('description'):
        lines.append(f"Description: {campaign['description']}")
    return "\n".join(lines)

def format_thank_you_note(note: dict) -> str:
    lines = [f"Recipient: {note.get('recipient', 'Unknown')}", f"Date: {note.get('date', 'N/A')}", f"Message: {note.get('message', '')}"]
    return "\n".join(lines)

def list_all(data: dict) -> str:
    parts = []
    if 'contacts' in data:
        parts.append(f"\n--- {len(data['contacts'])} Contact(s) ---")
        for c in data['contacts']:
            parts.append(format_contact(c))
    if 'gifts' in data:
        parts.append(f"\n--- {len(data['gifts'])} Gift(s) ---")
        for g in data['gifts']:
            parts.append(format_gift(g))
    if 'campaigns' in data:
        parts.append(f"\n--- {len(data['campaigns'])} Campaign(s) ---")
        for k in data['campaigns']:
            parts.append(format_campaign(data['campaigns'][k]))
    if 'notes' in data:
        parts.append(f"\n--- {len(data['notes'])} Thank-You Note(s) ---")
        for n in data['notes']:
            parts.append(format_thank_you_note(n))
    return "\n".join(parts) if parts else "No data to display."
