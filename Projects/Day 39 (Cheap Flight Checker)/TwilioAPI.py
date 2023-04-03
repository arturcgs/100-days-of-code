from twilio.rest import Client
import os


class TwilioAPI:
    def __init__(self):
        self._SID = os.getenv("TWILIO_SID")
        self._TOKEN = os.getenv("TWILIO_TOKEN")

    def send_message(
            self,
            price,
            city_from,
            airport_from_code,
            city_to,
            airport_to_code,
            departure_date,
            arrival_date,
            nights_in_destination
    ):
        text = f"Low price alert! Only R${price} to fly from "
        f"{city_from}-{airport_from_code} to {city_to}-{airport_to_code} "
        f"from {departure_date} to {arrival_date}"
        f" for {nights_in_destination} nights!"

        client = Client(self._SID, self._TOKEN)

        message = client.messages.create(
            body=text,
            from_="+14406364934",
            to="+5511964922298"
        )

        return message
