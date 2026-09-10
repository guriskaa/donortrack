# === Stage 13: Add file save support using a configurable path ===
# Project: DonorTrack
import os

def save_to_file(data, path):
    if not path:
        path = "donor_data.json"
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
