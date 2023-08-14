import time
from background import draw_background
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# drawing the background
draw_background()

# creating objects
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# controlling player
screen.listen()
screen.onkeypress(player.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # checks if player has crossed the finish line
    if player.ycor() >= 270:
        player.refresh()
        scoreboard.increase_level()
        car_manager.increase_speed()

    # managing cars
    car_manager.create_cars()
    car_manager.move()

    # check for collision
    if car_manager.has_car_collision(player):
        scoreboard.game_over()
        game_is_on = False

# exit on click
screen.exitonclick()
