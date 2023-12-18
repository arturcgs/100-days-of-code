'''Draw a square'''

from turtle import Turtle, Screen

# creating turtle
timmy = Turtle()
timmy.shape("turtle")

# setting color
timmy.color('light steel blue')

# creating  square
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

# creating screen
screen = Screen()
screen.exitonclick()