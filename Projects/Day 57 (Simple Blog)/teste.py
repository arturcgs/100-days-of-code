import requests

posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
posts_response = requests.get(url=posts_url)
posts_data = posts_response.json()

print(posts_data)