from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.create_paddle(x, y)

    def create_paddle(self, x, y):
        """Creates a paddle"""
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.penup()
        self.speed(0)
        self.goto(x, y)

    # movement functions
    def go_up(self):
        if self.ycor() < 250:
            self.forward(20)

    def go_down(self):
        if self.ycor() > -250:
            self.backward(20)
