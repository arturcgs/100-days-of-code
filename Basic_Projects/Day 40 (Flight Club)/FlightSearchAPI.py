import requests
import os
from datetime import datetime, timedelta

'''
https://tequila.kiwi.com/portal/docs/tequila_api/locations_api
'''


class FlightSearchAPI:
    def __init__(self):
        self._API_KEY = os.getenv("FLIGHT_API")
        self._ENDPOINT = "https://api.tequila.kiwi.com"
        self._HEADERS = {
            "apikey": self._API_KEY,
        }
        self._fly_from = "SAO"

    def get_city_code(self, city_name):
        # getting information from API
        params = {
            "term": city_name
        }

        response = requests.get(
            url=f"{self._ENDPOINT}/locations/query",
            params=params,
            headers=self._HEADERS
        )
        city = response.json()

        # filtering only the city code
        for location in city["locations"]:
            if location["type"] == "city":
                return location["code"]
        # return locatin not found, if not found
        return "location not found"

    def search_flights(self, fly_to):
        date_from = datetime.now()
        date_to = date_from + timedelta(days=183)

        params = {
            "fly_from": self._fly_from,
            "fly_to": fly_to,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "curr": "BRL",
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 20
        }

        response = requests.get(
            url=f"{self._ENDPOINT}/v2/search",
            params=params,
            headers=self._HEADERS
        ).json()

        return response["data"]
