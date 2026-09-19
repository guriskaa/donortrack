# === Stage 35: Add active user switching and user-specific records ===
# Project: DonorTrack
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserDatabase:
    def __init__(self):
        self.users = []
        self.active_user = None

    def add_user(self, name, email):
        self.users.append(User(name, email))

    def login(self, email):
        for user in self.users:
            if user.email == email:
                self.active_user = user
                return user
        return None

    def logout(self):
        self.active_user = None

    def get_active_user(self):
        return self.active_user
