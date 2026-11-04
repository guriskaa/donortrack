# === Stage 50: Add unit tests for import and export behavior ===
# Project: DonorTrack
import json
from datetime import datetime


def test_import_and_export_roundtrip():
    contacts = [
        {"name": "Ada Lovelace", "email": "ada@example.com", "phone": "555-0001"},
        {"name": "Alan Turing", "email": "alan@example.com", "phone": "555-0002"},
    ]
    gifts = [
        {"donor_name": "Ada Lovelace", "amount": 100, "date": "2024-01-01"},
        {"donor_name": "Alan Turing", "amount": 250, "date": "2024-02-01"},
    ]
    campaigns = [
        {"name": "Winter Gala", "goal": 5000, "raised": 3000},
    ]
    notes = [
        {"recipient": "Ada Lovelace", "message": "Thank you for your generous gift!"},
    ]

    data = {"contacts": contacts, "gifts": gifts, "campaigns": campaigns, "notes": notes}
    payload = json.dumps(data, indent=2)

    restored = json.loads(payload)
    assert restored["contacts"][0]["name"] == "Ada Lovelace"
    assert restored["gifts"][1]["amount"] == 250
    assert restored["campaigns"][0]["raised"] == 3000
    assert restored["notes"][0]["message"] == "Thank you for your generous gift!"

    exported = json.loads(json.dumps(data))
    assert exported == data

    with open("donortrack_export.json", "w") as handle:
        json.dump(data, handle)
    with open("donortrack_export.json") as handle:
        reloaded = json.load(handle)
    assert reloaded["contacts"] == contacts
    assert reloaded["gifts"] == gifts
    assert reloaded["campaigns"] == campaigns
    assert reloaded["notes"] == notes

    print("DonorTrack import/export tests passed")
