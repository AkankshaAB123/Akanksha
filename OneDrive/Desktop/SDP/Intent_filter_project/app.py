import streamlit as st
from ai_engine import classify_intent, generate_explanation
from guardrails import apply_guardrails
from logger import log_attempt

st.set_page_config(page_title="Intent Filter AI")

st.title("🎓 Intelligent Assignment Intent Filter")

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

user_input = st.text_area("Enter your academic question:")

if st.button("Submit"):

    st.session_state.attempts += 1

    classification = classify_intent(user_input)
    log_attempt(user_input, classification)

    st.subheader("🔍 Classification Result")
    st.json(classification)

    guard = apply_guardrails(classification, user_input)

    if not guard["allowed"]:
        st.error(guard["message"])
    else:
        explanation = generate_explanation(user_input)
        st.success("📘 Concept Support:")
        st.write(explanation)

    if st.session_state.attempts > 5:
        st.warning("Usage limit reached. Please slow down.")

