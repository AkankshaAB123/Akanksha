from groq_api import ask_llm

SYSTEM_PROMPT = """
You are an expert Technical Interviewer for top MNCs like Google, TCS, and Infosys.

For the given job role or topic, provide:
1. 3 Common Technical Questions.
2. 1 Behavioral (HR) Question.
3. A 'Golden Tip' for the candidate to stand out.

Keep the tone professional and challenging.
"""

def generate_interview(topic):
    return ask_llm(SYSTEM_PROMPT, f"Generate interview questions for: {topic}")

def main():
    print("=" * 60)
    print("💼 AI INTERVIEW PREP BOT")
    print("Powered by Groq API")
    print("Type 'exit' to quit")
    print("=" * 60)

    while True:
        topic = input("\nEnter Role or Tech Stack (e.g., Java Developer): ")

        if topic.lower() == "exit":
            print("👋 Good luck with your placements!")
            break

        print("\n📝 Interview Questions & Tips:\n")
        result = generate_interview(topic)
        print(result)

if __name__ == "__main__":
    main()