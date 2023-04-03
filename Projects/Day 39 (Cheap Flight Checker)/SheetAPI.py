import requests
import os

'''
https://dashboard.sheety.co/
'''

class SheetAPI:
    def __init__(self):
        self._API_KEY = os.getenv("SHEET_API")
        self._ENDPOINT = "https://api.sheety.co/3c2d93ee6776adea1ee6c8610b831960/flightDeals/prices"
        self._HEADERS = {
            "Authorization": f"Bearer {self._API_KEY}"
        }

    def write_to_sheet(self, city, iata_code, lowest_price):
        params = {
            "price": {
                "city": city,
                "iata": iata_code,
                "price": lowest_price,
            }
        }

        response = requests.post(
            url=self._ENDPOINT,
            json=params,
            headers=self._HEADERS)
        return response

    def read_from_sheet(self):
        response = requests.get(url=self._ENDPOINT, headers=self._HEADERS)
        return response.json()
