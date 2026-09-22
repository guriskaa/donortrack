# === Stage 41: Add plain text import for a simple line-based format ===
# Project: DonorTrack
class PlainTextImporter:
    """Simple line-based format importer for contacts, gifts, campaigns, and notes."""
    def import_contacts(self, lines):
        contacts = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(',')
            if len(parts) >= 4:
                contact = {
                    'name': parts[0].strip(),
                    'email': parts[1].strip(),
                    'phone': parts[2].strip(),
                    'address': parts[3].strip()
                }
                if len(parts) > 4:
                    contact['notes'] = parts[4].strip()
                contacts.append(contact)
        return contacts

    def import_gifts(self, lines):
        gifts = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(',')
            if len(parts) >= 4:
                gift = {
                    'donor': parts[0].strip(),
                    'amount': float(parts[1].strip()),
                    'date': parts[2].strip(),
                    'campaign': parts[3].strip()
                }
                gifts.append(gift)
        return gifts

    def import_campaigns(self, lines):
        campaigns = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(',')
            if len(parts) >= 3:
                campaign = {
                    'name': parts[0].strip(),
                    'budget': float(parts[1].strip()),
                    'target': float(parts[2].strip())
                }
                campaigns.append(campaign)
        return campaigns

    def import_notes(self, lines):
        notes = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(',')
            if len(parts) >= 3:
                note = {
                    'donor': parts[0].strip(),
                    'date': parts[1].strip(),
                    'message': parts[2].strip()
                }
                notes.append(note)
        return notes
