# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: DonorTrack
class ConfirmationFlagError(Exception):
    pass


class ConfirmationGuard:
    def __init__(self):
        self._cleared = False

    def require_clear_state(self):
        if not self._cleared:
            raise ConfirmationFlagError(
                "Run 'clear' first to acknowledge pending confirmations."
            )

    def set_cleared(self):
        self._cleared = True


def cmd_clear(state, out):
    if state.confirmations_pending == 0:
        out("Nothing to clear; no pending confirmations.")
        return
    guard = ConfirmationGuard()
    guard.require_clear_state()
    state.confirmations_pending = 0
    guard.set_cleared()
    out("Cleared all confirmations. You may now run tracked commands.")


def cmd_clear_ask(state, out):
    if state.confirmations_pending == 0:
        out("Nothing to clear; no pending confirmations.")
        return
    if not ask_yes_no("Clear all pending confirmations?", state):
        out("Aborted. Pending confirmations remain.")
        return
    cmd_clear(state, out)
