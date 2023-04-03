from SheetAPI import SheetAPI
from FlightSearchAPI import FlightSearchAPI
from TwilioAPI import TwilioAPI

if __name__ == "__main__":
    # initializing API objects
    sheet = SheetAPI()
    flight_searcher = FlightSearchAPI()
    twilio = TwilioAPI()

    # reading information from sheet
    sheet_information = sheet.read_from_sheet()

    for desired_flight in sheet_information["prices"]:
        flight_informations = flight_searcher.search_flights(fly_to=desired_flight["iata"])
        for flight in flight_informations:
            if flight["price"] <= desired_flight["price"]:
                a = twilio.send_message(
                    price=f"{flight['price']: .2f}",
                    city_from=flight['cityFrom'],
                    airport_from_code=flight['flyFrom'],
                    city_to=flight['cityTo'],
                    airport_to_code=flight['flyTo'],
                    departure_date=flight['route'][0]['local_departure'][:10],
                    arrival_date=flight['route'][1]['local_arrival'][:10],
                    nights_in_destination=flight['nightsInDest']
                )
                print(a.body)