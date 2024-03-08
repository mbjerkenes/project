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
            # Use the function from the API module to get company information
            company_info = api.company_info(self.symbol)
            if 'Name' in company_info:
                self.name = company_info['Name']
            else:
                print(f"Error: Unable to fetch company information for {self.symbol}")
            
            # Use the function from the API module to get stock price
            self.price = api.get_price(self.symbol)
            print(f"Stock data updated for {self.symbol}: Name = {self.name}, Price = {self.price}")
        except Exception as e:
            print(f"Error fetching stock data: {e}")

# Example usage:

# Create an instance of a stock
#apple_stock = Stock("AAPL")

# Fetch stock data from the API and update the name and price
#apple_stock.fetch_stock_data()

# Display updated stock information
#print(f"Stock Symbol: {apple_stock.symbol}")
#print(f"Stock Name: {apple_stock.name}")
#print(f"Updated Stock Price: {apple_stock.price}")