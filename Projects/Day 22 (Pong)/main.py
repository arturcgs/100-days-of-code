from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# setting screen up
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# creating paddles
computer_paddle = Paddle(350, 0)
player_paddle = Paddle(-350, 0)

# creating ball
ball = Ball()

# creating scoreboard
scoreboard = ScoreBoard()
scoreboard.write_score()

# control keys
screen.listen()
screen.onkeypress(player_paddle.go_up, "w")
screen.onkeypress(player_paddle.go_down, "s")
screen.onkeypress(computer_paddle.go_up, "Up")
screen.onkeypress(computer_paddle.go_down, "Down")

speed = 0.04
game_is_on = True
while game_is_on:
    # game setup
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # checking wall bounce
    if ball.has_wall_collision():
        ball.wall_bounce()
    # checking paddle bounce
    elif ball.has_right_paddle_collision(player_paddle) or ball.has_left_paddle_collision(computer_paddle):
        ball.paddle_bounce()

    # check player point
    if ball.xcor() > 600:
        scoreboard.increase_player_score()
        ball.refresh()
    # check computer point
    elif ball.xcor() < -600:
        scoreboard.increase_computer_score()
        ball.refresh()

    # check for game over
    if scoreboard.player_score == 5 or scoreboard.computer_score == 5:
        game_is_on = False
        scoreboard.game_over()

# exit on click
screen.exitonclick()
