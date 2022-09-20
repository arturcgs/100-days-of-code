"""Draw a square with dashed lines"""

from turtle import Turtle, Screen

# creating turtle
timmy = Turtle()
timmy.shape("turtle")

# moving the turtle
for _ in range(4):
    for _ in range(10):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
    timmy.right(90)

# creating screen
screen = Screen()
screen.exitonclick()
