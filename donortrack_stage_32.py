# === Stage 32: Add pagination helpers for long console output ===
# Project: DonorTrack
def paginate(lines, page_size=20):
    for start in range(0, len(lines), page_size):
        chunk = lines[start:start + page_size]
        print(f"\n--- Page {start // page_size + 1} ---")
        for line in chunk:
            print(line)
    if len(lines) > page_size:
        print(f"\n[Total {len(lines)} lines. Showing first {len(lines) // page_size + (1 if len(lines) % page_size else 0)} pages.]")
