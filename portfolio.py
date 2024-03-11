# Portfolio
# Still need to add task of calling to displaying portfolio
#def display_portfolio(self):
  #  self.portfolio.display_portfolio()
class Portfolio:
    def __init__(self):
        self.stocks = {}

    def display_portfolio(self):
        if not self.stocks:
            print("Portfolio is empty")
        else:
            print("Portfolio:")
            for stock, quantity in self.stocks.items():
                print(f"{stock}: {quantity}")

#test
                