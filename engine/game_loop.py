from levels import level1

def start_game():
    print("\n🔐 SYSTEM 1: Encrypted Password Detected...")
    success = level1.run_level()
    
    if success:
        print("\n✅ ACCESS GRANTED! Moving to next system...")
    else:
        print("\n❌ ACCESS DENIED! Try again later.")
