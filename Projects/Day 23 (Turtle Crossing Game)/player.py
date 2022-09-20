from turtle import Turtle
INITIAL_POSITION = (0, -270)


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.create_player()

    def create_player(self):
        """creates the player"""
        self.shape("turtle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.refresh()

    def go_up(self):
        """Moves the player up"""
        self.forward(15)

    def refresh(self):
        """Sends the player to the initial position"""
        self.goto(INITIAL_POSITION)
