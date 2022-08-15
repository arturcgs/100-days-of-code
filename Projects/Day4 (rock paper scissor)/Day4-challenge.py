
def print_map():
    print(f"{map[0][0]}| {map[0][1]}| {map[0][2]}\n" + "-" * 18 +
          f"\n{map[1][0]}| {map[1][1]}| {map[1][2]}\n" + "-" * 18 +
          f"\n{map[2][0]}| {map[2][1]}| {map[2][2]}\n" + "-" * 18)

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

print("This is the current map")
print_map()

coordenates = input("Where do you want to put the X? Type first the column, then the line number: ").strip()
column = int(coordenates[0]) - 1
line = int(coordenates[1]) - 1

map[line][column] = "X  ️"

print_map()