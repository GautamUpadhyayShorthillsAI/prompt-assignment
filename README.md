## Nifty 50 Stock Analysis Assignment

### Overview
This assignment involves creating a Python script using ChatGPT or another LLM to fetch and analyze Nifty 50 stock data from NSE. The tasks include:

- Identifying **top 5 gainers and losers** of the day
- Finding **5 stocks that are 30% below their 52-week high**
- Finding **5 stocks that are 20% above their 52-week low**
- Determining **stocks with the highest returns in the last 30 days**
- Creating a **bar chart for top 5 gainers and losers**

### Technologies Used
- **Python**
- **Pandas** (for data processing)
- **Matplotlib** (for visualization)
- **Requests** (for data fetching from NSE API)

### Installation & Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/GautamUpadhyayShorthillsAI/prompt-assignment
   cd prompt-assignment
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

### Running the Script
To execute the script and analyze stock data, run:
```sh
python main.py
```

### Output
The script will generate:
- **A printed list of top gainers and losers**
- **Stock data 30% below 52-week high & 20% above 52-week low**
- **Stocks with the highest 30-day returns**
- **A bar chart visualization**

### Troubleshooting
If you encounter an **HTTP 401 (Unauthorized) error:**
- Retry after a few minutes
- Ensure your IP is not blocked (try using a VPN if needed)

### License
This assignment is for educational purposes only.

