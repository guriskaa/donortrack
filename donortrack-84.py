# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: DonorTrack
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def trim_whitespace(text):
    if text is None:
        return ""
    return text.strip()


def to_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def to_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def normalize_name(name):
    if name is None:
        return ""
    return trim_whitespace(name).title()


def group_by_key(mapping, key):
    grouped = {}
    for item in mapping.values():
        grouped.setdefault(item.get(key), []).append(item)
    return grouped


def filter_by(predicate, items):
    return [item for item in items if predicate(item)]


def sort_by_key(items, key, reverse=False):
    return sorted(items, key=lambda item: item.get(key, 0), reverse=reverse)
