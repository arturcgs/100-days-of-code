from tkinter import *
from quiz_brain import QuizBrain

# setting background color
BG_COLOR = "#3a3b7d"
SCORE_COLOR = "#ffffff"
TRIVIA_COLOR = "#000000"


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Quizzler")
        self.configure(background=BG_COLOR, padx=50, pady=50)

        # initializing QuizBrain
        self.quiz_brain = QuizBrain()

        # initializing score
        self.score = 0
        self.score_label = Label(
            text=f"Score: {self.score}",
            bg=BG_COLOR,
            foreground=SCORE_COLOR,
            font=("Hack", 30)
        )
        self.score_label.grid(column=2, row=1)

        # add canvas
        # creating canvas with image
        self.canvas = Canvas(width=800, height=526, background=BG_COLOR, highlightthickness=0)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=20)
        self.trivia_bg = PhotoImage(file="imgs/card_front.png")
        self.image_container = self.canvas.create_image(
            400,
            263,
            image=self.trivia_bg
        )
        # writing in canvas
        self.trivia = self.canvas.create_text(
            400,
            150,
            text="Welcome to Quizzler!\n\nPress any button \nbelow to start.",
            font=("Hack", 35),
            fill=TRIVIA_COLOR
        )

        # add buttons
        # correct button
        self.correct_image = PhotoImage(file="imgs/right.png")
        self.correct_button = Button(
            image=self.correct_image,
            bg=BG_COLOR,
            activebackground=BG_COLOR,
            borderwidth=0,
            command=lambda: self.check_answer(user_answer="True"),
        )
        self.correct_button.grid(column=2, row=3, pady=10)

        # wrong button
        self.wrong_image = PhotoImage(file="imgs/wrong.png")
        self.wrong_button = Button(
            image=self.wrong_image,
            borderwidth=0,
            activebackground=BG_COLOR,
            bg=BG_COLOR,
            command=lambda: self.check_answer(user_answer="False"),
        )
        self.wrong_button.grid(column=1, row=3)

    def check_answer(self, user_answer):
        # update question
        next_question = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.trivia, text=f"{next_question}")

        # update score
        self.score = self.quiz_brain.update_score(user_answer)
        self.score_label["text"] = f"Score: {self.score}"
