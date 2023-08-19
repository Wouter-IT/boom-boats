import sys
import os
import random
import copy
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

game_data = {
    "enemy_ships":  5,
    "player_ships": 5,
    "turn_count": 0
}

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
            elif cell == 3:
                print(" " + "H" + " ", end='') 
            elif cell == 4:
                print(" " + "M" + " ", end='')    
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
    print(f"Enemy ships intact: {game_data['enemy_ships']}    Your ships intact: {game_data['player_ships']}    Turn: {game_data['turn_count']}\n")
    picked_row = False
    while picked_row == False:
        row_coords = input("Choose a row for your next stike (A, B, C, D, E, F, G): ")
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
            print("Your input was invalid, please try again.")
            continue
    
    picked_col = False
    while picked_col == False:
        col_coords = input("Now choose a column for your next stike (1, 2, 3, 4, 5, 6, 7): ")
        try:
            col_coords_int = int(col_coords)
            if col_coords_int < 1 or col_coords_int > 7:
                print(f"Your input has to be a number between 1 to 7! Your input was: {col_coords_int}, please try again.\n")
                continue
        except ValueError:
            if col_coords == "":
                print(f"Your input has to be a number between 1 to 7! Your input was empty, please try again.\n")
                continue
            print(f"Your input has to be a number between 1 to 7! Your input was: {col_coords}, please try again.\n")
            continue
        col_coords_int -= 1
        strike_list.append(col_coords_int)
        print(strike_list)
        picked_col = True

    return strike_list

def validate_strike(target_coords, brd, owner):
    """
    Checks the input coordinates with current board state and determines if the 
    shot was hit, miss or on a ship that has already been sunk.
    """
    target_col = target_coords.pop()
    target_row = target_coords.pop()
    if brd[target_row][target_col] == 0:
        print('Miss!')
        brd[target_row][target_col] = 4
        return brd        
    if brd[target_row][target_col] == 1:
        print('Hit!')
        brd[target_row][target_col] = 3
        if owner != "Computer":
            game_data['enemy_ships'] -= 1
        else:
            game_data['player_ships'] -= 1
        return brd
    if brd[target_row][target_col] == 3:
        print('You already hit that target!')
        return brd 

def update_board(comp_brd, plyr_brd):
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
    computer_brd = copy.deepcopy(brd)
    player_brd = copy.deepcopy(brd)
    computer_brd = ship_placement(computer_brd, "Computer")
    print_brd(computer_brd, "Computer")
    player_brd = ship_placement(player_brd, user['username'])
    print_brd(player_brd, user['username'])

    # Core game loop
    ongoing = True
    while ongoing:
        target = user_turn()
        computer_brd = validate_strike(target, computer_brd, user['username'])
        update_board(computer_brd, player_brd)
        if game_data['enemy_ships'] == 0:
            ongoing == False
            print("You are victorious!")
            continue
        # computer_turn()
        if game_data['player_ships'] == 0:
            ongoing == False
            update_board(computer_brd, player_brd)
            print("You have been defeated!")
            continue
        update_board(computer_brd, player_brd)

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

