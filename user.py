# User
from transactions import TransactionHistory
class User:
    def __init__(self, name, balance, currency = "USD"):
        self.name = name
        self.balance = balance
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
            print(f"{self.currency} {amount} added to balance. New balance: {self.currency}: {self.balance}")
    
# Initialize test for Marius - starting balance 100 (USD is set a only currency for now)
user = User("Marius", 100)

# Display the current balance
user.display_balance()

# Transfer 500 into the account
user.add_money(500)


