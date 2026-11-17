# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: DonorTrack
def build_changelog():
    """Generate a compact changelog from the activity log."""
    activity = load_activity_log()
    entries = {}
    for record in activity:
        date = record.get("date")
        message = record.get("message", "")
        if date and message:
            entries[date] = entries.get(date, [])
            entries[date].append(message)
    lines = []
    for date in sorted(entries, reverse=True):
        lines.append(f"{date}")
        for message in entries[date]:
            lines.append(f"  - {message}")
    header = "CHANGELOG"
    width = max([len(header)] + [len(line) for line in lines])
    output = [f"{header:<{width}}"]
    output += lines
    return "\n".join(output)
