from ai_utils import call_ai

print("⚖️ Concept Comparator")
print("Type 'exit' to quit\n")


# ---------- helper function ----------
def clean_output(text):
    """
    Removes unwanted formatting like JSON/code blocks.
    """
    text = text.replace("```", "")
    text = text.replace("json", "")
    return text.strip()


# ---------- main loop ----------
while True:
    topic1 = input("Enter first concept: ")

    if topic1.lower() == "exit":
        print("👋 Exiting program...")
        break

    topic2 = input("Enter second concept: ")

    # Structured prompt for readable output
    prompt = f"""
You are an AI tutor teaching engineering students.

Compare the following concepts:
1. {topic1}
2. {topic2}

Output Rules:
- DO NOT return JSON
- DO NOT use code blocks
- Use clear headings
- Keep explanation simple and human readable

Format:

Definition:
Explain both concepts briefly.

Key Differences:
Give 3–5 bullet differences.

Simple Example:
Provide one easy real-world example.
"""

    try:
        response = call_ai(prompt)
        clean_text = clean_output(response)

        print("\n📘 Concept Comparison\n")
        print(clean_text)
        print("\n" + "-" * 55)

    except Exception as e:
        print(f"\n❌ Error: {e}")
