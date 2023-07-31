

import requests

key = "4057a2e8e113404a6834cbe0932c4174"

blop = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MDU3YTJlOGUxMTM0MDRhNjgzNGNiZTA5MzJjNDE3NCIsInN1YiI6IjY0YzI3ZGIyZWRlMWIwMDEzYzZlZjg1ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.F-826tZ8VP8L4a22cX_Wlzk6kP_ORjLpvKKYDrA37no"

url = "https://api.themoviedb.org/3/search/movie"

url_id = f"https://api.themoviedb.org/3/movie/603?api_key={key}"

headers = {"accept": "application/json", "Authorization": f"Bearer {blop}"}

params = {
    "query": "the matrix"
}

params_id = {
    "id": "603"
}
response = requests.get(url_id)

print(response.json().keys())

