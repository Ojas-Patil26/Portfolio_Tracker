import yfinance as yf

def current_price(instrument):
    data = yf.Ticker(instrument).history(period="5d")
    close_prices = data["Close"].dropna()

    if close_prices.empty:
        return "No data available"

    last_price = round(close_prices.iloc[-1], 2)

    return f"{last_price}"

def fetch_prices(tickers):
    prices = {}
    for ticker in tickers:
        try:
            prices[ticker] = current_price(ticker)
        except Exception as e:
            prices[ticker] = f"Error: {e}"
    return prices

if __name__ == "__main__":
    stock_list = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    stock_prices = fetch_prices(stock_list)
    for stock, price in stock_prices.items():
        print(f"{stock}: {price}")
