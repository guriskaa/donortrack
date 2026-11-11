# === Stage 58: Add bulk update behavior for selected records ===
# Project: DonorTrack
def bulk_update_records(contacts, selected_ids, field, new_value):
    """Update a single field for all records with the given selected_ids."""
    for contact in contacts:
        if contact["id"] in selected_ids and field in contact:
            contact[field] = new_value
    return len(selected_ids)
