from flask import Flask, render_template
from BlogContent import BlogContent
from Post import Post

app = Flask(__name__)
blog_content = BlogContent()
# edit blog content - https://www.npoint.io/docs/4c89fa7a0d8d3febcb28

@app.route("/")
def home():
    global blog_content
    blog_content = BlogContent()

    return render_template(
        "index.html",
        title="Clean Blog",
        bg_img="../static/assets/img/home-bg.jpg",
        all_posts=blog_content.all_posts
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About Me",
        bg_img="../static/assets/img/about-bg.jpg"
    )


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        title="Clean Blog",
        bg_img="../static/assets/img/contact-bg.jpg"
    )


@app.route("/post/<post_id>")
def post(post_id):
    # 404 if doesn't find
    post_content = Post()

    # looking for post with the same id
    for curr_post in blog_content.all_posts:
        if int(curr_post.id) == int(post_id):
            post_content = curr_post

    return render_template(
        "post.html",
        post=post_content
    )





if __name__ == "__main__":
    app.run(debug=True)
