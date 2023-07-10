from flask import Flask, render_template
import requests

"https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

@app.route('/')
def home():
    # getting posts data
    posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    posts_response = requests.get(url=posts_url)
    posts_data = posts_response.json()

    return render_template("index.html", all_posts=posts_data)


@app.route('/post/<post_id>')
def get_post(post_id):

    # getting posts data
    posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    posts_response = requests.get(url=posts_url)
    posts_data = posts_response.json()

    # defining correct_post_data, in case it's not found
    correct_post_data = {
        "id": 0,
        "body": "post not found",
        "title": "post not found",
        "subtitle": "post not found"
    }

    # looking for correct post data
    for post in posts_data:
        if post["id"] == int(post_id):
            correct_post_data = post

    return render_template("post.html", post_data=correct_post_data)


if __name__ == "__main__":
    app.run(debug=True)
