from turtle import Screen
import time
from Snek import Snek
from Food import Food
from ScoreBoard import ScoreBoard


def game_over():
    global game_is_on
    game_is_on = False
    score_board.game_over()


# creating screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# changing difficulty
difficulty = int(screen.numinput(title="Difficulty", prompt="Choose a difficulty:\n(1) Easy\n(2) Medium\n(3) Hard",
                                 minval=1, maxval=3))
difficulty_speed = {1: 0.1, 2: 0.06, 3: 0.03}

# creating initial objects
snek = Snek()
food = Food()
score_board = ScoreBoard()

# controlling the snake
screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.right, "Right")
screen.onkey(snek.left, "Left")
screen.onkey(game_over, "c")

# game loop
game_is_on = True
while game_is_on:
    # screen update and time (time controls speed)
    screen.update()
    time.sleep(difficulty_speed[difficulty])

    # moving the snake
    snek.move()

    # detect collision with food
    if snek.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snek.extend()

    # detect collision with wall
    snek.loop_screen()

    # detect collision with snake
    if snek.has_collision():
        game_over()

# exit on click
screen.exitonclick()
