# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: DonorTrack
def main():
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nDonorTrack stopped. Goodbye!")
