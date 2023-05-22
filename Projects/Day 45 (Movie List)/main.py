from bs4 import BeautifulSoup
import requests

URL = "https://www.timeout.com/film/best-movies-of-all-time"

# getting html
response = requests.get(URL)
live_page = response.text

# transforming to soup
soup = BeautifulSoup(live_page, "html.parser")

# looking for titles
movie_titles = soup.select("h3._h3_cuogz_1")

# converting titles to python list of text
movies = [movie.getText().replace(u'\xa0', u' ') for movie in movie_titles]

# saving movies to text file
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
