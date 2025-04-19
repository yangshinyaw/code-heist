from ai.hf_riddles import generate_riddle_hf

def run_level():
    print("🧠 SYSTEM 3: Hugging Face AI RIDDLE")

    riddle, answer = generate_riddle_hf()
    if not riddle:
        print("⚠️ AI Riddle failed. Skipping...")
        return False

    print(f"\n🤖 Riddle: {riddle}")
    guess = input("\n📝 Your Answer: ").strip().lower()

    if guess == answer:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Incorrect. The right answer was: {answer}")
        return False
