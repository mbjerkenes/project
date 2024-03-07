# API
import requests


# Function for fetching stock price
def get_price(ticker):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey=IDNUWBH3517E0U6J'
    r = requests.get(url)
    quote = r.json()
    quote = quote['Global Quote']['02. open']
    
    return quote



# Function for fetching historical stock data
def historical_prices(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=IDNUWBH3517E0U6J'
    r = requests.get(url)
    historicalprices = r.json()
    historicalprices = timeseries['Global Quote']['02. open']
    
    return historicalprices





