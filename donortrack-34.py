# === Stage 34: Add support for multiple local user profiles ===
# Project: DonorTrack
import json
from pathlib import Path

class UserProfile:
    def __init__(self, name, email, phone, notes=""):
        self.name = name
        self.email = email
        self.phone = phone
        self.notes = notes

    def to_dict(self):
        return {"name": self.name, "email": self.email, "phone": self.phone, "notes": self.notes}

    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["email"], d["phone"], d.get("notes", ""))

    def save(self, filepath):
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def load(cls, filepath):
        with open(filepath, "r") as f:
            return cls.from_dict(json.load(f))

class DonorTracker:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.profiles_dir = self.data_dir / "profiles"
        self.profiles_dir.mkdir(exist_ok=True)
        self.users = []
        self.current_user = None
        self._load_users()

    def _load_users(self):
        for p in sorted(self.profiles_dir.glob("user_*.json")):
            self.users.append(UserProfile.load(p))
        if self.users:
            self.current_user = self.users[0]

    def add_user(self, profile):
        self.users.append(profile)
        profile.save(self.profiles_dir / f"user_{len(self.users)}.json")
        if not self.current_user:
            self.current_user = profile

    def switch_user(self, index):
        if 0 <= index < len(self.users):
            self.current_user = self.users[index]
