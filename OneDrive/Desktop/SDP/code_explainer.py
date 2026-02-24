from ai_utils import call_ai

print("💻 AI Code Explainer")
print("Paste Python code (type END to finish)")
print("Type EXIT to quit program\n")


# ---------- CLEAN OUTPUT ----------
def clean_output(text):
    """
    Removes markdown/code block formatting
    to keep output human readable.
    """
    text = text.replace("```python", "")
    text = text.replace("```", "")
    return text.strip()


# ---------- READ MULTILINE CODE ----------
def read_code():
    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        if line.strip().upper() == "EXIT":
            return None

        lines.append(line)

    return "\n".join(lines)


# ---------- MAIN LOOP ----------
while True:

    code = read_code()

    if code is None:
        print("\n👋 Exiting Code Explainer...")
        break

    # Structured prompt for readable explanation
    prompt = f"""
You are a programming tutor teaching beginner engineering students.

Explain the following Python code in a HUMAN READABLE way.

Rules:
- Do NOT return JSON
- Do NOT use markdown code blocks
- Use simple language
- Explain step-by-step

Format output as:

1. What this program does
2. Step-by-step explanation
3. Important concepts used
4. Simple real-world analogy

Python Code:
{code}
"""

    try:
        response = call_ai(prompt)
        explanation = clean_output(response)

        print("\n🧠 Code Explanation\n")
        print(explanation)
        print("\n" + "-" * 60)

    except Exception as e:
        print(f"\n❌ Error: {e}")
