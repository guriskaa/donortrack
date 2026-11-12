# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: DonorTrack
def donor_priority(donor):
    score = 0
    score += donor.get("lifetime_gifts", 0) * 5
    score += donor.get("last_gift_age_months", 120)
    score += len(donor.get("campaigns", [])) * 2
    if donor.get("contacted", False):
        score += 1
    return score

def prioritize_donors(donors):
    return sorted(donors, key=donor_priority, reverse=True)
