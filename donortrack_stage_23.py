# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: DonorTrack
def tag_contact(contact, tag_name):
    """Add a tag to a contact if not already present."""
    if tag_name not in contact.tags:
        contact.tags.append(tag_name)
        contact.save()
        return True
    return False

def remove_tag_contact(contact, tag_name):
    """Remove a tag from a contact if present."""
    if tag_name in contact.tags:
        contact.tags.remove(tag_name)
        contact.save()
        return True
    return False

def tag_gift(gift, tag_name):
    """Add a tag to a gift if not already present."""
    if tag_name not in gift.tags:
        gift.tags.append(tag_name)
        gift.save()
        return True
    return False

def remove_tag_gift(gift, tag_name):
    """Remove a tag from a gift if present."""
    if tag_name in gift.tags:
        gift.tags.remove(tag_name)
        gift.save()
        return True
    return False

def tag_campaign(campaign, tag_name):
    """Add a tag to a campaign if not already present."""
    if tag_name not in campaign.tags:
        campaign.tags.append(tag_name)
        campaign.save()
        return True
    return False

def remove_tag_campaign(campaign, tag_name):
    """Remove a tag from a campaign if present."""
    if tag_name in campaign.tags:
        campaign.tags.remove(tag_name)
        campaign.save()
        return True
    return False

def tag_thank_you_note(note, tag_name):
    """Add a tag to a thank-you note if not already present."""
    if tag_name not in note.tags:
        note.tags.append(tag_name)
        note.save()
        return True
    return False

def remove_tag_thank_you_note(note, tag_name):
    """Remove a tag from a thank-you note if present."""
    if tag_name in note.tags:
        note.tags.remove(tag_name)
        note.save()
        return True
    return False

def get_tagged_contacts(tag_name):
    """Return all contacts with the given tag."""
    return [c for c in Contact.objects.all() if tag_name in c.tags]

def get_tagged_gifts(tag_name):
    """Return all gifts with the given tag."""
    return [g for g in Gift.objects.all() if tag_name in g.tags]

def get_tagged_campaigns(tag_name):
    """Return all campaigns with the given tag."""
    return [c for c in Campaign.objects.all() if tag_name in c.tags]

def get_tagged_notes(tag_name):
    """Return all thank-you notes with the given tag."""
    return [n for n in ThankYouNote.objects.all() if tag_name in n.tags]
