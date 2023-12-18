import requests
from twilio.rest import Client
import os

# Variables
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")
account_sid = "ACea3c49fae83e4c51d11160d369877b85"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# Weather API

weather_params = {
    "lat": -23.559604,
    "lon": -46.724125,
    "appid": api_key
}

response = requests.get(owm_endpoint, params=weather_params)
weather_data = response.json()

# separating weather ids and checking if it will rain
weather_ids = [weather["weather"][0]["id"] for weather in weather_data["list"][:4]]

if any(i < 700 for i in weather_ids):
    # sending twilio message
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Vai chover aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        from_="+14406364934",
        to="+5511964922298"
    )
    print(message.status)
