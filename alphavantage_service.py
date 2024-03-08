# API
import requests

APIKEY = 'IDNUWBH3517E0U6J'

# Function for stock search
def search(string):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={string}&apikey={APIKEY}'
    r = requests.get(url)
    search = r.json()
    bestmatches = search['bestMatches']
    
    return bestmatches

# Function for getting company fundamentals
def company_info(ticker):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={APIKEY}'
    r = requests.get(url)
    companyinfo = r.json()

    return companyinfo


# Function to get stock price
def get_price(ticker):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={APIKEY}'
    r = requests.get(url)
    quote = r.json()
    quote = quote['Global Quote']['02. open']
    
    return quote


# Function for fetching historical stock data
def historical_prices(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={APIKEY}'
    r = requests.get(url)
    historicalprices = r.json()
    historicalprices = historicalprices['Global Quote']['02. open']
    
    return historicalprices



