from levels import level1, level2

def start_game():
    print("\n🔐 SYSTEM 1: Encrypted Password Detected...")
    success = level1.run_level()

    if success:
        print("\n✅ ACCESS GRANTED! Moving to SYSTEM 2...")
        success = level2.run_level()

    if success:
        print("\n✅ SUCCESS! You've successfully breached the system.")
    else:
        print("\n❌ SYSTEM SECURED! Better luck next time.")
