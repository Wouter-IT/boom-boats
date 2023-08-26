import sys
import gspread
import time
import os
import random
import copy
from google.oauth2.service_account import Credentials
from colorama import Fore, Style
from art import LOGO_TEXT, DIVIDER, BANNER, UNAME_BANNER
from settings import user, BRD, game_data

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bb_leaderboard')

# Use of color came from Code Institute student kpetrauskas92 and
# his project "Fury".
# https://github.com/kpetrauskas92/fury-p3/blob/main/game/game.py
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
DIM = Style.DIM
RESET = Style.RESET_ALL

# LINE_CLEAR and the use of ANSI code comes from itnext.io and is used to
# remove error messages after a few seconds.
# https://itnext.io/overwrite-previously-printed-lines-4218a9563527
LINE_CLEAR = '\x1b[2K'
LINE_UP = '\033[1A'


def clear_screen():
    '''
    Clears the screen
    '''
    os.system('clear')


def create_logo():
    """
    Prints logo and banner on screen.
    """
    print(LOGO_TEXT)
    print(BANNER)


# end= to prevent new line after print was found on EnterpriseDNA blog
# https://blog.enterprisedna.co/python-print-without-newline-easy-step-by-step-guide/#:~:text=To%20print%20without%20a%20new,")
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
    row_capitals = [BOLD + ' A |' + RESET, BOLD + ' B |' + RESET,
                    BOLD + ' C |' + RESET, BOLD + ' D |' + RESET,
                    BOLD + ' E |' + RESET, BOLD + ' F |' + RESET,
                    BOLD + ' G |' + RESET]
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
    Places ships on computer and player board an verifies if
    there isn't already a ship on the given tile.
    """
    ship_counter = 0
    if owner != "Computer":
        while ship_counter < 5:
            # Random nr generation found on W3Schools
            # https://www.w3schools.com/python/ref_random_randint.asp
            rdm_row = random.randint(0, 6)
            rdm_col = random.randint(0, 6)
            if owner_brd[rdm_row][rdm_col] == 0:
                owner_brd[rdm_row][rdm_col] = 2
                ship_counter += 1
    else:
        while ship_counter < 5:
            rdm_row = random.randint(0, 6)
            rdm_col = random.randint(0, 6)
            if owner_brd[rdm_row][rdm_col] == 0:
                owner_brd[rdm_row][rdm_col] = 1
                ship_counter += 1
    return owner_brd


def user_turn():
    """
    Process user input for strike coordinates and checks if
    the inputs are valid, throwing an error in case they are
    invalid. Then proceeds to pack the coordinates in a list
    for the strike validation.
    """
    strike_list = []
    print(RED + f"Enemy ships intact: " + RESET, end="")
    print(RED + f"{game_data['enemy_ships']}" + RESET, end="")
    print(GREEN + f"    Your ships intact: " + RESET, end="")
    print(GREEN + f"{game_data['player_ships']}" + RESET, end="")
    print(f"    Score: {user['score']}", end="")
    print(f"    Turn: {game_data['turn_count']}\n")

    picked_row = False
    while picked_row is False:
        print("Choose a row for your next strike", end="")
        row_coords = input("(A, B, C, D, E, F, G): \n")
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
            print(RED + BOLD + f"Your input: '{row_coords}' " + RESET, end="")
            print(RED + BOLD + f"is invalid, please retry." + RESET, end='\r')
            time.sleep(2)
            print(end=LINE_CLEAR)
            continue

    picked_col = False
    while picked_col is False:
        print("Now choose a column for your next stike", end="")
        col_coords = input("(1, 2, 3, 4, 5, 6, 7): \n")
        try:
            col_coords_int = int(col_coords)
            if col_coords_int < 1 or col_coords_int > 7:
                print(RED + BOLD + "Your input has to be " + RESET, end="")
                print(RED + BOLD + "a number  between " + RESET, end="")
                print(RED + BOLD + "1 to 7! Your input " + RESET, end="")
                print(RED + BOLD + f"was: {col_coords_int}" + RESET, end="")
                print(RED + BOLD + "please try again." + RESET)
                time.sleep(2)
                print(end=LINE_CLEAR)
                continue
        except ValueError:
            if col_coords == "":
                print(RED + BOLD + "Your input has to be " + RESET, end="")
                print(RED + BOLD + "a number  between " + RESET, end="")
                print(RED + BOLD + "1 to 7! Your input " + RESET, end="")
                print(RED + BOLD + "was: empty " + RESET, end="")
                print(RED + BOLD + "please try again." + RESET)
                time.sleep(2)
                print(end=LINE_CLEAR)
                continue
                print(RED + BOLD + "Your input has to be " + RESET, end="")
                print(RED + BOLD + "a number  between " + RESET, end="")
                print(RED + BOLD + "1 to 7! Your input " + RESET, end="")
                print(RED + BOLD + f"was: {col_coords}" + RESET, end="")
                print(RED + BOLD + "please try again." + RESET)
            time.sleep(2)
            print(end=LINE_CLEAR)
            continue
        col_coords_int -= 1
        strike_list.append(col_coords_int)
        picked_col = True

    return strike_list


def computer_turn(plyr_brd):
    """
    Processes the computers turn, randomly chooses target, validates if it is a
    valid target, and then proceeds to print the selection and a miss/hit
    confirm to the screen before it registers the strike on the player_brd.
    """
    # Select tile to strike and validate target.
    strike_valid = False
    valid_comp_strike = False
    while valid_comp_strike is False:
        rdm_strike_row = random.randint(0, 6)
        rdm_strike_col = random.randint(0, 6)
        if (plyr_brd[rdm_strike_row][rdm_strike_col] != 3
                and plyr_brd[rdm_strike_row][rdm_strike_col] != 4):
            valid_comp_strike is True
            strike_valid = True
            break
    # Process valid strike and prints selections to the terminal
    if strike_valid is True:
        #  Print selected row
        if rdm_strike_row == 0:
            print("Computer picked row 'A'")
            time.sleep(0.8)
        elif rdm_strike_row == 1:
            print("Computer picked row 'B'")
            time.sleep(0.8)
        elif rdm_strike_row == 2:
            print("Computer picked row 'C'")
            time.sleep(0.8)
        elif rdm_strike_row == 3:
            print("Computer picked row 'D'")
            time.sleep(0.8)
        elif rdm_strike_row == 4:
            print("Computer picked row 'E'.")
            time.sleep(0.8)
        elif rdm_strike_row == 5:
            print("Computer picked row 'F'.")
            time.sleep(0.8)
        elif rdm_strike_row == 6:
            print("Computer picked row 'G'.")
            time.sleep(0.8)

        # Print selected column
        if rdm_strike_col == 0:
            print("Computer picked row '1'")
            time.sleep(0.8)
        elif rdm_strike_col == 1:
            print("Computer picked row '2'")
            time.sleep(0.8)
        elif rdm_strike_col == 2:
            print("Computer picked row '3'")
            time.sleep(0.8)
        elif rdm_strike_col == 3:
            print("Computer picked row '4'")
            time.sleep(0.8)
        elif rdm_strike_col == 4:
            print("Computer picked row '5'.")
            time.sleep(0.8)
        elif rdm_strike_col == 5:
            print("Computer picked row '6'.")
            time.sleep(0.8)
        elif rdm_strike_col == 6:
            print("Computer picked row '7'.")
            time.sleep(0.8)

        # Processes hit/miss and prints it to the terminal
        if plyr_brd[rdm_strike_row][rdm_strike_col] == 0:
            print(GREEN + "The Computer Missed!" + RESET)
            time.sleep(1)
            plyr_brd[rdm_strike_row][rdm_strike_col] = 4
        elif plyr_brd[rdm_strike_row][rdm_strike_col] == 2:
            print(RED + "The Computer hits!" + RESET)
            time.sleep(1)
            plyr_brd[rdm_strike_row][rdm_strike_col] = 3
            game_data['player_ships'] -= 1
            user['score'] -= 5

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
        print(CYAN + 'You miss!' + RESET)
        time.sleep(1)
        brd[target_row][target_col] = 4
        return brd
    if brd[target_row][target_col] == 1:
        print('You shoot..')
        time.sleep(1)
        print(RED + "That's a Hit!!" + RESET)
        time.sleep(1)
        brd[target_row][target_col] = 3
        if owner != "Computer":
            game_data['enemy_ships'] -= 1
            user['score'] += 10
        return brd
    if brd[target_row][target_col] == 3:
        print(RED + BOLD + 'You already hit that target!' + RESET)
        time.sleep(2)
        return brd
    if brd[target_row][target_col] == 4:
        print(CYAN + BOLD + 'You already struck this tile! ' + RESET, end="")
        print(CYAN + BOLD + 'Nothing but water here.' + RESET)
        time.sleep(2)
        return brd


def update_board(comp_brd, plyr_brd):
    """
    Updates the gameboard with all current strikes processed.
    """
    clear_screen()
    create_logo()
    print_brd(comp_brd, "Computer")
    print_brd(plyr_brd, user['username'])


def validate_answer(user_input):
    """
    Validates the user input and checks whether it is yes or no.
    Prints a message accordingly and terminates or continues the program.
    """
    is_valid = False
    while is_valid is False:
        if user_input.lower() == "y":
            is_valid = True
            return True
        elif user_input.lower() == "n":
            is_valid = True
            return False
        else:
            print(RED + BOLD + f"{user_input} " + RESET, end="")
            print(RED + BOLD + f"is not a valid answer." + RESET, end='\r')
            time.sleep(1.2)
            print(LINE_CLEAR)
            user_input = input('Do you wish to play again? (y/n)\n')


def bonus_score(win):
    '''
    Check if the player won and provides bonus points accordingly.
    Player earns points for winning and effective shooting.
    '''
    if win:
        user['score'] += 10
        print(GREEN + BOLD + "You score 10 bonus points for winning!" + RESET)
    else:
        user['score'] -= 10
        print(RED + BOLD + "You lose 10 points for defeat!" + RESET)

    if win:
        if game_data['turn_count'] <= 5:
            user['score'] += 50
            print(GREEN + BOLD + "You score 50 bonus points" + RESET, end="")
            print(GREEN + BOLD + " for 100 percent accuracy!" + RESET)
        elif game_data['turn_count'] > 5 and game_data['turn_count'] <= 10:
            user['score'] += 30
            print(GREEN + BOLD + "You score 30 bonus points" + RESET, end="")
            print(GREEN + BOLD + " for hitting almost all shots!" + RESET)
        elif game_data['turn_count'] > 10 and game_data['turn_count'] <= 20:
            user['score'] += 20
            print(GREEN + BOLD + "You score 20 bonus points" + RESET, end="")
            print(GREEN + BOLD + " for hitting many shots!" + RESET)
        elif game_data['turn_count'] > 20 and game_data['turn_count'] <= 30:
            user['score'] += 10
            print(GREEN + BOLD + "You score 10 bonus points" + RESET, end="")
            print(GREEN + BOLD + " for an average performance." + RESET)


def push_to_ldb():
    '''
    Pushes run score and username to leaderboard worksheet.
    '''
    game_data_lst = []
    game_data_lst.append(user['username'])
    game_data_lst.append(user['score'])

    ldb_sheet = SHEET.worksheet('leaderboard')
    ldb_sheet.append_row(game_data_lst)


def reset_game():
    ''''
    Resets the game_data and user data (except the username) for another game.
    '''
    game_data['enemy_ships'] = 5
    game_data['player_ships'] = 5
    game_data['turn_count'] = 0
    user['score'] = 0
    user['turns'] = 0


def main_gameloop():
    """
    Executes the main game loop.
    """
    # Creates visuals and distributes ships on player and computer board
    create_logo()
    # copy.deepcopy bug fix for copying the reference to the entitiy 'brd'
    # as opposed to the actual list of lists. Found on stack Overflow by
    # user Felix King
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
        user['turns'] = game_data['turn_count']
        print(f'{computer_brd}')
        target = user_turn()
        computer_brd = validate_strike(target, computer_brd, user['username'])
        update_board(computer_brd, player_brd)
        if game_data['enemy_ships'] == 0:
            ongoing = False
            print(GREEN + BOLD + ">>> You are victorious! <<<" + RESET)
            bonus_score(True)
            push_to_ldb()
            print(BOLD + f"\nYou completed your run with " + RESET, end="")
            print(BOLD + f"a total of {user['score']} points." + RESET, end="")
            print(BOLD + f" Your achievements are saved" + RESET, end="")
            print(BOLD + f" to the leaderboard." + RESET)
            continue
        player_brd = computer_turn(player_brd)
        if game_data['player_ships'] == 0:
            ongoing = False
            update_board(computer_brd, player_brd)
            print(RED + BOLD + ">>> You have been defeated! <<<" + RESET)
            bonus_score(False)
            push_to_ldb()
            print(BOLD + f"\nYou completed your run with " + RESET, end="")
            print(BOLD + f"a total of {user['score']} points." + RESET, end="")
            print(BOLD + f" Your achievements are saved" + RESET, end="")
            print(BOLD + f" to the leaderboard." + RESET)
            continue
        update_board(computer_brd, player_brd)

    new_game = input('Do you wish to play again? (y/n)\n')
    new_game_choice = validate_answer(new_game)
    if new_game_choice:
        clear_screen()
        reset_game()
        main_gameloop()
    else:
        reset_game()
        print('Returning to menu...')
        time.sleep(1.2)


def uname_registration():
    """
    Requests a username from the player and registers the input
    to the user data dictionary
    """
    valid_input = False
    while valid_input is False:
        clear_screen()
        print(LOGO_TEXT)
        print(UNAME_BANNER)
        print("\nAdmiral, please choose a username. It has to be at", end="")
        username_input = input(" least 3 to max 10 characters long:\n")
        only_space = username_input.isspace()
        if only_space:
            print(RED + BOLD + "The username cannot " + RESET, end="")
            print(RED + BOLD + "be just whitespace." + RESET, end='\r')
            time.sleep(1.8)
            print(LINE_CLEAR)
        elif username_input != "":
            if len(username_input) >= 3 and len(username_input) <= 10:
                valid_input = True
                user['username'] = username_input
                clear_screen()
                main_gameloop()
            else:
                print(RED + BOLD + "Name has to be between 3 " + RESET, end="")
                print(RED + BOLD + "and 10 characters long!" + RESET, end='\r')
                time.sleep(1.8)
                print(LINE_CLEAR)
        else:
            print(RED + BOLD + "The username cannot be empty."
                  + RESET, end='\r')
            time.sleep(1.8)
            print(LINE_CLEAR)
