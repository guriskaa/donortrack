# === Stage 26: Add weekly summary calculations ===
# Project: DonorTrack
from datetime import date, timedelta
from collections import defaultdict
import csv

def weekly_summary(report_path="reports/weekly.csv",
                   contacts_path="data/contacts.csv",
                   gifts_path="data/gifts.csv"):
    """Compute weekly donation totals per donor and write a CSV report."""
    if report_path:
        with open(report_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["week", "donor", "gift_amount", "gift_count"])

    gifts = []
    if gifts_path:
        with open(gifts_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                gifts.append({
                    "date": date.fromisoformat(row["date"]),
                    "donor": row["donor"],
                    "amount": float(row["amount"]),
                })

    today = date.today()
    week = today - timedelta(days=today.weekday())
    current_week = today.strftime("%Y-%m-%d")[:10]

    weekly = defaultdict(lambda: {"amount": 0.0, "count": 0})
    for g in gifts:
        if g["date"] >= week and g["date"] < week + timedelta(days=7):
            weekly[g["donor"]]["amount"] += g["amount"]
            weekly[g["donor"]]["count"] += 1

    return weekly
