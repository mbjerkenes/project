# This is the main script for running the investment program

import pandas as pd
import numpy as np


from user import User
from order import Order
from alphavantage_service import get_price, search
from stock import Stock

def main():
    # Display the available stocks and their prices
    # Prompt the user to log in or create a new account
    print("Investmest platform")
    print("What would you like to do?")
    print("1. Add user")
    print("2. Log in")
    
    choice = input("Enter your choice:")
    if choice == "1":
        new_user = input("What is your name?")
        startingbalance = input("How much money do you want to add?")
        User(new_user, startingbalance)
    
    username = input("Enter your username: ")
    user = User(username)

    # Allow the user to buy and sell stocks
    while True:
        # Display the main menu and prompt the user to choose an option
        print("1. My profile")
        print("2. Investment")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Display the profile menu and prompt the user to choose an option
            print("1. Add money")
            print("2. Balance")
            print("3. My portfolio")
            profile_choice = input("Enter your choice: ")

            if profile_choice == "1":
                # Prompt the user to enter the amount of money to add and update their balance
                amount = float(input("Enter the amount to add: "))
                User.add_money(amount)
                print(f"Added {amount} to your balance.")
            elif profile_choice == "2":
                # Display the user's current balance
                print(f"Your balance is {user.balance}.")
            elif profile_choice == "3":
                # Display the user's portfolio
                User.display_portfolio(user)

        elif choice == "2":
            # Display the investment menu and prompt the user to choose an option
            print("1. Search stocks")
            stocksearch = input("Enter your choice: ")
            bestmatches = search(stocksearch)
            searchoutput = [match['2. name'] for match in bestmatches]
            print(searchoutput)
            choosestock = input("Choose stock: ")
            

            if investment_choice == "1":
                # Prompt the user to enter a stock symbol and display the stock information
                stock_symbol = input("Enter the stock symbol: ")
                stock_info = Stock.fetch_stock_data(stock_symbol)
                print(f"{stock_symbol}: {stock_info['price']}")

                # Prompt the user to buy or sell the stock
                action = input("Do you want to buy or sell this stock? ")
                if action == "buy":
                    quantity = int(input("Enter the quantity: "))
                    Order.buy(user, ticker, quantity)
                elif action == "sell":
                    quantity = int(input("Enter the quantity: "))
                    Order.sell(user, ticker)

    # Display the user's portfolio
    # display_portfolio(user)

if __name__ == "__main__":
    main()