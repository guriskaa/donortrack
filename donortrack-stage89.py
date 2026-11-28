# === Stage 89: Add final consistency checks for names, statuses, and dates ===
# Project: DonorTrack
def validate_records(records):
    valid_statuses = {"new", "active", "lapsed", "donor", "prospect"}
    valid_name_fields = ["first", "last", "full"]
    issues = []
    for rec in records:
        name = rec.get("name") or rec.get("full")
        if not name or not str(name).strip():
            issues.append(f"Missing name for {rec.get('id', 'unknown')}")
            continue
        name = str(name).strip()
        if len(name) > 100:
            issues.append(f"Name too long for {rec.get('id', 'unknown')}")
        if rec.get("status") and rec["status"] not in valid_statuses:
            issues.append(f"Invalid status '{rec['status']}' for {name}")
        if rec.get("email") and not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", str(rec["email"])):
            issues.append(f"Invalid email for {name}")
        if rec.get("phone") and not re.match(r"^\+?[\d\s\-()]+$", str(rec["phone"])):
            issues.append(f"Invalid phone for {name}")
        for field in valid_name_fields:
            if rec.get(field) and not str(rec[field]).strip():
                issues.append(f"Empty {field} for {name}")
        date_fields = ["created", "donated", "last_contact"]
        for field in date_fields:
            raw = rec.get(field)
            if raw and not _is_valid_date(str(raw)):
                issues.append(f"Invalid date '{raw}' for {name}")
    return issues


def _is_valid_date(value):
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d"):
        try:
            datetime.strptime(value, fmt)
            return True
        except ValueError:
            continue
    return False
