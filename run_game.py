import sys
import os
from art import LOGO_TEXT, UNAME_BANNER
from settings import user

def create_brd():
    brd = []

def uname_registration():
    os.system('clear')
    print(LOGO_TEXT)
    print(UNAME_BANNER)
    username_input = input("\nAdmiral, please choose a username. It has to be at least 1 character long:\n")
    if username_input != "":
        user['username'] = username_input
    else:
        os.system('clear')
        print(LOGO_TEXT)
        print(UNAME_BANNER)
        print("\nThe username cannot be empty.")
