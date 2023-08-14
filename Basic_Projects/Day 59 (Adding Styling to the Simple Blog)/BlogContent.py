from Post import Post
import requests

class BlogContent:
    def __init__(self):

        # getting posts data
        posts_url = "https://api.npoint.io/4c89fa7a0d8d3febcb28"
        posts_response = requests.get(url=posts_url)
        posts_data = posts_response.json()

        self.all_posts = [
            Post(
                post_id=post["id"],
                body=post["body"],
                title=post["title"],
                subtitle=post["subtitle"],
                author=post["author"],
                date=post["date"],
                bg_img=post["bg_img"]
            )
            for post in posts_data
        ]

