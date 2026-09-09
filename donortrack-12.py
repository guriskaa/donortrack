# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: DonorTrack
import json

def load_json_safe(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"Warning: Malformed JSON in {filepath}: {e}")
        return None
    except PermissionError:
        print(f"Error: No permission to read {filepath}.")
        return None
    except Exception as e:
        print(f"Unexpected error reading {filepath}: {e}")
        return None
