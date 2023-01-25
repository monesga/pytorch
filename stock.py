import yfinance as yf

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info['regularMarketPrice']

ticker = input("Enter a ticker symbol: ")
price = get_stock_price(ticker)
print(f"The current price of {ticker} is ${price}.")
