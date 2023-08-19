import sys
import os
from art import LOGO_TEXT, DIVIDER, BANNER, UNAME_BANNER
from settings import user


# end= to prevent new line after print was found on EnterpriseDNA blog
# https://blog.enterprisedna.co/python-print-without-newline-easy-step-by-step-guide/#:~:text=To%20print%20without%20a%20new,")
def create_brd():
    """
    Prints the Logo text, banner, and creates a playing board with the appropriate row and column headers
    """
    os.system('clear')
    print(LOGO_TEXT)
    print(BANNER)
    numerals_top = f"\n     1  2  3  4  5  6  7  "
    border_top_bottom = f"   +---------------------+"
    brd = [
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [8, 0, 0, 0, 0, 0, 0, 0, 9]
    ]
    print(numerals_top)
    print(border_top_bottom)
    
    row_count = 0
    row_capitals = [' A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ']
    for row in brd:
        print(row_capitals[row_count], end="")
        row_count = row_count + 1
        for cell in row:
            if cell == 0:
                print(" " + "~" + " ", end='')
            elif cell == 8:
                print("|", end="")    
            elif cell == 9:
                print("|")
    print(border_top_bottom)
    something = input('type something')



def uname_registration():
    """
    Requests a username from the player and registers the input to the user data dictionary
    """
    os.system('clear')
    print(LOGO_TEXT)
    print(UNAME_BANNER)
    username_input = input("\nAdmiral, please choose a username. It has to be at least 1 character long:\n")
    if username_input != "":
        user['username'] = username_input
        create_brd()
    else:
        os.system('clear')
        print(LOGO_TEXT)
        print(UNAME_BANNER)
        print("\nThe username cannot be empty.")
