from colorama import Fore, Style

# Use of color came from Code Institute student kpetrauskas92 and his project Fury
# https://github.com/kpetrauskas92/fury-p3/blob/main/game/game.py
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
DIM = Style.DIM
RESET = Style.RESET_ALL

LOGO = f'''⠀⠀⠀{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢶⠢⢤⡀⠀⠙⢷⣌⠑⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠃⠈⣇⠀⠀⠑⠢⢄⡻⣷⡈⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⢸⡀⠀⠀⠀⠀⠈⠙⠻⢦⡈⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠻⢷⣴⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⣀⢨⣉⣉⣉⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢌⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠰⠆⠦⣤⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣶⡀⠀⠀⠀⠖⠻⠿⠿⠿⠿⠿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⡀⠀⠀⠀⠀⢠⣿⣿⣿⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⣄⡀⠀⢐⣒⡒⠶⠶⠶⡖⡧⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢄⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⠑⠮⣗⡛⠯⠵⢶⣧⣙⡒⠦⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠉⠓⠢⣄⣳⠦⣟⣛⠵⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣄⡀⠀⠀⠉⠓⠦⣌⡉⢳⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣬⣆⣆⡍⠛⠦⣤⠂⠐⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠙⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣶⣦⣭⣓⠦⣏⠉⠁⡶⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⣤⣤⣤⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⣀⣶⣾⣦⣀⣀⡀⠀
 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 

⠀⣶⣶⣶⣶⣶⣶⣤⠀⠀⣠⣶⣶⣶⣶⣦⡀⠀⢀⣤⣶⣶⣶⣶⣤⠀⢰⣶⣶⣶⣶⠀⢀⣶⣶⣶⣶⠀⠀⠀⣶⣶⣶⣶⣶⣶⣤⡀⠀⣠⣴⣶⣶⣶⣦⡄⠀⠀ ⣶⣶⣶⡆⠀⣶⣶⣶⣶⣶⣶⣶⢠⣴⣶⣶⣶⣦⣄⠀ 
⠀⣿⣿⣿⠛⢿⣿⣿⡇⢰⣿⣿⣿⠛⣿⣿⣿⡄⣾⣿⣿⡟⢿⣿⣿⣇⢸⣿⣿⣿⣿⡆⣼⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⠛⢿⣿⣿⣷⢰⣿⣿⣿⠛⣿⣿⣿⡄⠀⣼⣿⣿⣿⣿⡀⠛⠛⣿⣿⣿⠛⠛⣿⣿⣿⡛⣿⣿⡿⠆ 
⠀⣿⣿⣿⣶⣿⣿⣿⠃⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⢸⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣶⣿⣿⣿⠟⣿⣿⣿⡇⠀⣿⣿⣿⡇⢰⣿⣿⠛⣿⣿⡇⠀⠀⣿⣿⣿⠀⠀⢿⣿⣿⣿⣾⣥⣄⠀ 
⠀⣿⣿⣿⠛⢿⣿⣿⣧⢿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⠛⢿⣿⣿⣷⣿⣿⣿⡇⠀⣿⣿⣿⡇⣼⣿⣿⣤⣿⣿⣿⡀⠀⣿⣿⣿⠀⠀⣈⣛⡻⢿⣿⣿⣿⡆ 
⠀⣿⣿⣿⣤⣾⣿⣿⡿⠸⣿⣿⣿⣴⣿⣿⣿⠃⢿⣿⣿⣧⣾⣿⣿⡏⢸⣿⣿⡿⣿⣿⣿⡇⣿⣿⣿⠀⠀⠀⣿⣿⣿⣤⣾⣿⣿⣿⠸⣿⣿⣿⣴⣿⣿⣿⣻⣿⣿⡿⠿⢿⣿⣿⣧⠀⣿⣿⣿⠀⠸⣿⣿⣷⣤⣿⣿⣿⠇ 
⠀⠿⠿⠿⠿⠿⠿⠛⠁⠀⠙⠿⢿⣿⠿⠟⠁⠀⠈⠛⠿⣿⣿⠿⠛⠀⠸⠿⠿⠇⠻⠿⠿⠀⠿⠿⠿⠀⠀⠀⠿⠿⠿⠿⠿⠿⠟⠁⠀⠙⠻⢿⣿⡿⠟⠃⠿⠿⠿⠃ ⠸⠿⠿⠿ ⠿⠿⠿⠀⠀⠙⠿⢿⣿⡿⠟⠋⠀ 
{RESET}'''
LOGO_TEXT = f'''{CYAN}
⠀⣶⣶⣶⣶⣶⣶⣤⠀⠀⣠⣶⣶⣶⣶⣦⡀⠀⢀⣤⣶⣶⣶⣶⣤⠀⢰⣶⣶⣶⣶⠀⢀⣶⣶⣶⣶⠀⠀⠀⣶⣶⣶⣶⣶⣶⣤⡀⠀⣠⣴⣶⣶⣶⣦⡄⠀⠀ ⣶⣶⣶⡆⠀⣶⣶⣶⣶⣶⣶⣶⢠⣴⣶⣶⣶⣦⣄  
⠀⣿⣿⣿⠛⢿⣿⣿⡇⢰⣿⣿⣿⠛⣿⣿⣿⡄⣾⣿⣿⡟⢿⣿⣿⣇⢸⣿⣿⣿⣿⡆⣼⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⠛⢿⣿⣿⣷⢰⣿⣿⣿⠛⣿⣿⣿⡄⠀⣼⣿⣿⣿⣿⡀⠛⠛⣿⣿⣿⠛⠛⣿⣿⣿⡛⣿⣿⡿⠆ 
⠀⣿⣿⣿⣶⣿⣿⣿⠃⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⢸⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣶⣿⣿⣿⠟⣿⣿⣿⡇⠀⣿⣿⣿⡇⢰⣿⣿⠛⣿⣿⡇⠀⠀⣿⣿⣿⠀⠀⢿⣿⣿⣿⣾⣥⣄⠀ 
⠀⣿⣿⣿⠛⢿⣿⣿⣧⢿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⠛⢿⣿⣿⣷⣿⣿⣿⡇⠀⣿⣿⣿⡇⣼⣿⣿⣤⣿⣿⣿⡀⠀⣿⣿⣿⠀⠀⣈⣛⡻⢿⣿⣿⣿⡆ 
⠀⣿⣿⣿⣤⣾⣿⣿⡿⠸⣿⣿⣿⣴⣿⣿⣿⠃⢿⣿⣿⣧⣾⣿⣿⡏⢸⣿⣿⡿⣿⣿⣿⡇⣿⣿⣿⠀⠀⠀⣿⣿⣿⣤⣾⣿⣿⣿⠸⣿⣿⣿⣴⣿⣿⣿⣻⣿⣿⡿⠿⢿⣿⣿⣧⠀⣿⣿⣿⠀⠸⣿⣿⣷⣤⣿⣿⣿⠇ 
⠀⠿⠿⠿⠿⠿⠿⠛⠁⠀⠙⠿⢿⣿⠿⠟⠁⠀⠈⠛⠿⣿⣿⠿⠛⠀⠸⠿⠿⠇⠻⠿⠿⠀⠿⠿⠿⠀⠀⠀⠿⠿⠿⠿⠿⠿⠟⠁⠀⠙⠻⢿⣿⡿⠟⠃⠿⠿⠿⠃ ⠸⠿⠿⠿ ⠿⠿⠿⠀⠀⠙⠿⢿⣿⡿⠟⠋⠀ 
{RESET}'''

MENU_BANNER = f'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ MAIN MENU ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿'''

DIVIDER = f'''⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶\n'''

UNAME_BANNER = f'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ USERNAME ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿'''

BANNER = f'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n'''