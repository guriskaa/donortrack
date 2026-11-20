# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: DonorTrack
def compare_snapshots(before, after):
    before = dict(before)
    after = dict(after)
    keys = sorted(set(before) | set(after))
    return {
        k: {
            'added': k not in before,
            'removed': k not in after,
            'changed': k in before and k in after and before[k] != after[k],
            'old': before.get(k),
            'new': after.get(k),
        }
        for k in keys
    }


def summarize_snapshot(diff):
    items = [d for d in diff.values() if d['added'] or d['removed'] or d['changed']]
    if not items:
        return 'No changes'
    return f'{len(items)} field(s) changed: ' + ', '.join(
        f"{d['name']} {d['old'] if d['old'] is not None else ''} -> {d['new'] if d['new'] is not None else ''}"
        for d in items
    )
