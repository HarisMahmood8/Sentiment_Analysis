import yfinance as yf
import pandas as pd

equifax_symbol = "EFX"

equifax = yf.Ticker(equifax_symbol)

# income statement
income_statement = equifax.financials

income_statement.to_csv("equifax_income_statement.csv")

print(income_statement)
