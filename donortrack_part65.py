# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: DonorTrack
import re


def merge_imports(existing: str, new_imports: list) -> str:
    """Append new imports while removing obvious duplicate lines."""
    lines = existing.splitlines()
    if not new_imports:
        return existing

    blank_count = len(lines) - len([l for l in lines if l.strip()])
    has_any_import = any(re.match(r"^\s*import\s", l) or re.match(r"^\s*from\s", l), lines)

    if not has_any_import:
        lines.append("")
        lines.append("")

    for imp in new_imports:
        imp = imp.strip()
        if not imp:
            continue
        if any(line.strip() == imp for line in lines):
            continue
        lines.append(imp)

    lines.append("")
    lines.append("")
    return "\n".join(lines[: len(lines) - blank_count])
