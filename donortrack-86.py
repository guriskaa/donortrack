# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: DonorTrack
def demo_cli():
    """Sample command transcripts for DonorTrack CLI workflows."""
    print("=== DonorTrack CLI Demo ===")
    print("1) Add a contact")
    print("   python donortrack.py add-contact --name 'Alice Johnson' "
          "--email alice@example.com --phone 555-0100")
    print("2) List contacts")
    print("   python donortrack.py list-contacts")
    print("3) Add a gift")
    print("   python donortrack.py add-gift --contact 'Alice Johnson' "
          "--amount 100 --campaign 'Spring Gala' --date 2024-05-01")
    print("4) List gifts")
    print("   python donortrack.py list-gifts")
    print("5) Create a campaign")
    print("   python donortrack.py add-campaign --name 'Spring Gala' "
          "--goal 5000")
    print("6) List campaigns")
    print("   python donortrack.py list-campaigns")
    print("7) Create a thank-you note")
    print("   python donortrack.py add-note --contact 'Alice Johnson' "
          "--gift 'Spring Gala' --message 'Thank you for your generous gift!'")
    print("8) List thank-you notes")
    print("   python donortrack.py list-notes")
    print("9) Export data")
    print("   python donortrack.py export --format json")
    print("10) Start server")
    print("    python donortrack.py serve")
