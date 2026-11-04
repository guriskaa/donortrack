# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: DonorTrack
def test_update_missing_contact_returns_none():
    contacts = {"alice": {"name": "Alice"}}
    result = update_contact(contacts, "bob", {"name": "Bob"})
    assert result is None
    assert contacts == {"alice": {"name": "Alice"}}


def test_update_existing_contact_updates_fields():
    contacts = {"alice": {"name": "Alice"}}
    result = update_contact(contacts, "alice", {"name": "Alice Smith"})
    assert result == {"name": "Alice Smith"}
    assert contacts["alice"]["name"] == "Alice Smith"


def test_delete_missing_contact_returns_none():
    contacts = {"alice": {"name": "Alice"}}
    result = delete_contact(contacts, "bob")
    assert result is None
    assert contacts == {"alice": {"name": "Alice"}}


def test_delete_existing_contact_removes_entry():
    contacts = {"alice": {"name": "Alice"}}
    result = delete_contact(contacts, "alice")
    assert result == {"name": "Alice"}
    assert contacts == {}
