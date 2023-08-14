from turtle import Turtle
import random
INITIAL_HEADINGS = [30, 35, 40, 45, 50, 130, 135, 140, 145, 150, 210, 215, 220, 225, 230, 310, 315, 320, 325, 330]


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.create_ball()
        self.move_speed = 0.04

    def create_ball(self):
        """Creates the ball"""
        self.shape("circle")
        self.color("white")
        self.setheading(random.choice(INITIAL_HEADINGS))
        self.penup()
        self.speed("slowest")

    def move(self):
        """Moves the ball forward"""
        self.forward(10)

    def refresh(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.move_speed = 0.04

    # bouncing functions
    def wall_bounce(self):
        """Bounces the ball on the wall"""
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def paddle_bounce(self):
        """Bounces the ball on the paddle"""
        new_heading = 180 - self.heading()
        self.setheading(new_heading)
        self.move_speed *= 0.9

    # collision functions
    def has_wall_collision(self):
        """Returns True if the ball has collided with a wall"""
        return self.ycor() >= 280 or self.ycor() <= -280

    def has_right_paddle_collision(self, paddle):
        """Returns True if the ball has collided with the right paddle"""
        return self.xcor() <= -330 and self.distance(paddle) <= 50

    def has_left_paddle_collision(self, paddle):
        """Returns True if the ball has collided with the left paddle"""
        return self.xcor() >= 330 and self.distance(paddle) <= 50
