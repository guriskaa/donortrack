# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: DonorTrack
class SortedDonorView(DonorView):
    def __init__(self, donors, sort_by="last_updated", reverse=False):
        super().__init__(donors)
        self._sort_key = {"title": 0, "date": 1, "priority": 2, "last_updated": 3}.get(sort_by, 3)
        self._reverse = reverse

    def __iter__(self):
        return sorted(self._donors, key=lambda d: (d.title if self._sort_key == 0 else d.created,
                                                     d.priority if self._sort_key == 2 else d.created,
                                                     d.last_updated if self._sort_key == 3 else d.created),
                       reverse=self._reverse)

    def __len__(self):
        return len(self._donors)
