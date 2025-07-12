import yfinance as yf

def current_price(instrument):
    data = yf.Ticker(instrument).history(period="5d")
    close_prices = data["Close"].dropna()

    if close_prices.empty:
        return "No data available"

    last_price = round(close_prices.iloc[-1], 2)
    last_date = close_prices.index[-1].strftime("%Y-%m-%d")

    return f"{last_price} (as of {last_date})"

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]

for ticker in tickers:
    try:
        price = current_price(ticker)
        if price is not None:
            print(f"{ticker}: {price}")
    except Exception as e:
        print(f"{ticker}: Error - {e}")
