# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: DonorTrack
def parse_date(value, fmt=None):
    """Parse a date string into a datetime.date object.

    Tries ISO format (YYYY-MM-DD) first, then common alternatives.
    Returns None and a descriptive error message on failure.
    """
    if fmt is not None:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass

    for _fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(value, _fmt).date()
        except ValueError:
            continue

    return None, "Unrecognized date format: {}".format(value)
