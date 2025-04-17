from levels import level1, level2, level3, level4

def start_game():
    print("\n🔐 SYSTEM 1: Encrypted Password Detected...")
    success = level1.run_level()

    if success:
        print("\n✅ ACCESS GRANTED! Moving to SYSTEM 2...")
        success = level2.run_level()

    if success:
        print("\n✅ ACCESS GRANTED! Moving to SYSTEM 3...")
        success = level3.run_level()

    if success:
        print("\n✅ ACCESS GRANTED! Moving to SYSTEM 4...")
        success = level4.run_level()

    if success:
        print("\n🎉 CONGRATULATIONS! You've successfully breached all systems.")
    else:
        print("\n❌ SYSTEM SECURED! You failed the mission. Better luck next time.")
