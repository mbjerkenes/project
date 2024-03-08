# This is the main script for running the investment program

import pandas as pd
import numpy as np


from user import User
from order import Order
from alphavantage_service import get_price

def main():
    # Display the available stocks and their prices
    stocks = ["AAPL", "GOOG", "MSFT", "AMZN"]
    for stock in stocks:
        stock_info = get_price(stocks)
        print(f"{stock}: {stock_info['price']}")

    # Allow the user to buy and sell stocks
    while True:
        action = input("Do you want to buy or sell a stock? ")
        if action == "buy":
            stock_symbol = input("Enter the stock symbol: ")
            quantity = int(input("Enter the quantity: "))
            Order.buy(User, stock_symbol, quantity)
        elif action == "sell":
            stock_symbol = input("Enter the stock symbol: ")
            quantity = int(input("Enter the quantity: "))
            Order.sell(User, stock_symbol, quantity)
        else:
            break

    # Display the user's portfolio
    # display_portfolio(user)

if __name__ == "__main__":
    main()