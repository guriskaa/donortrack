# === Stage 31: Add compact table rendering for long lists ===
# Project: DonorTrack
def render_compact_table(headers, rows):
    """Render a compact table suitable for long lists."""
    if not headers:
        return ""
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))
    lines = []
    lines.append(" | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers)))
    lines.append("-+-".join("-" * w for w in col_widths))
    for row in rows:
        lines.append(" | ".join(str(v).ljust(col_widths[i]) for i, v in enumerate(row)))
    return "\n".join(lines)
