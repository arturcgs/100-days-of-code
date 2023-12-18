from FlightSearchAPI import FlightSearchAPI
from SheetAPI import SheetAPI

if __name__ == "__main__":
    # initializing API objects
    flight_search = FlightSearchAPI()
    sheet = SheetAPI()

    # initializing no options
    yes = ["yes", "y"]
    no = ["no", "n"]

    while True:
        # getting user inputs
        city_name = input("What city would you like to add? ").lower().strip()
        lowest_price = input("What's the lowest price you want for the ticket (in brazilian reais)? ").lower().strip()

        # getting city code
        city_code = flight_search.get_city_code(city_name)

        # writing the information in the sheet
        params = {
            "price": {
                "city": city_name,
                "iata": city_code,
                "price": lowest_price,
            }
        }
        sheet.write_to_sheet(
            page="prices",
            params=params
        )

        user_choice = input("Would you like to continue? ").lower().strip()

        if user_choice in no:
            break
