import sys
import os
from art import LOGO_TEXT, UNAME_BANNER
from settings import user

def create_brd():
    os.system('clear')
    print(LOGO_TEXT)
    numerals_top = f"    1  2  3  4  5  6  7  "
    border_top_bottom = f"  +---------------------+"
    board
    print(numerals_top)
    print(border_top_bottom)
    print(f)
    print(border_top_bottom)
    something = input('type something')



def uname_registration():
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
