# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: DonorTrack
def reset_demo_data(db):
    """Clear all tables and reinsert demo rows for manual testing."""
    tables = ["contacts", "gifts", "campaigns", "thank_you_notes"]
    for table in tables:
        db.execute(f"DELETE FROM {table}")
    db.execute(
        "INSERT INTO contacts (name, email, phone, city) VALUES "
        "(?, ?, ?, ?)",
        ("Alice Donor", "alice@example.com", "555-0100", "Springfield"),
        ("Bob Giver", "bob@example.com", "555-0101", "Shelbyville"),
        ("Carol Fundraiser", "carol@example.com", "555-0102", "Franklin"),
    )
    db.execute(
        "INSERT INTO campaigns (name, goal, status) VALUES (?, ?, ?)",
        ("Spring Fundraiser", 10000, "active"),
    )
    db.execute(
        "INSERT INTO gifts (donor_id, campaign_id, amount, date) VALUES "
        "(?, ?, ?, ?)",
        (1, 1, 500, "2024-01-15"),
        (2, 1, 250, "2024-02-20"),
    )
    db.execute(
        "INSERT INTO thank_you_notes "
        "(donor_id, campaign_id, message, sent) VALUES (?, ?, ?, ?)",
        (1, 1, "Thank you for your generous gift!", "yes"),
    )
    print("Demo data reset complete.")

if __name__ == "__main__":
    import sqlite3
    db = sqlite3.connect("donortrack.db")
    reset_demo_data(db)
    db.close()
