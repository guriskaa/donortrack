# === Stage 25: Add daily summary calculations ===
# Project: DonorTrack
def daily_summary(donors, gifts, campaigns, notes):
    today = datetime.date.today()
    daily_gifts = [g for g in gifts if g.gift_date == today]
    daily_value = sum(g.amount for g in daily_gifts)
    daily_count = len(daily_gifts)
    today_campaigns = [c for c in campaigns if c.start_date <= today <= c.end_date]
    today_notes = [n for n in notes if n.created_date == today]
    total_donors = len(donors)
    total_gifts = len(gifts)
    total_amount = sum(g.amount for g in gifts)
    avg_gift = total_amount / total_gifts if total_gifts else 0
    summary = {
        "date": today,
        "donors": total_donors,
        "gifts": daily_count,
        "gift_value": daily_value,
        "campaigns_active": len(today_campaigns),
        "notes": len(today_notes),
        "total_gifts": total_gifts,
        "total_amount": total_amount,
        "avg_gift": avg_gift,
    }
    return summary
