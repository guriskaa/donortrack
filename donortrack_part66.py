# === Stage 66: Add export of a short status dashboard ===
# Project: DonorTrack
def export_status_dashboard():
    contacts = load_contacts()
    gifts = load_gifts()
    campaigns = load_campaigns()
    notes = load_thank_you_notes()
    total_gifts = sum(g.amount for g in gifts)
    active_campaigns = [c for c in campaigns if c.active]
    recent_gifts = sorted(gifts, key=lambda g: g.date, reverse=True)[:5]
    lines = ["DonorTrack Status Dashboard", "==========================="]
    lines.append(f"Total Contacts: {len(contacts)}")
    lines.append(f"Total Gifts: {total_gifts}")
    lines.append(f"Active Campaigns: {len(active_campaigns)}")
    lines.append(f"Thank-You Notes Sent: {len(notes)}")
    lines.append("")
    lines.append("Recent Gifts:")
    for g in recent_gifts:
        lines.append(f"- {g.date}: {g.amount} from {g.donor}")
    with open("status_dashboard.txt", "w") as f:
        f.write("\n".join(lines))
    print("Status Dashboard Exported")
