from groq import Groq
import os

# ---------- LOAD API KEY ----------
def load_api_key():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(base_dir, "api_key.txt")

    try:
        with open(key_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        raise Exception("❌ api_key.txt not found")


# ---------- CREATE CLIENT ----------
client = Groq(api_key=load_api_key())

MODEL_NAME = "llama-3.3-70b-versatile"


# ---------- AI CALL FUNCTION ----------
def call_ai(prompt):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Return strictly valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return response.choices[0].message.content.strip()
