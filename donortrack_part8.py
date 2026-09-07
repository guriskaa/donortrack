# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: DonorTrack
def filter_donors(self, status=None, category=None, owner=None, tag=None):
    filtered = self._donors[:]
    if status is not None:
        filtered = [d for d in filtered if d.status == status]
    if category is not None:
        filtered = [d for d in filtered if d.category == category]
    if owner is not None:
        filtered = [d for d in filtered if d.owner == owner]
    if tag is not None:
        filtered = [d for d in filtered if tag in d.tags]
    return filtered
