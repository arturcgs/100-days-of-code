from tkinter import *
import pandas as pd

# setting background color
BG_COLOR = "#b1ddc6"


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Flashcards")
        self.configure(background=BG_COLOR, padx=50, pady=50)

        # importing the database with words and their translations
        try:
            self.words_df = pd.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            self.words_df = pd.read_csv("data/words_data_2k.csv")

        # getting random word
        self.sample = self.words_df.sample()
        self.pt = self.sample.iloc[0, 0]
        self.en = self.sample.iloc[0, 1]

        # add canvas
        # creating canvas with image
        self.canvas = Canvas(width=800, height=526, background=BG_COLOR, highlightthickness=0)
        self.canvas.grid(column=1, row=1, columnspan=2)
        # card images
        self.card_images = {"front": PhotoImage(file="images/card_front.png"),
                            "back": PhotoImage(file="images/card_back.png")}
        self.image_container = self.canvas.create_image(400, 263, image=self.card_images["front"])
        # writing in canvas
        self.language = self.canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
        self.word = self.canvas.create_text(400, 263, text=self.en, font=("Ariel", 60, "bold"))

        # add buttons
        # correct button
        self.correct_image = PhotoImage(file="images/right.png")
        self.correct_button = Button(image=self.correct_image, bg=BG_COLOR, activebackground=BG_COLOR, borderwidth=0,
                                     command=self.word_is_known)
        self.correct_button.grid(column=2, row=2)

        # wrong button
        self.wrong_image = PhotoImage(file="images/wrong.png")
        self.wrong_button = Button(image=self.wrong_image, borderwidth=0, activebackground=BG_COLOR, bg=BG_COLOR,
                                   command=self.get_new_word)
        self.wrong_button.grid(column=1, row=2)

        # show answer after 3 seconds
        self.timer = self.after(3000, self.show_answer)

    def show_answer(self):
        """Updates tha canvas with the correct answer"""
        self.canvas.itemconfig(self.image_container, image=self.card_images["back"])
        self.canvas.itemconfig(self.language, text="Português", fill="white")
        self.canvas.itemconfig(self.word, text=self.pt, fill="white")

    def get_new_word(self):
        """Resets the timer, gets a random word from the dataframe and updates the canvas with it
        After 3 seconds, it shows the correct answer"""
        # canceling current timer, for it to restart every time I press the button
        self.after_cancel(self.timer)

        # getting new random word
        self.sample = self.words_df.sample()
        self.pt = self.sample.iloc[0, 0]
        self.en = self.sample.iloc[0, 1]

        # updating canvas
        self.canvas.itemconfig(self.image_container, image=self.card_images["front"])
        self.canvas.itemconfig(self.language, text="English", fill="black")
        self.canvas.itemconfig(self.word, text=self.en, fill="black")

        # showing answer after 3 seconds
        self.timer = self.after(3000, self.show_answer)

    def word_is_known(self):
        """deletes the known word from the df, saves it, and calls the new_word function"""
        # deleting current word from dataframe
        self.words_df = self.words_df.drop(self.sample.index, axis=0)
        # saving new dataframe
        self.words_df.to_csv("data/words_to_learn.csv", index=False)
        # getting new word
        self.get_new_word()
