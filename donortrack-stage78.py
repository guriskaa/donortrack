# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: DonorTrack
def parse_gift_line(line):
    """Parse a single CSV gift record into a dict."""
    parts = line.split(",")
    if len(parts) < 4:
        return None
    gift = {
        "gift_id": parts[0].strip(),
        "donor_id": parts[1].strip(),
        "amount": float(parts[2].strip()),
        "gift_date": parts[3].strip(),
    }
    return gift


def calculate_gift_totals(gifts):
    """Return total, average, and count for a list of gifts."""
    amounts = [g["amount"] for g in gifts if g["amount"] > 0]
    total = sum(amounts)
    average = total / len(amounts) if amounts else 0.0
    return total, average, len(amounts)


def find_top_donors(gifts, limit=5):
    """Return the highest-value donors sorted by total gifts descending."""
    donor_totals = {}
    for gift in gifts:
        donor_id = gift["donor_id"]
        donor_totals[donor_id] = donor_totals.get(donor_id, 0) + gift["amount"]
    return sorted(donor_totals.items(), key=lambda item: item[1], reverse=True)[:limit]
