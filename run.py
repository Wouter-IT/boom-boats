import sys 
import gspread
import time
import os
from google.oauth2.service_account import Credentials
from colorama import Fore, Style
from art import LOGO, LOGO_TEXT, MENU_BANNER, DIVIDER, RULES_BANNER, BANNER, LDB_BANNER
from run_game import uname_registration

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS =  Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bb_leaderboard')

# Use of color came from Code Institute student kpetrauskas92 and his project Fury
# https://github.com/kpetrauskas92/fury-p3/blob/main/game/game.py
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
DIM = Style.DIM
RESET = Style.RESET_ALL

#LINE_CLEAR and the use of ANSI code comes from itnext.io and is used to remove error messages after a few seconds.
# https://itnext.io/overwrite-previously-printed-lines-4218a9563527
LINE_CLEAR = '\x1b[2K'
LINE_UP = '\033[1A'

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

def clear_screen():
    os.system('cls')
    os.system('clear')

def load_rules(origin):
    '''
    Loads the game rules on screen.
    '''
    clear_screen()
    print(LOGO_TEXT)
    print(RULES_BANNER)
    print(BOLD + f'''
    - Your goal is to destory all enemy ships.
    - Each player has 5 ships and all ships only cover 1 tile.
    - Shoot a target by choosing a row (letter) and a column (number).
    - You score 10 points for every hit, lose 5 points for every hit on you.
    - You earn bonus points for high accuracy (hitting most of your shots).
    - Hits are marked with a red "H", Miss with a blue "M", 
    - Your ships with a green "S", unknown sea tiles with a dim "~".
    - The game ends when all ships of a player are sunk.
    ''' + RESET)
    print(BANNER)
    
    if origin == "menu":
        press_enter = input('Press "Enter" to return to the menu.\n')
    else:
        press_enter = input('Press "Enter" to proceed to username registration.\n')

def view_rules():
    """
    Checks if user wants to view the rules before playing, and if yes, displays rules on screen.
    """
    chosen = False
    while chosen == False:
        clear_screen()
        print(LOGO_TEXT)
        print(BANNER)
        rules_answer = input('Would you like to see the rules before playing? (y/n)\n')
        if rules_answer.lower() == "y":
            chosen = True
            return True
        elif rules_answer.lower() == "n":
            chosen = True
            return False
        else:
            print(RED + BOLD + f"{rules_answer} is not a valid answer." + RESET, end='\r')
            time.sleep(1.2)
            print(LINE_CLEAR)

def load_game():
    """
    Displays logo and game name and simulates the game loading with immersive text greeting the player as the admiral of a naval fleet.
    """
    clear_screen()
    print(LOGO)
    typewriter("Greetings admiral, we were expecting you.\n")
    typewriter("Our fleet is ready for deployment.\n")
    typewriter("Game initializing in.\n")
    typewriter("3...\n")
    typewriter("2...\n")
    typewriter("1...\n")


# Gspread official documentation used to select worksheet, create a list of dictionaries.
# https://docs.gspread.org/en/latest/user-guide.html#selecting-a-worksheet
def load_leaderboard():
    clear_screen()
    print(LOGO_TEXT)
    print(LDB_BANNER)

    ldb_sheet = SHEET.worksheet('leaderboard')
    unsorted_scores = ldb_sheet.get_all_records()
    sorted_scores = sorted(unsorted_scores, key=lambda U_S: U_S['Score'], reverse=True)
    print(f'{sorted_scores}')
    wait = input("Waiting")
    

# Reused code from the Love Sandwiches assignment    
def validate_input_int(user_input):
    """
    Validates user input by checking if it is an Int. Also returns a specific message for an empty string.
    """
    try:
        input_int = int(user_input)
        if input_int > 4 or input_int <= 0:
            print(RED + BOLD + f"Your input has to be a number 1 to 4! Your input was: {user_input}, please try again.\n" + RESET)
            time.sleep(2)
            return False
    except ValueError:
        if user_input == "":
            print(RED + BOLD + "Your input has to be a number 1 to 4! Your input was empty, please try again.\n"  + RESET)
            time.sleep(2)
            return False
        print(RED + BOLD + f"Your input has to be a number 1 to 4! Your input was: {user_input}, please try again.\n"  + RESET)
        time.sleep(2)
        return False
    return True

def confirm_quit(user_input):
    """
    Validates the user input and checks whether it is yes or no. Prints a message accordingly and terminates or continues the program.
    """
    if user_input.lower() == "y":
        typewriter('Click the "Restart Game" button to reboot the game.\n')
        typewriter('Terminating program..\n')
        return True
    elif user_input.lower() == "n":
        typewriter('Returning to menu..\n')
        return False
    else:
        typewriter(RED + BOLD + 'Invalid input, returning to menu..\n' + RESET)
        return False


def load_main_menu_nav():
    """
    Clears screen and loads the main menu and awaits user input for navigation.
    """
    while True:
        clear_screen()
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
        if validate_input_int(nav_input):
            nav_input_int = int(nav_input)
            if nav_input_int == 1:
                rules_before_play = view_rules()
                if rules_before_play:
                    load_rules("play")
                uname_registration()
            elif nav_input_int == 2:
                load_rules("menu")
            elif nav_input_int == 3:
                load_leaderboard()
            elif nav_input_int == 4:
                confirm = input('Are you certain you want to quit? Yes or no (y/n): \n')
                if confirm_quit(confirm):
                    return False
            else:
                print(RED + BOLD + 'Error, invalid input' + RESET)
    


def main():
    """
    Run all program functions
    """
    #load_game()
    nav = load_main_menu_nav()

main()

