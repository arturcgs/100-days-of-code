starting_game = {
    1: "X",
    2: "X",
    3: " ",
    4: " ",
    5: "X",
    6: "X",
    7: " ",
    8: "X",
    9: " ",
}

a = [key for key, value in starting_game.items() if value == "X"]

print(a)