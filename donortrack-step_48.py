# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: DonorTrack
def test_create_contact():
    c = create_contact("Ada Lovelace", "ada@example.org", "+1-555-0100", None)
    assert c["name"] == "Ada Lovelace"
    assert c["email"] == "ada@example.org"
    assert c["phone"] == "+1-555-0100"
    assert c["notes"] is None


def test_create_gift():
    g = create_gift("Ada", "2024-01-01", 100, "cash")
    assert g["donor"] == "Ada"
    assert g["date"] == "2024-01-01"
    assert g["amount"] == 100
    assert g["kind"] == "cash"


def test_create_campaign():
    cm = create_campaign("2024 Gala", "2024-06-15", 5000)
    assert cm["name"] == "2024 Gala"
    assert cm["deadline"] == "2024-06-15"
    assert cm["goal"] == 5000


def test_create_note():
    n = create_note("Ada", "Thank you for your generous gift!")
    assert n["donor"] == "Ada"
    assert n["text"] == "Thank you for your generous gift!"


def test_validate_contact_email():
    assert is_valid_email("a@b.co")
    assert not is_valid_email("not-an-email")
    assert not is_valid_email("")


def test_validate_amount():
    assert is_valid_amount(50)
    assert is_valid_amount(0)
    assert not is_valid_amount(-5)
    assert not is_valid_amount("money")


def test_validate_date():
    assert is_valid_date("2024-01-01")
    assert not is_valid_date("01-01-2024")
    assert not is_valid_date("2024-13-01")
