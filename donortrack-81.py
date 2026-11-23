# === Stage 81: Add final README text as a module string with usage examples ===
# Project: DonorTrack
def show_usage():
    print("=" * 60)
    print("DonorTrack - Nonprofit Donor Tracker")
    print("=" * 60)
    print("1. Add a donor:  donor.add(name, email, phone)")
    print("2. Log a gift:   donor.receive(amount, date, campaign)")
    print("3. List donors:  donor.list_all()")
    print("4. Send thanks:  donor.thank_you(amount, campaign)")
    print("5. Show reports: donor.report()")
    print("=" * 60)


def demo():
    demo = Donor("Alice Johnson", "alice@example.com", "555-0100")
    demo.receive(100.0, "2024-06-01", "Summer Fundraiser")
    demo.thank_you(100.0, "Summer Fundraiser")
    demo.list_all()
    demo.report()


if __name__ == "__main__":
    show_usage()
    demo()
