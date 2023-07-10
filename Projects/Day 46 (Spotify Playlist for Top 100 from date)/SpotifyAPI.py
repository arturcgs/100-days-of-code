import os
import time
from spotipy import SpotifyOAuth, Spotify


class SpotifyAPI:
    def __init__(self, date):
        self._CLIENT_ID = os.getenv("CLIENT_ID")
        self._CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        self._REDIRECT_URI = "http://localhost:3000"
        self._DATE = date

        oauth_spotify = SpotifyOAuth(
            client_id=self._CLIENT_ID,
            client_secret=self._CLIENT_SECRET,
            redirect_uri=self._REDIRECT_URI,
            scope="playlist-modify-public",
            show_dialog=True,
            cache_path="token.txt"
        )

        oauth_spotify.get_access_token()

        self.sp = Spotify(oauth_manager=oauth_spotify)

        self.user_id = self.sp.current_user()["id"]

    def create_playlist(self):
        playlist = self.sp.user_playlist_create(
            user=self.user_id,
            name=f"TOP 100 BILLBOARD - {self._DATE}",
            public=True
        )
        return playlist["id"]

    def add_songs(self, song_names, playlist_id):
        uri_list = []
        for song_name in song_names:
            time.sleep(1)
            search_uri = self.sp.search(q=f"track:{song_name}", type="track")
            try:
                uri = search_uri["tracks"]["items"][0]["uri"]
                uri_list.append(uri)

            except:
                print(f"{song_name} not found, skipping")

        self.sp.playlist_add_items(
            playlist_id=playlist_id,
            items=uri_list
        )




