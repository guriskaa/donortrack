# === Stage 43: Add CSV import for the primary record type ===
# Project: DonorTrack
import csv

def import_contacts_from_csv(file_path):
    """Import contacts from a CSV file with columns: name, email, phone."""
    contacts = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            contacts.append({
                'name': row['name'].strip(),
                'email': row['email'].strip(),
                'phone': row.get('phone', '').strip(),
            })
    return contacts
