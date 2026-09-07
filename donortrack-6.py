# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: DonorTrack
def delete_record(self, record_id: str, confirm: bool = False) -> bool:
    """Delete a record by its unique ID.
    
    Args:
        record_id: The unique identifier of the record.
        confirm: If False, prompts for confirmation before deletion.
        
    Returns:
        True if the record was successfully deleted, False otherwise.
    """
    if record_id not in self._data:
        print(f"Record with ID '{record_id}' not found.")
        return False
    
    if not confirm:
        print(f"WARNING: You are about to delete the record with ID '{record_id}'.")
        response = input("Are you sure? (yes/no): ").strip().lower()
        if response != 'yes':
            print("Deletion cancelled.")
            return False
    
    del self._data[record_id]
    print(f"Record '{record_id}' deleted successfully.")
    return True
