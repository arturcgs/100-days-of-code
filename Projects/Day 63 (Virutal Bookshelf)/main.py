from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


# create table
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # reading the database
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", book_data=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    # adding book to database
    if request.method == "POST":
        new_book = Book(
            title=request.form.get("title"),
            author=request.form.get("author"),
            rating=request.form.get("rating")
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/edit/id=<book_id>", methods=["GET", "POST"])
def edit(book_id):
    # getting book information
    book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

    # updating rating
    if request.method == "POST":
        book.rating = request.form.get("new_rating")
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", book_data=book)


@app.route("/delete/<book_id>")
def delete(book_id):
    # deleting book
    book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

