from SheetAPI import SheetAPI
from FlightSearchAPI import FlightSearchAPI
from EmailManager import EmailManager


def send_email_to_all_users(
        price,
        city_from,
        airport_from_code,
        city_to,
        airport_to_code,
        departure_date,
        arrival_date,
        nights_in_destination
):
    """
    This function sends an email, to alert all user of a good flight deal.
    :param price: str
    :param city_from: str
    :param airport_from_code: str
    :param city_to: str
    :param airport_to_code: str
    :param departure_date: str
    :param arrival_date: str
    :param nights_in_destination: str
    :return: None
    """
    email = EmailManager()
    users_sheet = sheet.read_from_sheet(page="users")

    for user in users_sheet["users"]:
        text = f"Subject:Low price alert!\nHello {user['name']} {user['surname']},\n\n" \
               f"We have found a good deal for you! Only R${price} to fly from " \
               f"{city_from}-{airport_from_code} to {city_to}-{airport_to_code} " \
               f"from {departure_date} to {arrival_date} for {nights_in_destination} nights!"
        email.send_email(
            text=text,
            receiver_email=user["email"]
        )


if __name__ == "__main__":
    # initializing API objects
    sheet = SheetAPI()
    flight_searcher = FlightSearchAPI()

    # reading information from sheet
    flight_sheet = sheet.read_from_sheet(page="prices")

    for desired_flight in flight_sheet["prices"]:
        flight_informations = flight_searcher.search_flights(fly_to=desired_flight["iata"])
        for flight in flight_informations:
            if flight["price"] <= desired_flight["price"]:
                send_email_to_all_users(
                    price=f"{flight['price']: .2f}",
                    city_from=flight['cityFrom'],
                    airport_from_code=flight['flyFrom'],
                    city_to=flight['cityTo'],
                    airport_to_code=flight['flyTo'],
                    departure_date=flight['route'][0]['local_departure'][:10],
                    arrival_date=flight['route'][1]['local_arrival'][:10],
                    nights_in_destination=flight['nightsInDest']
                )
