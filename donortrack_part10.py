# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: DonorTrack
def search_contacts(self, query):
    """Case-insensitive search across name, email, and organization."""
    query = query.lower().strip()
    if not query:
        return list(self.contacts.values())
    matches = []
    for cid, c in self.contacts.items():
        if (query in c.name.lower() or
            query in c.email.lower() or
            query in c.organization.lower() or
            query in c.phone.lower()):
            matches.append(c)
    return matches
