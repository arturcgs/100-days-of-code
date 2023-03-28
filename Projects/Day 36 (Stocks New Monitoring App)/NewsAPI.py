import requests
import os


class NewsAPI:
    def __init__(self, company: str):
        # starting variables
        self._search = f'"+{company}"'
        self._endpoint = "https://newsapi.org/v2/everything"
        self._api_key = os.getenv("NEWS_API_KEY")
        self._params = {
            "q": self._search,
            "apiKey": self._api_key,
            "sortBy": "publishedAt",
            "language": "en",
            "searchIn": "title"
        }

        # getting data from API
        self._data = requests.get(self._endpoint, params=self._params).json()

        # selecting only interested data
        self._raw_latest_article = self._data["articles"][0]
        self.latest_article = {key: self._raw_latest_article[key] for key in ["title", "description"]}
