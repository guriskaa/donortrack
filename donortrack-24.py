# === Stage 24: Add grouped summaries by category or status ===
# Project: DonorTrack
def grouped_summaries(groups):
    """Return a dict of category/status -> list of donor summaries."""
    out = {}
    for donor in groups:
        key = donor.get('category', donor.get('status', 'unknown'))
        out.setdefault(key, []).append(donor)
    return out
