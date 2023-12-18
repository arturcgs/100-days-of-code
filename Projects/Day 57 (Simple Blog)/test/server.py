from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(0, 20)
    today = datetime.today().strftime("%Y")
    return render_template("index.html", number=random_number, year=today)


@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}").json()
    gender = gender_response["gender"]

    age_response = requests.get(url=f"https://api.agify.io?name={name}").json()
    age = age_response["age"]

    return render_template(
        "guess.html",
        name=name,
        gender=gender,
        age=age
    )


@app.route("/blog/<num>")
def get_blog(num):
    return render_template("blog.html", number=num)


if __name__ == "__main__":
    app.run(debug=True)
