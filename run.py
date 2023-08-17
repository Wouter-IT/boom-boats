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

# Reused code from the Love Sandwiches assignment    
def validate_input(input):
    try:
        input_int = int(input)
        if input_int > 4 or input_int <= 0:
            print(f"Your input has to be a number 1 to 4! Your input was: {input}, please try again.\n")
            return False
    except ValueError:
        if input == "":
            print("Your input has to be a number 1 to 4! Your input was empty, please try again.\n")
            return False
        print(f"Your input has to be a number 1 to 4! Your input was: {input}, please try again.\n")
        return False
    return True


def load_main_menu_nav():
    """
    Clears screen and loads the main menu.
    """
    os.system('clear')
    while True:
        print(LOGO_TEXT)
        print(MENU_BANNER)
        print(f'''
        1. Play Game
        2. Rules
        3. Leaderboards
        4. Quit Game
        ''')
        print(DIVIDER)
        # Reused code from the Love Sandwiches assignment
        nav_input= input("Choose a number between 1 and 4 and press 'Enter' to navigate: ")
        if validate_input(nav_input):
            print('THIS IS VALID')
        else:
            print('THIS IS AN ERROR')


def main():
    """
    Run all program functions
    """
    # load_game()
    nav = load_main_menu_nav()


main()

