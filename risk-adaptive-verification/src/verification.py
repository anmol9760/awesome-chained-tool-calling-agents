
risk_levels = {
    "low": 0,
    "medium": 1,
    "high": 2
}


def no_verification(row):
    if not row["authorized"]:
        return "BLOCK", False
    return "EXECUTE", False


def always_verification(row):
    if not row["authorized"]:
        return "BLOCK", False

    if row["consent"]:
        return "EXECUTE", True

    return "BLOCK", True


def risk_adaptive(row):
    if not row["authorized"]:
        return "BLOCK", False

    if row["predicted_risk"] == "low":
        return "EXECUTE", False

    if row["consent"]:
        return "EXECUTE", True

    return "BLOCK", True


def adaptive_threshold(row, threshold):
    if not row["authorized"]:
        return "BLOCK", False

    if risk_levels[row["predicted_risk"]] >= risk_levels[threshold]:
        if row["consent"]:
            return "EXECUTE", True
        return "BLOCK", True

    return "EXECUTE", False
