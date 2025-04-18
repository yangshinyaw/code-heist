from levels import level1, level2, level3, level4
from assets.ascii_art import get_access_granted, get_access_denied

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

    print("\n" + ("🎉 MISSION COMPLETE!" if success else "💀 MISSION FAILED..."))
    print(get_access_granted() if success else get_access_denied())
