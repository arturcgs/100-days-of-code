""" Draw polygons from 3 to 10 sides, with random colors"""

from turtle import Turtle, Screen, colormode
import random


def change_color():
    """ This function changes de trutle's color"""
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)

    timmy.color(R, G, B)


def draw_polygon(n_sides):
    """ Thins function draws a polygon of n_sides"""
    angle = 360 / n_sides
    for _ in range(n_sides):
        timmy.forward(100)
        timmy.right(angle)


# creating turtle
timmy = Turtle()
timmy.shape("turtle")

# colormode
colormode(255)

# drawing the polygons
for i in range(3, 11):
    change_color()
    draw_polygon(i)




# creating screen
screen = Screen()
screen.exitonclick()