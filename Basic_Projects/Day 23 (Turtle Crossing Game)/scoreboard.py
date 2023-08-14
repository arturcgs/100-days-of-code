from turtle import Turtle
FONT = ("Courier", 18, "bold")
ALIGNMENT = "left"
LEVEL_POSITION = (-280, 240)


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self._level = 0
        self.penup()
        self.hideturtle()
        self.goto(LEVEL_POSITION)
        self.write_level()

    def write_level(self):
        """Write the current level the player is on"""
        self.clear()
        self.write(f"Level: {self._level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """Increases the level by 1"""
        self._level += 1
        self.write_level()

    def game_over(self):
        self.goto(-50, 0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)
