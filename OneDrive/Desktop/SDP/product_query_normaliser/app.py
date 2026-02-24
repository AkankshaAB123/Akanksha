import streamlit as st
import json
import pandas as pd
from ai_engine import normalize_query, generate_clarification
from logger import log_attempt, init_log

init_log()

st.set_page_config(page_title="Product Query Normalizer")

st.title("🛒 Product Query Normalizer")
st.write("Converts vague shopping queries into structured product data.")

# Sidebar Logs
st.sidebar.title("Admin Panel")

if st.sidebar.checkbox("View Logs"):
    try:
        with open("audit_log.json", "r") as f:
            logs = json.load(f)
        df = pd.DataFrame(logs)
        st.sidebar.dataframe(df)
    except:
        st.sidebar.write("No logs available.")


user_input = st.text_area("Enter your product search:")

if st.button("Normalize"):
    if not user_input.strip():
        st.warning("Please enter a product query.")
    else:
        structured_data, needs_clarification, error = normalize_query(user_input)

        if error:
            st.error(error)

        elif needs_clarification:
            st.warning("Missing information detected.")
            questions = generate_clarification(
                structured_data.get("missing_fields", [])
            )
            st.write("Please clarify:")
            st.write(questions)

        else:
            st.success("Structured Query Extracted Successfully ✅")
            st.json(structured_data)

        log_attempt({
            "raw_query": user_input,
            "structured_output": structured_data,
            "needs_clarification": needs_clarification
        })