"""Draw a Spirograph"""

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
timmy.speed(0)

# colormode
colormode(255)

# drawing spirograph
angle = 360/80
for _ in range(80):
    change_color()
    timmy.circle(100)
    timmy.left(angle)

# creating screen
screen = Screen()
screen.exitonclick()
