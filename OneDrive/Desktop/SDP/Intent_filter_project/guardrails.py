def apply_guardrails(classification, user_input):
    intent = classification.get("intent")
    risk = classification.get("risk_level")

    if risk == "high" or intent == "assignment_answer":
        return {
            "allowed": False,
            "message": "⚠️ I can help explain the concept, but I cannot generate direct assignment answers."
        }

    if intent == "mixed":
        return {
            "allowed": True,
            "partial": True
        }

    return {
        "allowed": True,
        "partial": False
    }

