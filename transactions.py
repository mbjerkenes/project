# Transactions ledger
class Transaction:
    def __init__(self, ticker, quantity, price, transaction_type):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        self.transaction_type = transaction_type
        self.total = quantity * price if transaction_type == "buy" else -quantity * price

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
