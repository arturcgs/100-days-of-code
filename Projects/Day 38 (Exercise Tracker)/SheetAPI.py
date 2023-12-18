import requests
import os

'''
https://dashboard.sheety.co/
'''

API_KEY = os.getenv("SHEET_KEY")
ENDPOINT = "https://api.sheety.co/3c2d93ee6776adea1ee6c8610b831960/myWorkouts/workouts"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}


class SheetAPI:
    def __init__(self):
        pass

    @staticmethod
    def add_row(date, time, exercise, duration, calories):
        params = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }
        }

        response = requests.post(url=ENDPOINT, json=params, headers=headers)
        return response
