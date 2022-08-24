from color_extraction import colors_list
from turtle import Turtle, Screen, colormode
import random


def draw_line():
    for _ in range(18):
        timmy.dot(20, random.choice(colors_list))
        timmy.forward(40)


# creating turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.speed(0)

# colormode
colormode(255)

# setting timmy up
timmy.penup()
x = -345
y = -290
timmy.setposition(x, y)

# moving timmy
for _ in range(16):
    draw_line()
    y += 40
    timmy.setposition(x, y)


# creating screen
screen = Screen()
screen.exitonclick()
