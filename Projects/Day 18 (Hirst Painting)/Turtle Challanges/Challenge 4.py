"""Create random wal"""

from turtle import Turtle, Screen, colormode
import random


def change_color():
    """ This function changes de turtle's color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    timmy.color((r, g, b))


# creating turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.width(8)
timmy.speed(10)

# colormode
colormode(255)

# random walk
directions = [0, 90, 180, 270]
for _ in range(100):
    timmy.setheading(random.choice(directions))
    timmy.forward(30)
    change_color()

# creating screen
screen = Screen()
screen.exitonclick()
