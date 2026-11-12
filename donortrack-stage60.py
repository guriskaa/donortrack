# === Stage 60: Add saved views for frequently used filters ===
# Project: DonorTrack
class SavedView:
    def __init__(self, name, filters=None, sort_by=None, sort_order=None):
        self.name = name
        self.filters = filters or {}
        self.sort_by = sort_by or "last_gift_date"
        self.sort_order = sort_order or "desc"

    def apply(self, contacts):
        result = [c for c in contacts if _matches(c, self.filters)]
        result.sort(key=lambda c: c.get(self.sort_by), reverse=(self.sort_order == "desc"))
        return result

    def to_dict(self):
        return {"name": self.name, "filters": self.filters, "sort_by": self.sort_by, "sort_order": self.sort_order}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data.get("filters"), data.get("sort_by"), data.get("sort_order"))


def _matches(contact, filters):
    for key, value in filters.items():
        if contact.get(key) != value:
            return False
    return True


class SavedViewManager:
    def __init__(self, store=None):
        self._store = store if store is not None else []

    def add(self, view):
        self._store.append(view)

    def list(self):
        return list(self._store)

    def get(self, name):
        for view in self._store:
            if view.name == name:
                return view
        return None

    def remove(self, name):
        self._store = [v for v in self._store if v.name != name]

    def rename(self, old_name, new_name):
        view = self.get(old_name)
        if view:
            view.name = new_name

    def save(self, name, filters=None, sort_by=None, sort_order=None):
        self.add(SavedView(name, filters, sort_by, sort_order))

    def load(self, name):
        return self.get(name).apply([]) if self.get(name) else []


def register_common_views(manager):
    manager.save("All Donors", {"status": "active"}, "last_gift_date", "desc")
    manager.save("Recent Gifts", {"last_gift_date": ">=2024-01-01"}, "gift_amount", "desc")
    manager.save("Major Donors", {"gift_amount": ">1000"}, "gift_amount", "desc")
    manager.save("Pending Thank Yous", {"thanked": False}, "gift_date", "desc")
