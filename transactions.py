# Transactions ledger
from order import Order

class Transaction:
    def __init__(self, ticker, quantity, price, transaction_type):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        self.transaction_type = transaction_type
        self.total = quantity * price if transaction_type in ["buy", "sell"] else price
    
    def __str__(self):
        if self.transaction_type in ["buy", "sell"]:
            return f"{self.transaction_type.title()} {self.quantity} of {self.ticker} at {self.price}. Total: {self.total}"
        else:
            return f"{self.transaction_type.title()} transaction: {self.total}"

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

# Create some sample transactions
transaction1 = Transaction("AAPL", 10, 150, "buy")
transaction2 = Transaction("GOOGL", 5, 1000, "sell")
transaction3 = Transaction("USD", 0, 500, "deposit")

# Initialize a TransactionHistory instance
transaction_history = TransactionHistory()

# Add the transactions to the transaction history
transaction_history.add_transaction(transaction1)
transaction_history.add_transaction(transaction2)
transaction_history.add_transaction(transaction3)

# Display all transactions
transaction_history.display_transactions()