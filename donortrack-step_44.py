# === Stage 44: Add backup creation for the data file ===
# Project: DonorTrack
def backup_data_file(data_file, backup_dir="."):
    """Create a dated backup of the data file."""
    import os
    import shutil
    from datetime import datetime
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(data_file)}.backup_{timestamp}")
    shutil.copy2(data_file, backup_path)
    print(f"Backup created: {backup_path}")
    return backup_path
