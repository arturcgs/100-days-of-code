import EtchASketch as Es
import Race as Rc

print("Welcome! Which game would you like to play?")
game = int(input("Game options:\n(1) Etch a Sketch\n(2) Turtle Race Game\n(0) Exit\nWhat is your choice? "))
if game == 1:
    Es.etchsketch()
elif game == 2:
    Rc.turtle_race()
else:
    print("Thank you very much!")
