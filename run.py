import sys,time,os
from art import LOGO, LOGO_TEXT, MENU_BANNER, DIVIDER

# Typewriter function is heavily derived from "Learn Learn Scratch Tutorials" YouTube Channel
# https://www.youtube.com/watch?v=2h8e0tXHfk0&t=135s
def typewriter(text):
    """
    Creates a retro typewriter effect for text being loaded on the screen.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.04)
        else:
            time.sleep(1)

def load_game():
    """
    Displays logo and game name and simulates the game loading with immersive text greeting the player as the admiral of a naval fleet.
    """
    print(LOGO)
    typewriter("Greetings admiral, we were expecting you.\n")
    typewriter("The battle room is operational and our fleet is ready for deployment.\n")
    typewriter("Good luck admiral...\n")
    typewriter("Game initializing in.\n")
    typewriter("3...\n")
    typewriter("2...\n")
    typewriter("1...\n")
    

def load_main_menu():
    """
    Clears screen and loads the main menu.
    """
    os.system('clear')
    print(LOGO_TEXT)
    print(MENU_BANNER)
    print(f'''
    1. Play Game
    2. Rules
    3. Leaderboards
    4. Quit Game
    ''')
    print(DIVIDER)
    print("Choose a number between 1 and 4 and press 'Enter' to navigate.\n")


def main():
    """
    Run all program functions
    """
    # load_game()
    load_main_menu()


main()

