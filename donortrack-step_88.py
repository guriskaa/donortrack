# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: DonorTrack
def safe_int(value, default=0):
    try:
        return int(str(value).strip())
    except (ValueError, TypeError):
        return default


def safe_float(value, default=0.0):
    try:
        return float(str(value).strip())
    except (ValueError, TypeError):
        return default


def safe_str(value, default=""):
    if value is None:
        return default
    return str(value).strip()


def safe_bool(value, default=False):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ("yes", "true", "1", "y", "t")
    return bool(value)


def safe_name(value, default=""):
    name = safe_str(value, default)
    return name or "Unknown Donor"


def safe_email(value, default=""):
    email = safe_str(value, default)
    if "@" not in email or "." not in email.split("@")[-1]:
        return default
    return email.lower()


def safe_money(value, default=0.0):
    amount = safe_float(value, default)
    return max(0.0, round(amount, 2))


def safe_date(value, default=""):
    if not value:
        return default
    text = safe_str(value, default)
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d %b %Y", "%B %d, %Y"):
        try:
            return datetime.strptime(text, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return default


def safe_phone(value, default=""):
    cleaned = re.sub(r"[^0-9+()\- ]", "", str(value).strip())
    return cleaned or default


class SafeInput:
    def __init__(self, name, email="", phone="", address="", city="", state="", zip_code="", notes=""):
        self.name = safe_name(name)
        self.email = safe_email(email)
        self.phone = safe_phone(phone)
        self.address = safe_str(address)
        self.city = safe_str(city)
        self.state = safe_str(state)
        self.zip_code = safe_str(zip_code)
        self.notes = safe_str(notes)

    def is_valid(self):
        return bool(self.name)
