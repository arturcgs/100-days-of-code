import requests
import os


class StockAPI:
    def __init__(self, stock: str):
        # starting variables
        self._stock = stock
        self.endpoint = "https://www.alphavantage.co/query"
        self.api_key = os.getenv("STOCK_API_KEY")
        self.params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": self._stock,
            "outputsize": "compact",
            "apikey": self.api_key
        }

        # getting data from API
        self._data = requests.get(self.endpoint, params=self.params).json()

        self.percentage_change = self.calculate_percentage_change()

    def calculate_percentage_change(self):
        # separating days
        data = self._data["Time Series (Daily)"]
        data_keys = list(data)
        yesterday = float(data[data_keys[0]]['4. close'])
        day_before = float(data[data_keys[1]]['4. close'])

        # calculating percentage
        return ((yesterday * 100) / day_before) - 100
