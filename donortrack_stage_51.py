# === Stage 51: Add unit tests for search and filter behavior ===
# Project: DonorTrack
def test_search_by_name():
    contacts = [
        {"name": "Alice Smith", "gifts": []},
        {"name": "Bob Jones", "gifts": []},
        {"name": "Alice Cooper", "gifts": []},
    ]
    results = search_contacts(contacts, "alice")
    assert len(results) == 2
    assert all("Alice" in c["name"] for c in results)


def test_search_is_case_insensitive():
    contacts = [{"name": "Carol Danvers", "gifts": []}]
    results = search_contacts(contacts, "CAROL")
    assert len(results) == 1


def test_search_no_match_returns_empty():
    contacts = [{"name": "Dave", "gifts": []}]
    results = search_contacts(contacts, "zoe")
    assert results == []


def test_filter_by_gift_amount():
    contacts = [
        {"name": "Frank", "gifts": [{"amount": 100}]},
        {"name": "Grace", "gifts": [{"amount": 250}]},
        {"name": "Heidi", "gifts": [{"amount": 50}]},
    ]
    results = filter_contacts_by_min_gift(contacts, 100)
    assert len(results) == 2
    assert all(c["gifts"] for c in results)


def test_filter_no_gifts_excluded():
    contacts = [
        {"name": "Ivan", "gifts": []},
        {"name": "Judy", "gifts": [{"amount": 10}]},
    ]
    results = filter_contacts_by_min_gift(contacts, 10)
    assert len(results) == 1
    assert results[0]["name"] == "Judy"


def test_filter_with_no_min_amount_returns_all():
    contacts = [{"name": "Karl", "gifts": []}]
    results = filter_contacts_by_min_gift(contacts, 0)
    assert len(results) == 1
