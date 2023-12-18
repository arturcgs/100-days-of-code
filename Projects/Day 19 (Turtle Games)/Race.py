import turtle as t
import random


def draw_finish_line():
    """This function draws the finish line"""
    # initiating pencil turtle
    pencil = t.Turtle(shape='turtle')
    pencil.hideturtle()
    pencil.speed(0)
    pencil.width(5)

    # drawing two main lines
    pencil.setheading(90)
    for x in [205, 230]:
        pencil.penup()
        pencil.setposition(x=x, y=-200)
        pencil.pendown()
        pencil.forward(400)

    # drawing the strips
    pencil.setheading(45)
    pencil.width(5)
    y_position = -200
    for _ in range(20):
        # initial position
        pencil.penup()
        pencil.setposition(x=205, y=y_position)
        # draw line
        pencil.pendown()
        pencil.forward(32)
        # increment y
        y_position += 20


def turtle_race():
    # creating screen
    screen = t.Screen()
    screen.setup(width=500, height=400)

    # getting user's bet
    user_guess = screen.textinput(title="Make your bet!", prompt="Which turtle would you like to bet on?\n(Red, Orange,"
                                                                 " Yellow, Green, Blue, Purple)").lower().strip()

    # drawing finish line
    draw_finish_line()

    # creating turtles
    all_turtles = [t.Turtle(shape='turtle') for _ in range(6)]

    # creating colors list
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # setting y variable to control turtle's initial position
    y = -100

    for turtle, color in zip(all_turtles, colors):
        # changing colors
        turtle.color(color)
        # changing position
        turtle.penup()
        turtle.goto(x=-230, y=y)
        y += 40

    # moving turtles by random amount
    race_is_on = True
    while race_is_on:
        for turtle in all_turtles:
            turtle.forward(random.randint(0, 10))
            # winner check
            if turtle.xcor() >= 240:
                winner = turtle.pencolor()
                race_is_on = False
                # player guess check
                if user_guess == winner:
                    print(f"You guessed it, {winner.capitalize()} won the race!")
                else:
                    print(f"You lost, {winner.capitalize()} won the race!")

    # exit on click
    screen.exitonclick()


if __name__ == '__main__':
    turtle_race()
