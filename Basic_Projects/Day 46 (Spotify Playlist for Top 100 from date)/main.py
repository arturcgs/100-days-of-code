from bs4 import BeautifulSoup
import requests
from SpotifyAPI import SpotifyAPI

# getting year from user
year = input("Which year would you like to travel to? (Please type de date in this format YYYY-MM-DD): ")


# getting website data
URL = f"https://www.billboard.com/charts/hot-100/{year}/"
response = requests.get(URL)
live_page = response.text

# Getting the song name and saving them in a list
soup = BeautifulSoup(live_page, "html.parser")

song_names_raw = soup.select("h3#title-of-a-story.c-title.a-no-trucate")

song_names = [song.getText().strip() for song in song_names_raw]

# Creating Spotify Playlist and Adding songs to Playlist

spotify = SpotifyAPI(date="1970-07-27")

playlist_id = spotify.create_playlist()

spotify.add_songs(song_names=song_names, playlist_id=playlist_id)

print("Playlist created!")