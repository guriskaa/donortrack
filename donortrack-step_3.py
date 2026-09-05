# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: DonorTrack
def is_valid_email(email):
    if not email or '@' not in email:
        return False
    local, _, domain = email.rpartition('@')
    return bool(local) and '.' in domain

def is_valid_date(date_str):
    if not date_str:
        return False
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_valid_id(id_str):
    if not id_str or not id_str.isalnum():
        return False
    return len(id_str) >= 2

def is_valid_short_text(text, max_len=100):
    if not text or len(text.strip()) == 0:
        return False
    return len(text) <= max_len

def is_valid_money(amount):
    if not amount or not amount.replace('.', '', 1).isdigit():
        return False
    return float(amount) >= 0
