from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

# flask app, bootstrap and ckeditor
app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


# ADD POST FORM
class AddPost(FlaskForm):
    title = StringField("Post Title:", validators=[DataRequired()])
    subtitle = StringField("Post Subtitle:", validators=[DataRequired()])
    author = StringField("Post Author:", validators=[DataRequired()])
    img_url = StringField("Post Image:", validators=[DataRequired(), URL()])
    body = CKEditorField("Post Body:", validators=[DataRequired()])
    submit = SubmitField("Send")


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    all_posts = result.scalars().all()
    return render_template("index.html", all_posts=all_posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/<post_id>')
def show_post(post_id):
    post_data = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=post_data)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    add_post = AddPost()
    if add_post.validate_on_submit():
        new_post = BlogPost(
            title=add_post.title.data,
            subtitle=add_post.subtitle.data,
            date=date.today().strftime("%b %d, %Y"),
            body=add_post.body.data,
            author=add_post.author.data,
            img_url=add_post.img_url.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=add_post, create=True)

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    # getting the post data
    post_data = db.get_or_404(BlogPost, post_id)

    # creating the form
    edit_post_form = AddPost(
        title=post_data.title,
        subtitle=post_data.subtitle,
        author=post_data.author,
        img_url=post_data.img_url,
        body=post_data.body,
    )

    if edit_post_form.validate_on_submit():
        post_data.title = edit_post_form.title.data
        post_data.subtitle = edit_post_form.subtitle.data
        post_data.author = edit_post_form.author.data
        post_data.img_url = edit_post_form.img_url.data
        post_data.body = edit_post_form.body.data
        post_data.date = date.today().strftime("%b %d, %Y")

        db.session.commit()

        return redirect(url_for("show_post", post_id=post_data.id))

    return render_template("make-post.html", create=False, form=edit_post_form)


@app.route("/delete/<post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
