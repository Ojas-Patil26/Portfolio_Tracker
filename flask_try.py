from flask import Flask, render_template, request, jsonify
from fetch_stock_prices import fetch_prices

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    stock_prices = None
    if request.method == "POST":
        tickers = request.form.get("tickers")
        if tickers:
            ticker_list = tickers.split(",")
            stock_prices = fetch_prices([ticker.strip() for ticker in ticker_list])

    return jsonify(stock_prices)

if __name__ == "__main__":
    app.run(debug=True)

