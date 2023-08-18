import sys
import os
from art import LOGO_TEXT, UNAME_BANNER
from settings import user

def uname_registration():
    os.system('clear')
    print(LOGO_TEXT)
    print(UNAME_BANNER)
    while True:
        username_input = input("\nAdmiral, please choose a username. It has to be at least 1 character long:\n")
        if username_input != "":
            return False
        else:
            os.system('clear')
        print(LOGO_TEXT)
        print(UNAME_BANNER)
        print("\nThe username cannot be empty.")
    user['username'] = username_input