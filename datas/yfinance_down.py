import yfinance as yf

# Define the ticker symbol for Ethereum
ticker = 'ETH-USD'

# Download 1 minute data for the last 5 days
eth_data_1m = yf.download(ticker, period='5d', interval='1m')
eth_data_1m.to_csv('eth_data_1m_last_5_days.csv')

# Download 5 minute data for the last 5 days
eth_data_5m = yf.download(ticker, period='5d', interval='5m')
eth_data_5m.to_csv('eth_data_5m_last_5_days.csv')

# Download 15 minute data for the last 5 days
eth_data_15m = yf.download(ticker, period='5d', interval='15m')
eth_data_15m.to_csv('eth_data_15m_last_5_days.csv')

print("Data saved to CSV files.")
