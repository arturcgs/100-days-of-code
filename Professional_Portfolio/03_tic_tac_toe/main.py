from data import logo, how_to_play, starting_game, winning_conditions, valid_plays

print(logo)
print(how_to_play)

current_game = starting_game


def print_board():
    print(f"""
============

 {current_game[1]} | {current_game[2]} | {current_game[3]} 
-----------
 {current_game[4]} | {current_game[5]} | {current_game[6]}
-----------
 {current_game[7]} | {current_game[8]} | {current_game[9]}
""")


def player_won(player):
    used_squares = [key for key, value in starting_game.items() if value == player]
    if used_squares in winning_conditions:
        return True
    return False


def add_play(play, player):
    # check if player gave number
    try:
        play = int(play)
    # error for not number
    except ValueError:
        print("That's not a valid play! You lost your turn.")
    else:
        # check if answer is between 1 and 9
        if play not in valid_plays:
            print("That's not a valid play! You lost your turn.")
            return
        used_squares = [key for key, value in starting_game.items() if value == "X"] + \
                       [key for key, value in starting_game.items() if value == "O"]
        if play in used_squares:
            print("That square is already used! You lost your turn.")
        # add play if all is correct
        current_game[play] = player


# initiate game
while True:
    # show board
    print_board()

    # player 1 play
    play_1 = input("Player 1:\nWhere do you want to put the X ?\n")
    add_play(play=play_1, player="X")
    if player_won("X"):
        print_board()
        print("Player 1 won!")
        break

    # show board
    print_board()

    # player 2 play
    play_2 = input("Player 2:\nWhere do you want to put the O ? ")
    add_play(play=play_2, player="O")
    if player_won("O"):
        print_board()
        print("Player 2 won!")
        break
