def calculate_confidence(data):
    score = 100

    if not data.get("symptoms"):
        score -= 25
    if not data.get("duration"):
        score -= 25
    if not data.get("risk_flags"):
        score -= 25

    return max(score, 0)