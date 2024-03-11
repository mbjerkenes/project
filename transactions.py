# Transactions ledger
from order import Order

class Transaction:
    def __init__(self, user, ticker, quantity, price, transaction_type):
        self.user = user
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        self.transaction_type = transaction_type
        self.total = quantity * price if transaction_type in ["buy", "sell"] else price
    
    def __str__(self):
        if self.transaction_type in ["buy", "sell"]:
            return f"{self.user.name} {self.transaction_type.title()} {self.quantity} of {self.ticker} at {self.price}. Total: {self.total}"
        else:
            return f"{self.user.name} {self.transaction_type.title()} transaction: {self.total}"

class TransactionHistory:
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
    
    def display_transactions(self):
        if not self.transactions:
            print("No transactions")
        else:
            for transaction in self.transactions:
                print(transaction)