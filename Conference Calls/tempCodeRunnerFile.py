import yfinance as yf
import pandas as pd

# Define the ticker symbol for Equifax
equifax_symbol = "EFX"

# Create a Ticker object for Equifax
equifax = yf.Ticker(equifax_symbol)

# Fetch the income statement
income_statement = equifax.financials

# Save the income statement to a CSV file
income_statement.to_csv("equifax_income_statement.csv")

# Display the income statement (optional)
print(income_statement)
