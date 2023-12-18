import requests
import os

'''
https://www.nutritionix.com/business/api
'''

APP_ID = os.getenv("NUTRI_ID")
API_KEY = os.getenv("NUTRI_KEY")
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


class NutriAPI:
    def __init__(self, query):
        # getting response and saving in attributes
        self._response = self._get_data(query).json()
        self.name = [str(exercise["name"]) for exercise in self._response["exercises"]]
        self.duration = [exercise["duration_min"] for exercise in self._response["exercises"]]
        self.calories = [exercise["nf_calories"] for exercise in self._response["exercises"]]

        # counter
        self.num = 0

    @staticmethod
    def _get_data(query):
        params = {
            "query": query,
            "gender": "male",
            "weight_kg": 72,
            "height_cm": 172,
            "age": 25
        }

        return requests.post(url=ENDPOINT, json=params, headers=headers)
