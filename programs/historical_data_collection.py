import yfinance as yf

# Download historical data for required stocks
def historical_data_collection(ticker):
    data = yf.download(tickers=ticker, period='max')
    data.to_csv(f'../data/{ticker}.csv')
    return True