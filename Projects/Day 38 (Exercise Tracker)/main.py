from NutriApi import NutriAPI
from SheetAPI import SheetAPI
from datetime import datetime


if __name__ == "__main__":
    # aks query for user
    query = input("What exercise did you do? ")

    # Creating API objects
    exercise = NutriAPI(query=query)
    sheet = SheetAPI()

    # sending data to google sheets
    for i in range(len(exercise.name)):
        a = sheet.add_row(
            date=datetime.now().strftime("%d/%m/%Y"),
            time=datetime.now().hour,
            exercise=exercise.name[i],
            duration=exercise.duration[i],
            calories=exercise.calories[i],
        )
