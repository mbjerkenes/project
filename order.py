class Order:
    def __init__(self, user, symbol, quantity, price=None):
        self.user = user
        self.symbol = symbol
        self.quantity = quantity
        self.price = price  # For limit and stop orders
        self.order_type = None

    def prompt_order_type(self):
        print("Choose the order type:")
        print("1. Buy")
        print("2. Sell")
        choice = input("Enter your choice (1/2): ")
        if choice == "1":
            self.order_type = "buy"
        elif choice == "2":
            self.order_type = "sell"
        else:
            print("Invalid choice. Please enter 1 or 2.")
            self.prompt_order_type()

    def execute(self):
        if self.order_type is None:
            self.prompt_order_type()
            self.execute()
        elif self.order_type == 'buy':
            self.buy()
        elif self.order_type == 'sell':
            self.sell()
        elif self.order_type == 'limit':
            self.limit_order()
        elif self.order_type == 'stop':
            self.stop_order()

    def buy(self):
        # Implement buy order logic here
        current_price = self.get_current_stock_price()
        total_cost = self.quantity * current_price
        if self.user.balance >= total_cost:
            self.user.balance -= total_cost
            if self.symbol in self.user.portfolio:
                self.user.portfolio[self.symbol] += self.quantity
            else:
                self.user.portfolio[self.symbol] = self.quantity
            self.user.transaction_history.append(f"Bought {self.quantity} shares of {self.symbol} at {current_price} {self.user.currency}")
            print(f"Bought {self.quantity} shares of {self.symbol} at {current_price} {self.user.currency}")
        else:
            print("Insufficient funds to execute buy order.")

    def sell(self):
        # Implement sell order logic here
        if self.symbol not in self.user.portfolio or self.user.portfolio[self.symbol] < self.quantity:
            print("Insufficient shares to execute sell order.")
        else:
            current_price = self.get_current_stock_price()
            total_sale = self.quantity * current_price
            self.user.balance += total_sale
            self.user.portfolio[self.symbol] -= self.quantity
            self.user.transaction_history.append(f"Sold {self.quantity} shares of {self.symbol} at {current_price} {self.user.currency}")
            print(f"Sold {self.quantity} shares of {self.symbol} at {current_price} {self.user.currency}")

    def limit_order(self):
        # Implement limit order logic here
        pass

    def stop_order(self):
        # Implement stop order logic here
        pass

    def get_current_stock_price(self):
        # Implement a function to get current stock price
        # For now, returning a random price for demonstration purposes
        import random
        return random.randint(50, 200)

class User:
    def __init__(self, name, balance, currency="USD"):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.portfolio = {}
        self.transaction_history = []

# Example usage:
user = User("Sample User", 1000)  # Adjusted the initial balance to 1000
order = Order(user, 'AAPL', 1)  # Buying 10 shares of AAPL
order.execute()