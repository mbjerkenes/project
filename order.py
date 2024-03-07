#Order
class Order:
    def __init__(self, user, order_type, symbol, quantity, price=None):
        self.user = user
        self.order_type = order_type  # 'buy', 'sell', 'limit', 'stop'
        self.symbol = symbol
        self.quantity = quantity
        self.price = price  # For limit and stop orders

    def execute(self):
        if self.order_type == 'buy':
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

    #To implement: get current stock price