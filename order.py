from stock import Stock

class Order:
    def __init__(self, user, ticker, quantity, price=None):
        self.user = user
        self.ticker = ticker
        self.quantity = quantity
        self.price = price  # For limit and stop orders
        self.order_type = None

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
        try:
            current_stock = Stock(self.ticker)
            current_stock.fetch_stock_data()
            current_price = current_stock.price
            total_cost = self.quantity * current_price
            if self.user.balance >= total_cost:
                self.user.balance -= total_cost
                if self.ticker in self.user.portfolio:
                    self.user.portfolio[self.ticker] += self.quantity
                else:
                    self.user.portfolio[self.ticker] = self.quantity
                self.user.transaction_history.append(f"Bought {self.quantity} shares of {self.ticker} at {current_price} {self.user.currency}")
                print(f"Bought {self.quantity} shares of {self.ticker} at {current_price} {self.user.currency}")
            else:
                print("Insufficient funds to execute buy order.")
        except Exception as e:
            print(f"Error executing buy order: {e}")

    def sell(self):
        try:
            current_stock = Stock(self.ticker)
            current_stock.fetch_stock_data()
            current_price = current_stock.price
            if self.ticker not in self.user.portfolio or self.user.portfolio[self.ticker] < self.quantity:
                print("Insufficient shares to execute sell order.")
            else:
                total_sale = self.quantity * current_price
                self.user.balance += total_sale
                self.user.portfolio[self.ticker] -= self.quantity
                self.user.transaction_history.append(f"Sold {self.quantity} shares of {self.ticker} at {current_price} {self.user.currency}")
                print(f"Sold {self.quantity} shares of {self.ticker} at {current_price} {self.user.currency}")
        except Exception as e:
            print(f"Error executing sell order: {e}")

    def limit_order(self):
        # Implement limit order logic here
        pass

    def stop_order(self):
        # Implement stop order logic here
        pass