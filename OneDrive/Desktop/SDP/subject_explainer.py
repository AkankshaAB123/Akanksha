from groq_api import ask_llm

# ---------------- SYSTEM PROMPT ----------------
SYSTEM_PROMPT = """
You are an AI Professor teaching BE Engineering students.

Explain the topic using:

1. Simple Explanation
2. Real-world Example
3. Key Points (bullet points)
4. Short Summary

Keep explanation clear and beginner friendly.
"""


# ---------------- EXPLAIN FUNCTION ----------------
def explain_topic(topic):
    return ask_llm(SYSTEM_PROMPT, topic)


# ---------------- MAIN PROGRAM ----------------
def main():

    print("=" * 60)
    print("🎓 AI SUBJECT EXPLAINER")
    print("Powered by Groq API")
    print("Type 'exit' to quit")
    print("=" * 60)

    while True:
        topic = input("\nEnter topic: ")

        if topic.lower() == "exit":
            print("👋 Exiting Subject Explainer...")
            break

        print("\n📘 Explanation:\n")
        result = explain_topic(topic)
        print(result)


if __name__ == "__main__":
    main()
