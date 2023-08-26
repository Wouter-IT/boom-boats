# Idea to setup a settings file for a few global
# variables from Stack Overflow user Hai Vu.
# https://stackoverflow.com/questions/13034496/using-global-variables-between-files

user = {
    "username": '',
    "score": 0,
    "turns": 0,
}

"""
Creates a list of lists with intigers assigned to it that function as tiles
for the game and and display the game data. Function call upon these list
indexes to process computer and player input needed to operate the main
game loop. Numbers stand for the following:
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
Stores game data to display on screen the enemy/player ships that
are left as well as the turn count.
"""
game_data = {
    "enemy_ships":  5,
    "player_ships": 5,
    "turn_count": 0
}
