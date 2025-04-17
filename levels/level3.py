import re

def run_level():
    print("\n🔎 Challenge: Solve the Regex puzzle to break into the system.")
    print("Match the correct pattern to proceed.")

    # Simple regex pattern for matching an email address
    print("\nRegex Pattern: Match a valid email address.")
    print("For example: someone@example.com")

    # Sample input string
    email = "test.email@domain.com"

    # Regex pattern for basic email validation
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    # Ask the player for input
    answer = input("\nEnter the email address you think matches the pattern: ").strip()

    # Check if the input matches the regex pattern
    if re.match(pattern, answer):
        print("✅ Access Granted! You've solved the regex puzzle.")
        return True
    else:
        print("❌ Access Denied! The pattern doesn't match.")
        return False
