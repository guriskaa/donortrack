# === Stage 53: Add command help text and usage examples ===
# Project: DonorTrack
HELP_TEXT = """
DonorTrack - Nonprofit Donor Tracker
Usage: python donortrack.py <command> [options]

Commands:
  contacts add    Add a new donor contact
  contacts list   List all donor contacts
  gifts add       Record a gift from a donor
  gifts list      List all recorded gifts
  campaigns add   Create a fundraising campaign
  campaigns list  List all campaigns
  notes add       Write a thank-you note for a gift
  notes list      List all thank-you notes
  help            Show this help message

Examples:
  python donortrack.py contacts add --name Alice --email alice@example.com
  python donortrack.py gifts add --donor Alice --amount 50 --campaign Spring Gala
  python donortrack.py campaigns add --name Spring Gala --goal 5000 --deadline 2025-06-01
  python donortrack.py notes add --gift 123 --message "Thank you for your generous gift!"
  python donortrack.py contacts list
  python donortrack.py gifts list
  python donortrack.py campaigns list
  python donortrack.py notes list
"""


def show_help():
    print(HELP_TEXT)


if __name__ == "__main__":
    show_help()
