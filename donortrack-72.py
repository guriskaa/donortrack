# === Stage 72: Add Markdown report export ===
# Project: DonorTrack
def export_markdown_report(donors, gifts, campaigns, thank_you_notes, path):
    lines = ["# DonorTrack Report", ""]
    lines.append("## Contacts")
    lines.append("")
    for d in donors:
        lines.append(f"- {d['name']} ({d['email']}) - {d['phone']}")
    lines.append("")
    lines.append("## Gifts")
    lines.append("")
    for g in gifts:
        lines.append(f"- {g['donor']} - ${g['amount']} on {g['date']}")
    lines.append("")
    lines.append("## Campaigns")
    lines.append("")
    for c in campaigns:
        lines.append(f"- {c['name']} - {c['goal']}")
    lines.append("")
    lines.append("## Thank-You Notes")
    lines.append("")
    for n in thank_you_notes:
        lines.append(f"- To {n['recipient']}: {n['message']}")
    lines.append("")
    with open(path, "w") as f:
        f.write("\n".join(lines))
