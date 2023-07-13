from BlogContent import BlogContent

blog = BlogContent()

for post in blog.all_posts:
    print(post.subtitle)