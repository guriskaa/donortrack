# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: DonorTrack
def _dry_run(self, action: str, target: str) -> None:
    print(f"[dry-run] {action} on {target} -- no changes applied")

def dry_run_mode(self) -> None:
    self._dry_run("initialize", "DonorTrack")
