def run_level():
    print("\n🔎 Challenge: Use logical operators to break into the system.")
    print("You need to solve this boolean logic puzzle to proceed.")
    
    # Sample logic puzzle
    print("\n( A AND B ) OR ( NOT C )")
    print("A = True")
    print("B = False")
    print("C = True")

    # Asking the player for the answer
    answer = input("\nIs the expression TRUE or FALSE? (Enter True/False): ").strip().lower()

    # The correct answer
    correct_answer = (True and False) or (not True)  # Which is False
    
    if answer == str(correct_answer).lower():
        print("✅ Access Granted! You've solved the puzzle.")
        return True
    else:
        print("❌ Access Denied! Wrong answer.")
        return False
