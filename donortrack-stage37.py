# === Stage 37: Add recommendations for the next useful action ===
# Project: DonorTrack
def generate_monthly_report(donors, gifts, campaigns):
    """Generate a monthly summary report for the nonprofit."""
    total_gifts = sum(g.amount for g in gifts)
    total_campaigns = len(campaigns)
    unique_donors = len(donors)
    avg_gift = total_gifts / unique_donors if unique_donors > 0 else 0
    report = f"Monthly Report: {unique_donors} donors, {total_campaigns} campaigns, total gifts: ${total_gifts:,.2f}, avg: ${avg_gift:,.2f}"
    return report
