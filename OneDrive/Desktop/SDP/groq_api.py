from groq import Groq
import os

# ---------------- LOAD API KEY ----------------
def load_api_key():
    try:
        # ensures file is read from project folder
        base_dir = os.path.dirname(os.path.abspath(__file__))
        key_path = os.path.join(base_dir, "api_key.txt")

        with open(key_path, "r") as f:
            return f.read().strip()

    except FileNotFoundError:
        raise Exception("❌ api_key.txt not found in project folder")


# ---------------- CREATE CLIENT ----------------
client = Groq(api_key=load_api_key())

# Recommended stable Groq model (2026)
MODEL_NAME = "llama-3.3-70b-versatile"


# ---------------- GENERIC LLM CALL ----------------
def ask_llm(system_prompt, user_prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR: {str(e)}"
