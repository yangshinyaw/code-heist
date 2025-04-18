from ai.puzzle_generator import generate_puzzle

def run_level():
    puzzle = generate_puzzle()
    print(f"🔐 SYSTEM 2: {puzzle['type']} Puzzle")
    print("🔎 Challenge: Decrypt the following message.\n")
    print(f"📄 Encrypted Message: {puzzle['encrypted']}")
    print("Hint:", "Caesar Cipher" if puzzle["type"] == "Caesar Cipher" else "It's reversed.")

    answer = input("\n📝 Your Decryption: ").strip().lower()
    if answer == puzzle["original"]:
        print("✅ Access Granted!")
        return True
    else:
        print("❌ Access Denied!")
        return False
