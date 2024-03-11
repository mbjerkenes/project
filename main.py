# This is the main script for running the investment program

import pandas as pd
import numpy as np


from user import User
from order import Order
from alphavantage_service import get_price, search
from stock import Stock
from portfolio import Portfolio

def main():
    # Display the available stocks and their prices
    # Prompt the user to log in or create a new account
    print("Investmest platform")
    print("What would you like to do?")
    print("1. Add user")
    print("2. Log in")
    
    choice = input("Enter your choice:")
    if choice == "1":
        username = input("What is your name?")
        startingbalance = input("How much money do you want to add?")
        user = User(username, startingbalance)
    
        
        #user = User(username)
        
    elif choice == "2":
        username = input("Enter your username: ")
            
        

    # Allow the user to buy and sell stocks
    while True:
        # Display the main menu and prompt the user to choose an option
        print(f"Welcome {username}")
        print("Menu:")
        print("1. My profile")
        print("2. Investment")
        choice = input("Enter your choice: ")
        
        # Split into separate function
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
                continue

        elif choice == "2":
            # Display the investment menu and prompt the user to choose an option
            print("Search stocks")
            stocksearch = input("Search: ")
            bestmatches = search(stocksearch)
            searchoutput = [match['1. symbol'] for match in bestmatches]
            print(searchoutput)
            choosestock = input("Choose stock (1 to 3): ")
            
            if choosestock == "1":
                stock_symbol = searchoutput[0]
                stock_name = bestmatches[0]['2. name']
            elif choosestock == "2":
                stock_symbol = searchoutput[1]
                stock_name = bestmatches[1]['2. name']
            elif choosestock == "3":
                stock_symbol = searchoutput[2]
                stock_name = bestmatches[2]['2. name']
            else:
                print("Invalid input: Please enter the number of the stock.")
            stock_price = get_price(stock_symbol)
            stock = Stock(stock_symbol, stock_name, stock_price)
            print(f"You have chosen {stock_name} with ticker {stock_symbol}")
            print(f"Price is currently at USD {stock.price}")
            print("Stock options:")
            print("1. Buy")
            print("2. Sell")
            choice = input("Enter your choice:")

            if choice == "1":
                print(f"Your balance is currently: " + str(user.balance))
                quantity = input(f"How many shares do you want to buy?")
                order = Order(user, stock_symbol, quantity, stock_price)
                print(order.__dict__)
                order_sum = int(quantity)*int(stock_price)
                print(f"Order: {order.ticker}: {order.quantity} @ {order.price} for a total sum of USD" + str(order_sum))
                order.buy(stock_name, stock_price)


        else: print("Invalid input: Choose 1 or 2.")

"""if investment_choice == "1":
                # Prompt the user to enter a stock symbol and display the stock information
                #stock_symbol = input("Enter the stock symbol: ")
                stock_info = Stock.fetch_stock_data(stock_symbol)
                print(f"{stock_symbol}: {stock_info['price']}")

                # Prompt the user to buy or sell the stock
                action = input("Do you want to buy or sell this stock? ")
                if action == "buy":
                    quantity = int(input("Enter the quantity: "))
                    Order.buy(user, ticker, quantity)
                elif action == "sell":
                    quantity = int(input("Enter the quantity: "))
                    Order.sell(user, ticker)"""

    # Display the user's portfolio
    # display_portfolio(user)

if __name__ == "__main__":
    main()