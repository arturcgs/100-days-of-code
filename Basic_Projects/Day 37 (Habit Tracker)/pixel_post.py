import requests
import os
from datetime import date, timedelta
from random import randint

TOKEN = os.getenv("TOKEN")

headers = {
    "X-USER-TOKEN": TOKEN
}

# posting for today

today = str(date.today().strftime("%Y%m%d"))

params = {
    "date": today,
    "quantity": "5"
}

request = requests.post(url="https://pixe.la/v1/users/arturcgs/graphs/graph1", json=params, headers=headers)

# populating the graph with information from the past (just to look pretty)


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2022, 2, 1)
end_date = date.today()
for single_date in daterange(start_date, end_date):
    params = {
        "date": single_date.strftime("%Y%m%d"),
        "quantity": str(randint(5, 30))
    }

    request = requests.post(url="https://pixe.la/v1/users/arturcgs/graphs/graph1", json=params, headers=headers)
    print(f"{single_date.strftime('%d/%m/%Y')}{request.text}")





