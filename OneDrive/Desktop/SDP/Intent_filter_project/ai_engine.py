import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"

def classify_intent(user_input):
    prompt = f"""
You are an academic integrity classifier.

Classify the student request into:
1. concept_explanation
2. assignment_answer
3. mixed
4. unclear

Return STRICT JSON:
{{
 "intent": "",
 "risk_level": "low | medium | high",
 "confidence": "0-1",
 "reason": ""
}}

Student request:
{user_input}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {
            "intent": "unknown",
            "risk_level": "high",
            "confidence": 0,
            "reason": "Invalid JSON from model"
        }

def generate_explanation(user_input):
    prompt = f"""
You are a tutor.
Explain the concept clearly.
Do NOT generate assignment answers.
Keep it educational.

Student query:
{user_input}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content

