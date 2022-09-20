from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 50, 'bold')
SCORE_POSITION = (0, 220)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.computer_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(SCORE_POSITION)
        self.write_score()

    def write_score(self):
        """Write the score"""
        self.clear()
        self.write(f"{self.player_score} | {self.computer_score}", align=ALIGNMENT, font=FONT)

    def increase_player_score(self):
        """Increases the player score by 1"""
        self.player_score += 1
        self.write_score()

    def increase_computer_score(self):
        """Increases the computer score by 1"""
        self.computer_score += 1
        self.write_score()

    def game_over(self):
        """Prints Game Over message"""
        self.goto(0, -100)
        self.write("  GAME OVER\nClick to exit", align=ALIGNMENT, font=FONT)
