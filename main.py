from engine.game_loop import start_game
from assets.ascii_art import get_title_art

def main():
    print(get_title_art())
    input("Press Enter to begin your mission.")
    start_game()

if __name__ == "__main__":
    main()
