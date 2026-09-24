# === Stage 45: Add restore from backup with validation ===
# Project: DonorTrack
import shutil, os, json

BACKUP_DIR = os.path.join(os.path.dirname(__file__), "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)

def save_backup():
    """Save current DB to a timestamped backup file."""
    src = os.path.join(os.path.dirname(__file__), "donors.json")
    if not os.path.isfile(src):
        return None
    ts = os.path.getmtime(src)
    name = f"donors_backup_{ts}.json"
    dst = os.path.join(BACKUP_DIR, name)
    shutil.copy2(src, dst)
    return name

def restore_backup(name=None):
    """Restore from a backup file, validating it before overwriting."""
    if name is None:
        backups = sorted(os.listdir(BACKUP_DIR), reverse=True)
        if not backups:
            print("No backups available.")
            return False
        name = backups[0]
    src = os.path.join(BACKUP_DIR, name)
    if not os.path.isfile(src):
        print(f"Backup file not found: {src}")
        return False
    try:
        with open(src, "r") as f:
            data = json.load(f)
        if not isinstance(data, dict) or "contacts" not in data:
            print("Invalid backup structure.")
            return False
    except (json.JSONDecodeError, TypeError) as e:
        print(f"Backup corrupted: {e}")
        return False
    dst = os.path.join(os.path.dirname(__file__), "donors.json")
    with open(dst, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Restored from {name}.")
    return True
