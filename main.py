from src.career_guidance_system import run_conversation

if __name__ == "__main__":
    print("Welcome to the AI Career Guidance System 🚀\n")
    user_input = input("Tell me about your interests, skills, and career goals:\n")
    result = run_conversation(user_input)

    print("\n🧠 Career Guidance Result:\n")
    print(result)
