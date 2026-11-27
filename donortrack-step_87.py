# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: DonorTrack
def normalize_report(report):
    cleaned = {}
    for key, value in report.items():
        if isinstance(value, dict):
            cleaned[key] = {k: v for k, v in value.items() if isinstance(k, str) and isinstance(v, (str, int, float))}
        else:
            cleaned[key] = value
    return cleaned


def normalize_report(report):
    if isinstance(report, list):
        return [normalize_report(item) for item in report if isinstance(item, (dict, list))]
    if isinstance(report, dict):
        return {normalize_key(key): normalize_report(value) for key, value in report.items()}
    return report


def normalize_key(key):
    return key.strip().lower()


def compare_reports(report_a, report_b):
    report_a = normalize_report(report_a)
    report_b = normalize_report(report_b)
    normalized_a = {normalize_key(k): v for k, v in report_a.items()}
    normalized_b = {normalize_key(k): v for k, v in report_b.items()}
    missing_in_b = {key: value for key, value in normalized_a.items() if key not in normalized_b}
    missing_in_a = {key: value for key, value in normalized_b.items() if key not in normalized_a}
    differences = []
    for key, value in normalized_a.items():
        if key in normalized_b:
            if value != normalized_b[key]:
                differences.append({key: value, key + "_new": normalized_b[key]})
    return {
        "missing_in_second": missing_in_b,
        "missing_in_first": missing_in_a,
        "value_differences": differences,
    }


def are_reports_equal(report_a, report_b, tolerance=1e-6):
    result = compare_reports(report_a, report_b)
    return (
        len(result["missing_in_second"]) == 0
        and len(result["missing_in_first"]) == 0
        and len(result["value_differences"]) == 0
    )


def compare_gift_totals(report_a, report_b):
    total_a = sum(gift.get("amount", 0) for gift in report_a.get("gifts", []))
    total_b = sum(gift.get("amount", 0) for gift in report_b.get("gifts", []))
    return {"total_a": total_a, "total_b": total_b, "difference": total_a - total_b}


def count_contacts(report):
    return len(report.get("contacts", []))


def count_gifts(report):
    return len(report.get("gifts", []))


def count_thank_you_notes(report):
    return len(report.get("thank_you_notes", []))


def count_campaigns(report):
    return len(report.get("campaigns", []))
