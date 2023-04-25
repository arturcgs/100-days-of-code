import requests
import os

'''
https://dashboard.sheety.co/
'''


class SheetAPI:
    def __init__(self):
        self._API_KEY = os.getenv("SHEET_API")
        self._ENDPOINT = "https://api.sheety.co/3c2d93ee6776adea1ee6c8610b831960/flightDeals/"
        self._HEADERS = {
            "Authorization": f"Bearer {self._API_KEY}"
        }

    def write_to_sheet(self, page, params):
        response = requests.post(
            url=f"{self._ENDPOINT}{page}",
            json=params,
            headers=self._HEADERS)
        return response

    def read_from_sheet(self, page):
        response = requests.get(url=f"{self._ENDPOINT}{page}", headers=self._HEADERS)
        return response.json()
