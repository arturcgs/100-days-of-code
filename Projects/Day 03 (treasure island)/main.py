def invalid_command():
    print("Invalid command, you died!")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
\nWelcome to the Treasure Island\nYour mission is to find the treasure''')

cross_road = input("\nYou're at a crossroad. Where do you want to go? Left or Right? ").strip().lower()

if cross_road == 'left':
    lake = input("\nYou find yourself at the a lake's shore. You see a boat in the middle of tha lake."
                 "Do you try to swim through the lake, or wait for the boat? Type swim or wait. ").strip().lower()
    if lake == 'wait':
        door = input("\nYou stand in the lake's shore, waiting. You look at the boat, it seems to be coming to you.\n"
                     "You get bored, but decides to keep waiting. Eventually, the boat comes.\n"
                     '"Can I help you with something?" The boat captain asks\n'
                     '"I just need to get to the other side of tha lake"\n'
                     '"Oh, no problem friend, come aboard!"\n'
                     'You enter the boat, and the friendly captain takes you to the other side of the lake\n'
                     'There, you enter a building with three doors: red, blue and yellow. Which one do you enter?'
                     ' ').strip().lower()
        if door == 'red':
            print("You enter the door, and suddenly fire erupts from the wall. You are dead.\nGame Over!")
        elif door == 'blue':
            print("You enter the door, and suddenly water starts filling the room. You die after a few minutes."
                  "\nGame Over!")
        elif door == 'yellow':
            print("You find yourself in a dark corridor. You start walking forward, but doesn't seem to be going "
                  "anywhere.\nAfter a few minutes, you start hearing a noise behind you, something faint, almost "
                  "like a growl.\nYou start running forward. The noise gets louder and louder. You finally see"
                  "something in front of you.\nA door. You give your all to get to it. After going through it, you find"
                  " a treasure.\nCongratulations! You won!")
        else:
            invalid_command()
    elif lake == 'swim':
        print('''You fell a cold and gooey thing twirl around you ankle. It pushes you down.
              You kick it hard, but it doesn't let go. You try to swim up, but you're not strong enough.
              Everything is getting darker. And darker. And darker. Until it's all just darkness, forever.
              You died. Game over!''')
    else:
        invalid_command()
elif cross_road == 'right':
    print('A tree fell on you. Game Over!')
else:
    invalid_command()
