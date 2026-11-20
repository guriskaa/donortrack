# === Stage 73: Add a lightweight HTML report export ===
# Project: DonorTrack
import csv, datetime

def export_report(donors, gifts, campaigns, output="report.csv"):
    with open(output, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["donor_id", "name", "email", "total_gifts", "gift_count", "campaigns", "last_gift"])
        for d in donors:
            gid = d.get("gifts", [])
            total = sum(g.get("amount", 0) for g in gid)
            camps = [c.get("name") for c in campaigns if any(g.get("campaign") == c["name"] for g in gid)]
            last = max((g.get("date", "") for g in gid), default="")
            w.writerow([d["id"], d["name"], d.get("email", ""), total, len(gid), "|".join(camps), last])
