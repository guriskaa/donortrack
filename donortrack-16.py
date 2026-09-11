# === Stage 16: Add argparse support for the most common commands ===
# Project: DonorTrack
import argparse

def main():
    parser = argparse.ArgumentParser(description="DonorTrack - Nonprofit Donor Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("contacts", help="Manage donor contacts")
    subparsers.add_parser("gifts", help="Record gifts and donations")
    subparsers.add_parser("campaigns", help="Manage fundraising campaigns")
    subparsers.add_parser("notes", help="Write and send thank-you notes")
    subparsers.add_parser("list", help="List all contacts")
    subparsers.add_parser("search", help="Search contacts by name or email")
    subparsers.add_parser("stats", help="View campaign statistics")
    subparsers.add_parser("export", help="Export data to CSV")

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return
    print(f"Running command: {args.command}")
    # TODO: dispatch to corresponding handler

if __name__ == "__main__":
    main()
