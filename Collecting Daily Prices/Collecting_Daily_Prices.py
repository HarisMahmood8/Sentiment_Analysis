import yfinance as yf
import pandas as pd

efx = yf.Ticker("EFX")

# daily prices
historical_data = efx.history(period="1d")

historical_data.to_csv("equifax_historical_prices.csv")