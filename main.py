import requests
import pandas as pd
import matplotlib.pyplot as plt
import time

# URL for NSE Nifty 50 data
NSE_URL = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.nseindia.com/market-data/live-equity-market",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}

# Initialize session
session = requests.Session()
session.headers.update(HEADERS)

# First request to get session cookiescd 
session.get("https://www.nseindia.com", headers=HEADERS)
time.sleep(2)  # Pause to avoid being blocked

# Fetch data from NSE with session
response = session.get(NSE_URL)

if response.status_code != 200:
    print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
    exit()

try:
    data = response.json()
    if "data" not in data:
        print("Error: Unexpected JSON format.")
        exit()
except requests.exceptions.JSONDecodeError:
    print("Error: Failed to decode JSON. Response may be blocked.")
    exit()

# Convert to DataFrame
stocks = pd.DataFrame(data["data"])
print("Available columns:", stocks.columns)

# Ensure the correct column names
high52_col = "yearHigh" if "yearHigh" in stocks.columns else "high52"
low52_col = "yearLow" if "yearLow" in stocks.columns else "low52"

# Drop rows with missing 52-week high/low values
stocks = stocks.dropna(subset=[high52_col, low52_col, "lastPrice", "pChange"])

# Top 5 Gainers and Losers
gainers = stocks.nlargest(5, "pChange")
losers = stocks.nsmallest(5, "pChange")

# Stocks 30% below 52-week high
stocks["percent_below_52_high"] = ((stocks[high52_col] - stocks["lastPrice"]) / stocks[high52_col]) * 100
below_52_week_high = stocks[stocks["percent_below_52_high"] >= 30].nlargest(5, "percent_below_52_high")

# Stocks 20% above 52-week low
stocks["percent_above_52_low"] = ((stocks["lastPrice"] - stocks[low52_col]) / stocks[low52_col]) * 100
above_52_week_low = stocks[stocks["percent_above_52_low"] >= 20].nlargest(5, "percent_above_52_low")

# Highest returns in last 30 days (assuming "pChange" reflects short-term gains)
highest_returns = stocks.nlargest(5, "pChange")


# Print results
print("\nTop 5 Gainers:\n", gainers[["symbol", "pChange"]])
print("\nTop 5 Losers:\n", losers[["symbol", "pChange"]])

print("\nStocks 30% Below 52-Week High:\n", below_52_week_high[["symbol", "lastPrice", "percent_below_52_high"]]
      if not below_52_week_high.empty else "No data available")

print("\nStocks 20% Above 52-Week Low:\n", above_52_week_low[["symbol", "lastPrice", "percent_above_52_low"]]
      if not above_52_week_low.empty else "No data available")

print("\nHighest Returns in Last 30 Days:\n", highest_returns[["symbol", "pChange"]])

# Plot top gainers and losers
plt.figure(figsize=(10, 5))
plt.bar(gainers["symbol"], gainers["pChange"], color='green', label='Gainers')
plt.bar(losers["symbol"], losers["pChange"], color='red', label='Losers')
plt.xlabel("Stocks")
plt.ylabel("% Change")
plt.title("Top 5 Gainers and Losers")
plt.legend()
plt.show()