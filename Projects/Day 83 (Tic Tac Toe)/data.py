logo = """
 _   _      _             _             
| | (_)    | |           | |            
| |_ _  ___| |_ __ _  ___| |_ ___   ___ 
| __| |/ __| __/ _` |/ __| __/ _ \ / _ \\
| |_| | (__| || (_| | (__| || (_) |  __/
 \__|_|\___|\__\__,_|\___|\__\___/ \___|
"""

how_to_play = """
======== Welcome to Tic Tac Toe! ========

This is a two player game, so call a friend!
For this game, player 1 will be X, and player 2 will be O.
To select the square you want use, please refer to this board:

 1 | 2 | 3 
 ----------
 4 | 5 | 6 
 ----------
 7 | 8 | 9 
"""

starting_game = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " ",
}

winning_conditions = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]

valid_plays = [1, 2, 3, 4, 5, 6, 7, 8, 9]