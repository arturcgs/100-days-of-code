from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# create flask app and connect it to bootstrap-flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# create SQLAlchemy database
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
db.init_app(app)


# creating forms
class UpdateForm(FlaskForm):
    new_rating = StringField(label='Rating (Out of 10):', validators=[DataRequired()])
    new_review = StringField(label='Review:', validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):
    title = StringField(label="Movie Title:", validators=[DataRequired()])
    submit = SubmitField(label="Done")


# defining table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)


# creating table
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    # getting movies data, ordered by ranting
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    all_movies = result.scalars()

    # updating their rankings
    i = 1
    for movie in all_movies:
        print(movie.title)
        movie.ranking = i
        print(movie.ranking)
        i += 1
    db.session.commit()

    # getting the movie data again, now ordered by ranking
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars()

    return render_template("index.html", movies_data=all_movies)


@app.route("/edit/id=<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    edit_form = UpdateForm()
    movie_data = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    # update database from edit
    if edit_form.validate_on_submit():
        movie_data.rating = edit_form.new_rating.data
        movie_data.review = edit_form.new_review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_data, form=edit_form)


@app.route("/delete/id=<movie_id>")
def delete(movie_id):
    movie_data = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_data)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        # getting the movie data from the API
        api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MDU3YTJlOGUxMTM0MDRhNjgzNGNiZTA5MzJjNDE3NCIsInN1YiI6IjY0YzI3ZGIyZWRlMWIwMDEzYzZlZjg1ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.F-826tZ8VP8L4a22cX_Wlzk6kP_ORjLpvKKYDrA37no"
        url = "https://api.themoviedb.org/3/search/movie"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        params = {
            "query": add_form.title.data
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        movies_data = data["results"]

        return render_template("select.html", movies_list=movies_data)
    return render_template("add.html", form=add_form)


@app.route("/add_to_sql/<tmdb_id>", methods=["GET"])
def add_to_sql(tmdb_id):
    # getting the selcted movie data
    api_key = "4057a2e8e113404a6834cbe0932c4174"
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={api_key}"
    response = requests.get(url)
    movie_data = response.json()

    # adding movie data to sql database
    img_url_endpoint = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
    new_movie = Movie(
        title=movie_data["title"],
        year=int(movie_data["release_date"][:4]),
        description=movie_data["overview"],
        rating=float(movie_data["vote_average"]),
        ranking=0,
        review="",
        img_url=img_url_endpoint + movie_data["poster_path"],
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", movie_id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True)
