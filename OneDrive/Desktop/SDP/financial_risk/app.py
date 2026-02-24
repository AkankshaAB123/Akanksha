import streamlit as st
import os
import re
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "llama-3.1-8b-instant"

# -------------------------------
# 🚨 Pattern Blocking Logic
# -------------------------------

BLOCK_PATTERNS = [
    r"should i invest in",
    r"is .* a good stock",
    r"recommend .* stock",
    r"best stock to buy",
    r"which stock should i buy",
    r"suggest .* investment",
    r"guaranteed returns",
    r"tell me where to invest"
]


def is_investment_advice_request(text):
    text = text.lower()
    for pattern in BLOCK_PATTERNS:
        if re.search(pattern, text):
            return True
    return False


# -------------------------------
# 📘 Scope-Limited Prompt
# -------------------------------

SYSTEM_PROMPT = """
You are a financial education assistant.

You are allowed to:
- Explain mutual funds
- Explain types of financial risk (market risk, credit risk, liquidity risk, etc.)
- Explain diversification
- Explain general financial concepts

You are NOT allowed to:
- Recommend specific stocks
- Suggest exact investments
- Tell users where to invest money
- Provide financial advice

If the user asks for specific investment advice,
politely refuse and redirect to general educational explanation.

Do NOT recommend specific financial instruments.
"""


DISCLAIMER = """
---
⚠️ Disclaimer:
This tool provides educational information only.
It does NOT provide financial or investment advice.
Please consult a certified financial advisor before making investment decisions.
"""


# -------------------------------
# 🧠 AI Explanation Function
# -------------------------------

def generate_explanation(user_input):

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"API Error: {str(e)}"


# -------------------------------
# 🖥️ Streamlit UI
# -------------------------------

st.set_page_config(page_title="Financial Risk Explanation Tool")

st.title("💰 Financial Risk Explanation Tool")
st.write("Educational tool explaining financial risks without giving investment advice.")

user_input = st.text_area("Ask about mutual funds, risks, or diversification:")

if st.button("Submit"):

    if not user_input.strip():
        st.warning("Please enter a question.")

    else:

        # 🚨 Pattern Blocking
        if is_investment_advice_request(user_input):
            st.error("🚫 Investment advice request detected.")
            st.write(
                "I cannot provide specific investment recommendations. "
                "However, I can explain general financial concepts like risk and diversification."
            )
            st.markdown(DISCLAIMER)

        else:
            explanation = generate_explanation(user_input)

            st.subheader("Explanation")
            st.write(explanation)

            # Auto-append disclaimer
            st.markdown(DISCLAIMER)