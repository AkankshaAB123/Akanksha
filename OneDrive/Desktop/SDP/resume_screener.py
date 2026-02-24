import json
from ai_utils import call_ai


# ---------------- AI SCREENING ----------------
def screen_resume(resume_text):

    prompt = f"""
You are an HR AI assistant.

Extract the following from the resume:
- candidate_name
- skills (list)
- years_experience (number)
- suggested_role
- suitability_score (0-10)

Return STRICTLY valid JSON only.
No explanation.
Do NOT use markdown formatting.

Resume:
{resume_text}
"""

    response = call_ai(prompt)

    print("\n--- RAW AI RESPONSE ---")
    print(response)

    # ✅ CLEAN RESPONSE
    cleaned = (
        response.replace("```json", "")
                .replace("```", "")
                .strip()
    )

    try:
        data = json.loads(cleaned)
        validated = validate_resume(data)

        # Convert to human readable output
        if isinstance(validated, dict):
            return format_resume_output(validated)
        else:
            return validated

    except json.JSONDecodeError as e:
        print("\nDEBUG CLEANED RESPONSE:\n", cleaned)
        return f"❌ Invalid JSON returned by AI.\nError: {e}"


# ---------------- VALIDATION ----------------
def validate_resume(data):

    required_fields = [
        "candidate_name",
        "skills",
        "years_experience",
        "suggested_role",
        "suitability_score"
    ]

    for field in required_fields:
        if field not in data:
            return f"❌ Missing field: {field}"

    if not isinstance(data["skills"], list):
        return "❌ Skills must be a list"

    if not isinstance(data["years_experience"], (int, float)):
        return "❌ Experience must be number"

    if not (0 <= data["suitability_score"] <= 10):
        return "❌ Score must be between 0 and 10"

    return data


# ---------------- HUMAN READABLE FORMAT ----------------
def format_resume_output(data):

    skills = ", ".join(data["skills"])

    # Score interpretation
    score = data["suitability_score"]

    if score >= 8:
        verdict = "✅ Strong Candidate"
    elif score >= 5:
        verdict = "⚠️ Moderate Fit"
    else:
        verdict = "❌ Needs Improvement"

    output = f"""
👤 Candidate Evaluation Report
----------------------------------------
Name                : {data['candidate_name']}
Suggested Role      : {data['suggested_role']}
Experience          : {data['years_experience']} years

🧠 Key Skills
{skills}

📊 Suitability Score : {score}/10
HR Verdict          : {verdict}
----------------------------------------
"""

    return output.strip()


# ---------------- MULTI-LINE INPUT ----------------
def get_multiline_input():

    print("Paste resume text below.")
    print("Type 'END' on a new line when finished.\n")

    lines = []

    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    return "\n".join(lines)


# ---------------- MAIN ----------------
if __name__ == "__main__":

    print("📄 AI Resume Screener\n")

    resume = get_multiline_input()

    result = screen_resume(resume)

    print("\n--- FINAL OUTPUT ---\n")
    print(result)
