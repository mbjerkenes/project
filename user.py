# User
from transactions import TransactionHistory, Transaction

class User:
    def __init__(self, name, balance, currency = "USD"):
        self.name = name
        self.balance = float(balance)
        self.currency = currency
        self.portfolio = {}
        self.transaction_history = TransactionHistory() #class from transactions file
    
    # Show the current balance
    def display_balance(self):
        print(f"Current balance ({self.currency}): {self.balance}")

    # Transfer money into the account
    def add_money(self, amount):
        if amount <= 0:
            print("Enter a valid amount")
        else:
            self.balance += amount
            self.transaction_history.add_transaction(Transaction(self.currency, amount, 0, "deposit"))
            print(f"{self.currency} {amount} added to balance. New balance: {self.currency}: {self.balance}")