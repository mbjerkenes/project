# stock
# Implement a Stock class in stock.py for handling stock data.

import alphavantage_service as api

class Stock:
    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price

    def fetch_stock_data(self):
        try:
            new_price = api.get_price(self.symbol)
            if new_price is not None:
                self.price = new_price
                print(f"Stock data updated for {self.symbol}: Price = {self.price}")
            else:
                print(f"Error: Unable to fetch stock data for {self.symbol}")
        except Exception as e:
            print(f"Error fetching stock data: {e}")

    def update_price(self, new_price):
        self.price = new_price

# Example usage:

# Create an instance of a stock
#apple_stock = Stock("AAPL", "Apple Inc.", 150.25)

# Fetch stock data from the API and update the price
#apple_stock.fetch_stock_data()

# Display updated stock information
#print(f"Stock Symbol: {apple_stock.symbol}")
#print(f"Stock Name: {apple_stock.name}")
#print(f"Updated Stock Price: {apple_stock.price}")