from turtle import Turtle
import time
ALIGNMENT = 'center'
FONT = ('Courier', 18, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # score and high score
        self._score = 0
        with open("high_score.txt", "r") as f:
            self._high_score = int(f.readline())
        # turtle settings
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write_score()

    def write_score(self):
        """Prints the current score in the screen"""
        self.clear()
        self.write(f"Score: {self._score} | High Score: {self._high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increases the score by one, and, if necessary, the high score too"""
        self._score += 1
        if self._score > self._high_score:
            self._high_score = self._score
        self.write_score()

    def game_over(self):
        """Writes game over message and re-positions the scoreboard turtle"""
        # writing game over message
        self.goto(0, 0)
        self.write("YOU DIED!", align=ALIGNMENT, font=FONT)
        time.sleep(2)
        self.clear()
        # saving the high_score
        with open("high_score.txt", "w") as f:
            f.write(str(self._high_score))
        # restarting the scoreboard
        self._score = 0
        self.goto(x=0, y=270)
        self.write_score()
