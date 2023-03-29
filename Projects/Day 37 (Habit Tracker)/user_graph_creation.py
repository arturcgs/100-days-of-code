import requests
import os

# USER CREATION
username = "arturcgs"
TOKEN = os.getenv("TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

request = requests.post(url=pixela_endpoint, json=params)
print(request.text)

# GRAPH CREATION
graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}

params = {
    "id": "graph1",
    "name": "Meditation Tracker",
    "unit": "min",
    "type": "int",
    "color": "ajisai",
}

request = requests.post(url=graph_endpoint, json=params, headers=headers)
print(request.text)