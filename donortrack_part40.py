# === Stage 40: Add plain text report export ===
# Project: DonorTrack
def export_report(records, fields=('id','name','email','phone','gift','campaign','note','date','status')):
    lines = []
    for r in records:
        vals = []
        for f in fields:
            vals.append(getattr(r, f, None))
        lines.append('\t'.join(str(v) for v in vals))
    return '\n'.join(lines)
