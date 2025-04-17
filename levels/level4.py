def run_level():
    print("\n🔎 Challenge: Decode the number pattern to access the system.")
    print("The sequence follows the Fibonacci pattern.")

    # Fibonacci sequence
    sequence = [13, 8, 21, 34]

    # Ask the player for the next number
    print(f"\nPattern: {sequence}")
    answer = input("\nWhat’s the next number in the sequence? ").strip()

    # Calculate the correct answer (Fibonacci)
    correct_answer = sequence[-2] + sequence[-1]

    if int(answer) == correct_answer:
        print("✅ Access Granted! You've cracked the pattern.")
        return True
    else:
        print(f"❌ Access Denied! The correct answer is {correct_answer}.")
        return False
