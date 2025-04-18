from levels import level1, level2, level3, level4
from story.mission_script import intro_story, outro_story
from assets.ascii_art import get_access_granted, get_access_denied

def start_game():
    print(intro_story())

    success = level1.run_level()
    if success:
        print("\n✅ LEVEL 1 BREACHED... Proceeding to Internal Chat.")
        success = level2.run_level()

    if success:
        print("\n✅ LEVEL 2 BREACHED... Bypassing Logic Firewall.")
        success = level3.run_level()

    if success:
        print("\n✅ LEVEL 3 BREACHED... Entering CORE DATA MAZE.")
        success = level4.run_level()

    print(outro_story(success))
    print(get_access_granted() if success else get_access_denied())
