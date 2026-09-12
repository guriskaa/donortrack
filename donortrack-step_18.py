# === Stage 18: Add an activity log with timestamps and action names ===
# Project: DonorTrack
import datetime

class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, entity_type, entity_id, details=""):
        self.entries.append({
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "details": details,
        })

    def get_recent(self, limit=10):
        return self.entries[-limit:]

    def __len__(self):
        return len(self.entries)
