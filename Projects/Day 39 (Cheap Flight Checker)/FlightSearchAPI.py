import requests
import os

'''
https://tequila.kiwi.com/portal/docs/tequila_api/locations_api
'''

class FlightSearchAPI:
    def __init__(self):
        self._API_KEY = os.getenv("FLIGHT_API")
        self._ENDPOINT = "https://api.tequila.kiwi.com"
        self._HEADERS = {
            "apikey": self._API_KEY
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
        params = {
            "fly_from": self._fly_from,
            "fly_to": fly_to,
            "date_from": "01/04/2023",
            "date_to": "01/10/2023",
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