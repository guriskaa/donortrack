# === Stage 20: Add duplicate detection for newly created records ===
# Project: DonorTrack
import json
from datetime import datetime

class DuplicateDetector:
    def __init__(self):
        self.seen = {}

    def check(self, record, field='id'):
        key = record.get(field)
        if key in self.seen:
            return False
        self.seen[key] = datetime.now().isoformat()
        return True
