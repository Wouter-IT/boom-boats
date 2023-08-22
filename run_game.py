import sys
import os
import random
import copy
import time
from colorama import Fore, Style
from art import LOGO_TEXT, DIVIDER, BANNER, UNAME_BANNER
from settings import user


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
BRD = [
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,]
]

"""
Stores game data to display on screen the enemy/player ships that are left as well as the turn count.
""" 
game_data = {
    "enemy_ships":  5,
    "player_ships": 5,
    "turn_count": 0
}

# end= to prevent new line after print was found on EnterpriseDNA blog
# https://blog.enterprisedna.co/python-print-without-newline-easy-step-by-step-guide/#:~:text=To%20print%20without%20a%20new,")
def create_logo():
    """
    Prints logo and banner on screen.
    """
    print(LOGO_TEXT)
    print(BANNER)

def print_brd(brd, owner):
    """
    Prints the playing board with the appropriate row and column headers
    """
    print(BOLD + owner + "'s broad:" + RESET)
    numerals_top = BOLD + f"     1  2  3  4  5  6  7  " + RESET
    border_top_bottom = f"   +---------------------+"
    print(numerals_top)
    print(border_top_bottom)
    row_count = 0
    row_capitals = [BOLD + ' A |' + RESET, BOLD + ' B |' + RESET, BOLD + ' C |' + RESET, BOLD + ' D |' + RESET,
    BOLD + ' E |' + RESET, BOLD + ' F |' + RESET, BOLD + ' G |' + RESET]
    for row in brd:
        print(row_capitals[row_count], end="")
        row_count = row_count + 1
        for cell in row:
            if cell == 0 or cell == 1:
                print(DIM + " " + "~" + " " + RESET, end='')
            elif cell == 2:
                print(GREEN + " " + "S" + " " + RESET, end='')
            elif cell == 3:
                print(RED + " " + "H" + " " + RESET, end='') 
            elif cell == 4:
                print(CYAN + " " + "M" + " " + RESET, end='')    
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
                ship_counter += 1
    else:
        while ship_counter < 5:
            rdm_row = random.randint(0,6)
            rdm_col = random.randint(0,6)
            if owner_brd[rdm_row][rdm_col] == 0:
                    owner_brd[rdm_row][rdm_col] = 1
                    ship_counter += 1
    return owner_brd        


def user_turn():
    """
    Process user input for strike coordinates and checks if the inputs are valid, throwing an error in case they are invalid.
    Then proceeds to pack the coordinates in a list for the strike validation.
    """
    strike_list = []
    print(RED + f"Enemy ships intact: {game_data['enemy_ships']}" + RESET + GREEN + f"    Your ships intact: {game_data['player_ships']}" + RESET + f"    Turn: {game_data['turn_count']}\n")
    picked_row = False
    while picked_row == False:
        row_coords = input("Choose a row for your next strike (A, B, C, D, E, F, G): \n")
        row_coords = row_coords.lower()
        if row_coords == 'a':
                row_coords_int = 0
                strike_list.append(row_coords_int)
                picked_row = True
        elif row_coords == 'b':
                row_coords_int = 1
                strike_list.append(row_coords_int)
                picked_row = True
        elif row_coords == 'c':
                row_coords_int = 2
                strike_list.append(row_coords_int)
                picked_row = True
        elif row_coords == 'd':
                row_coords_int = 3
                strike_list.append(row_coords_int)
                picked_row = True
        elif row_coords == 'e':
                row_coords_int = 4
                strike_list.append(row_coords_int)
                picked_row = True
        elif row_coords == 'f':
                row_coords_int = 5
                strike_list.append(row_coords_int)
                picked_row = True
        elif row_coords == 'g':
                row_coords_int = 6
                strike_list.append(row_coords_int)
                picked_row = True
        else:
            print(RED + BOLD + f"Your input: '{row_coords}' was invalid, please try again." + RESET, end='\r')
            time.sleep(2)
            print(end=LINE_CLEAR)
            continue
    
    picked_col = False
    while picked_col == False:
        col_coords = input("Now choose a column for your next stike (1, 2, 3, 4, 5, 6, 7): \n")
        try:
            col_coords_int = int(col_coords)
            if col_coords_int < 1 or col_coords_int > 7:
                print(RED + BOLD + f"Your input has to be a number between 1 to 7! Your input was: '{col_coords_int}', please try again." + RESET, end='\r')
                time.sleep(2)
                print(end=LINE_CLEAR)
                continue
        except ValueError:
            if col_coords == "":
                print(RED + BOLD + f"Your input has to be a number between 1 to 7! Your input was empty, please try again." + RESET, end='\r')
                time.sleep(2)
                print(end=LINE_CLEAR)
                continue
            print(RED + BOLD + f"Your input has to be a number between 1 to 7! Your input was: '{col_coords}', please try again." + RESET, end='\r')
            time.sleep(2)
            print(end=LINE_CLEAR)
            continue
        col_coords_int -= 1
        strike_list.append(col_coords_int)
        picked_col = True

    return strike_list

