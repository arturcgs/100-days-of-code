from flask import Flask
import random

app = Flask(__name__)

HOME_GIF = "https://media2.giphy.com/media/UtWimzHLDlACk/200.webp?cid=ecf05e47h82ffk0lpnwuc99xdk88klxxtc8gj23663ueo652&ep=v1_gifs_search&rid=200.webp&ct=g"
GO_HIGHER = "https://media4.giphy.com/media/JLBT3PV3tOvIY/200.webp?cid=ecf05e47xleu82wgucpn6but2naeow9i8uqu50h5s71umldm&ep=v1_gifs_search&rid=200.webp&ct=g"
GO_LOWER = "https://media2.giphy.com/media/auXoWoc1Z4I16HC1CZ/200w.webp?cid=ecf05e47ocq9od8g6u0zxoy7lz4izgfqju831hkmuzflgvws&ep=v1_gifs_search&rid=200w.webp&ct=g"
WINNER_OTTER = "https://media3.giphy.com/media/11p8Lr9eVeXq2Q/200w.webp?cid=ecf05e47h82ffk0lpnwuc99xdk88klxxtc8gj23663ueo652&ep=v1_gifs_search&rid=200w.webp&ct=g"

correct_answer = random.randint(0, 9)
correct_answer = 7

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           f"<img src='{HOME_GIF}'>"


@app.route("/<guess>")
def check_answer(guess):
    guess = int(guess)
    if guess > correct_answer:
        return "<h1>Go lower!</h1>" \
               f"<img src={GO_LOWER}>"
    elif guess < correct_answer:
        return "<h1>Go higher!</h1>" \
               f"<img src={GO_HIGHER}>"
    else:
        return "<h1>CORRECT!</h1>" \
               f"<img src={WINNER_OTTER}>"


if __name__ == "__main__":
    app.run(debug=True)