from SheetAPI import SheetAPI
from FlightSearchAPI import FlightSearchAPI
#from TwilioAPI import TwilioAPI

if __name__ == "__main__":
    # initializing API objects
    sheet = SheetAPI()
    flight_searcher = FlightSearchAPI()

    # reading information from sheet
    sheet_information = sheet.read_from_sheet()

    for desired_flight in sheet_information["prices"]:
        flight_informations = flight_searcher.search_flights(fly_to=desired_flight["iata"])
        for flight in flight_informations:
            if flight["price"] <= desired_flight["price"]:
                print(f"Low price alert! Only R${flight['price']:.2f} to fly from"
                      f"{flight['cityFrom']}-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']}"
                      f"from "
                      f"for {flight['nightsInDest']} nights!")
        #print(flight_informations)
        break
