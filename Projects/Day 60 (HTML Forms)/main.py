from flask import Flask, render_template, request
import requests
from email_sender import send_email

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/4c89fa7a0d8d3febcb28").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # getting information from form
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        user_message = request.form.get("message")
        # sending email
        email_message = f"Subject:Contact from Blog!\n" \
                        f"Name - {name}\nEmail - {email}\nPhone - {phone}\n" \
                        f"Message - {user_message}"
        send_email(email_message)
        # returning contact.html, but with message sent title
        return render_template("contact.html", title="Succesfully sent message")

    return render_template("contact.html", title="Contact Me!")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
