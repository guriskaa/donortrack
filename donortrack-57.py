# === Stage 57: Add structured result objects for command handlers ===
# Project: DonorTrack
class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def to_dict(self):
        return {"name": self.name, "email": self.email, "phone": self.phone, "address": self.address}


class Gift:
    def __init__(self, donor, amount, date, campaign=None):
        self.donor = donor
        self.amount = amount
        self.date = date
        self.campaign = campaign

    def to_dict(self):
        result = {"donor": self.donor, "amount": self.amount, "date": self.date}
        if self.campaign is not None:
            result["campaign"] = self.campaign
        return result


class Campaign:
    def __init__(self, name, goal, deadline):
        self.name = name
        self.goal = goal
        self.deadline = deadline

    def to_dict(self):
        return {"name": self.name, "goal": self.goal, "deadline": self.deadline}


class ThankYouNote:
    def __init__(self, recipient, message, sent_date=None):
        self.recipient = recipient
        self.message = message
        self.sent_date = sent_date

    def to_dict(self):
        result = {"recipient": self.recipient, "message": self.message}
        if self.sent_date is not None:
            result["sent_date"] = self.sent_date
        return result