def computer_turn(plyr_brd):
    """
    Processes the computers turn, randomly chooses target, validates if it is a valid target, 
    and then proceeds to register the strike on the player_brd.
    """
    # Select tile to strike and validate target.
    strike_valid = False
    valid_comp_strike = False
    while valid_comp_strike == False:
        rdm_strike_row = random.randint(0,6)
        print(rdm_strike_row)
        rdm_strike_col = random.randint(0,6)
        print(rdm_strike_col)
        print(plyr_brd[rdm_strike_row][rdm_strike_col])
        if plyr_brd[rdm_strike_row][rdm_strike_col] != 3 and plyr_brd[rdm_strike_row][rdm_strike_col] != 4:
            valid_comp_strike == True
            strike_valid = True
            break
    # Process valid strike
    if strike_valid == True:
        if plyr_brd[rdm_strike_row][rdm_strike_col] == 0:
            plyr_brd[rdm_strike_row][rdm_strike_col] = 4
        elif plyr_brd[rdm_strike_row][rdm_strike_col] == 2:
            plyr_brd[rdm_strike_row][rdm_strike_col] = 3
            game_data['player_ships'] -= 1
    
    return plyr_brd

def validate_strike(target_coords, brd, owner):
    """
    Checks the input coordinates with current board state and determines if the 
    shot was hit, miss or on a ship that has already been sunk.
    """
    target_col = target_coords.pop()
    target_row = target_coords.pop()
    if brd[target_row][target_col] == 0:
        print('You shoot..')
        time.sleep(1)
        print(CYAN + 'Miss!' + RESET)
        time.sleep(1)
        brd[target_row][target_col] = 4
        return brd        
    if brd[target_row][target_col] == 1:
        print('You shoot..')
        time.sleep(1)
        print(RED + 'Hit!!' + RESET)
        time.sleep(1)
        brd[target_row][target_col] = 3
        if owner != "Computer":
            game_data['enemy_ships'] -= 1
        else:
            game_data['player_ships'] -= 1
        return brd
    if brd[target_row][target_col] == 3:
        print(RED + BOLD + 'You already hit that target!' + RESET)
        time.sleep(2)
        return brd 
    if brd[target_row][target_col] == 4:
        print(CYAN + BOLD + 'You already struck this tile! Nothing but water here.' + RESET)
        time.sleep(2)
        return brd 

def update_board(comp_brd, plyr_brd):
    """
    Updates the gameboard with all current strikes processed.
    """
    os.system('clear')
    create_logo()
    print_brd(comp_brd, "Computer")
    print_brd(plyr_brd, user['username'])

def main_gameloop():
    """
    Executes the main game loop
    """
    #Creates visuals and distributes ships on player and computer board
    create_logo()
    # copy.deepcopy bug fix for copying the reference to the entitiy 'brd' as opposed to the actual list of lists. Found on stack Overflow by user Felix King
    # https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment
    computer_brd = copy.deepcopy(BRD)
    player_brd = copy.deepcopy(BRD)
    computer_brd = ship_placement(computer_brd, "Computer")
    print_brd(computer_brd, "Computer")
    player_brd = ship_placement(player_brd, user['username'])
    print_brd(player_brd, user['username'])

    # Core game loop
    ongoing = True
    while ongoing:
        game_data['turn_count'] += 1
        target = user_turn()
        computer_brd = validate_strike(target, computer_brd, user['username'])
        update_board(computer_brd, player_brd)
        if game_data['enemy_ships'] == 0:
            ongoing == False
            print("You are victorious!")
            enter = input('Press Enter to continue\n')
            continue
        player_brd = computer_turn(player_brd)
        if game_data['player_ships'] == 0:
            ongoing == False
            update_board(computer_brd, player_brd)
            print("You have been defeated!")
            enter = input('Press Enter to continue\n')
            continue
        update_board(computer_brd, player_brd)

    # pauses gameclient
    something = input('type something\n')

def uname_registration():
    """
    Requests a username from the player and registers the input to the user data dictionary
    """
    valid_input = False
    while valid_input == False:
        os.system('clear')
        print(LOGO_TEXT)
        print(UNAME_BANNER)
        username_input = input("\nAdmiral, please choose a username. It has to be at least 1 character long:\n")
        if username_input != "":
            valid_input = True
            user['username'] = username_input
            os.system('clear')
            main_gameloop()
        else:
            os.system('clear')
            print(LOGO_TEXT)
            print(UNAME_BANNER)
            print(RED + BOLD + "\nThe username cannot be empty." + RESET, end='\r')
            time.sleep(2)
            print(LINE_CLEAR)

