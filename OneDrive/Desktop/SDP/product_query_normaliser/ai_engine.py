import os
import json
import re
from groq import Groq
from dotenv import load_dotenv
from guardrails import extract_numeric_budget, validate_budget

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Use updated supported model
MODEL_NAME = "llama-3.1-8b-instant"


SCHEMA_PROMPT = """
You are a strict JSON generator for an e-commerce platform.

IMPORTANT RULES:
- Return ONLY valid JSON.
- Do NOT add explanations.
- Do NOT add markdown formatting.
- Do NOT add ```json.
- Output must start with { and end with }.
- Do NOT guess missing information.

Schema:

{
  "product_type": "",
  "price_range": {
      "min": null,
      "max": null
  },
  "usage_context": "",
  "feature_preferences": [],
  "missing_fields": []
}

Rules:
- If budget mentioned like 4k → max = 4000
- If vague terms like "cheap" → add "price_range" to missing_fields
- If product type unclear → add "product_type" to missing_fields
- If usage context missing → add "usage_context" to missing_fields
- Always return valid JSON only.

User Query:
"""


def extract_json_from_text(text):
    """
    Safely extract JSON object from model output.
    """
    try:
        return json.loads(text)
    except:
        try:
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            return None
    return None


def normalize_query(user_input: str):

    prompt = SCHEMA_PROMPT + f'"{user_input}"'

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
    except Exception as e:
        return None, True, f"API Error: {str(e)}"

    raw_output = response.choices[0].message.content.strip()

    result = extract_json_from_text(raw_output)

    if result is None:
        return None, True, "Parsing error. Model did not return valid JSON."

    # 🔹 Budget Validation Logic
    numeric_budget = extract_numeric_budget(user_input)

    if numeric_budget:
        is_valid, message = validate_budget(numeric_budget)

        if not is_valid:
            return None, True, message

        # Enforce model consistency
        result["price_range"]["max"] = numeric_budget

    needs_clarification = len(result.get("missing_fields", [])) > 0

    return result, needs_clarification, None


def generate_clarification(missing_fields: list):

    questions = {
        "product_type": "What type of product are you looking for?",
        "price_range": "What is your budget range?",
        "usage_context": "Where or how will you use this product?",
        "feature_preferences": "Any specific features you prefer?"
    }

    clarification_questions = []

    for field in missing_fields:
        if field in questions:
            clarification_questions.append(questions[field])

    return "\n".join(clarification_questions)