import sys
import os
import random
from art import LOGO_TEXT, DIVIDER, BANNER, UNAME_BANNER
from settings import user

"""
Creates a list of lists with intigers assigned to it that function as tiles for the game and and display the game data.
Function call upon these list indexes to process computer and player input needed to operate the main game loop
Numbers stand for the following:
0 = empty tile
1 = computer hidden ship
2 = player ship
3 = hit ship
4 = missed shot
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
            if cell == 0 or cell == 1:
                print(" " + "~" + " ", end='')
            elif cell == 2:
                print(" " + "S" + " ", end='')
        print("|")    
    print(border_top_bottom + "\n")
    print(DIVIDER)

def ship_placement(owner_brd, owner):
    """
    Places ships on computer and player board an verifies if there isn't already a ship on the given tile.
    """
    ship_counter = 0
    if owner != "Computer":
        while ship_counter < 5:
            # Random nr generation found on W3Schools
            #https://www.w3schools.com/python/ref_random_randint.asp
            rdm_row = random.randint(0,6)
            rdm_col = random.randint(0,6)
            if owner_brd[rdm_row][rdm_col] == 0:
                owner_brd[rdm_row][rdm_col] = 2
                ship_counter = ship_counter + 1
    else:
        while ship_counter < 5:
            rdm_row = random.randint(0,6)
            rdm_col = random.randint(0,6)
            if owner_brd[rdm_row][rdm_col] == 0:
                    owner_brd[rdm_row][rdm_col] = 1
                    ship_counter = ship_counter + 1
    return owner_brd        

def main_gameloop():
    """
    Executes the main game loop
    """
    create_logo()
    computer_brd = brd
    player_brd = brd

    computer_brd = ship_placement(computer_brd, "Computer")
    player_brd = ship_placement(player_brd, user['username'])
    print_brd(computer_brd, "Computer")
    print_brd(player_brd, user['username'])
    # pauses gameclient

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

