import sys
import os
from art import LOGO_TEXT, DIVIDER, BANNER, UNAME_BANNER
from settings import user

"""
Creates a list of lists with intigers assigned to it that function as tiles for the game and and display the game data.
Function call upon these list indexes to process computer and player input needed to operate the main game loop
Numbers stand for the following:
0 = empty tile
1 = ship
2 = hit ship
3 = missed shot
""" 
brd = [
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,]
]

# end= to prevent new line after print was found on EnterpriseDNA blog
# https://blog.enterprisedna.co/python-print-without-newline-easy-step-by-step-guide/#:~:text=To%20print%20without%20a%20new,")
def create_logo():
    print(LOGO_TEXT)
    print(BANNER)

def print_brd(brd, owner):
    """
    Prints the playing board with the appropriate row and column headers
    """
    print(owner + "'s broad:")
    numerals_top = f"     1  2  3  4  5  6  7  "
    border_top_bottom = f"   +---------------------+"
    print(numerals_top)
    print(border_top_bottom)
    row_count = 0
    row_capitals = [' A |', ' B |', ' C |', ' D |', ' E |', ' F |', ' G |']
    for row in brd:
        print(row_capitals[row_count], end="")
        row_count = row_count + 1
        for cell in row:
            if cell == 0:
                print(" " + "~" + " ", end='')
        print("|")    
    print(border_top_bottom + "\n")
    print(DIVIDER)

def main_gameloop():
    create_logo()
    computer_brd = brd
    player_brd = brd
    print_brd(computer_brd, "Computer")
    print_brd(player_brd, user['username'])
    # pauses client
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
        os.system('clear')
        main_gameloop()
    else:
        os.system('clear')
        print(LOGO_TEXT)
        print(UNAME_BANNER)
        print("\nThe username cannot be empty.")

