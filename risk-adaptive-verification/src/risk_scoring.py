
RISK_LEVELS = {
    "low": 0,
    "medium": 1,
    "high": 2
}


def get_risk_score(predicted_risk):
    if predicted_risk not in RISK_LEVELS:
        raise ValueError(f"Unknown risk level: {predicted_risk}")

    return RISK_LEVELS[predicted_risk]


def requires_verification(predicted_risk, threshold="medium"):
    if threshold not in RISK_LEVELS:
        raise ValueError(f"Unknown threshold: {threshold}")

    return get_risk_score(predicted_risk) >= RISK_LEVELS[threshold]
