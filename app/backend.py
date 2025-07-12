from flask import Flask, request, jsonify, render_template
from fetch_stock_prices import fetch_prices
import os

TEMPLATES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
STATIC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

print(f"Templates path: {TEMPLATES_PATH}")
print(f"Static path: {STATIC_PATH}")

app = Flask(__name__,
            template_folder=TEMPLATES_PATH,
            static_folder=STATIC_PATH)


# ✅ THIS ROUTE IS CRITICAL!
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/prices", methods=["POST"])
def api_prices():
    data = request.get_json()
    tickers = data.get("tickers", "")
    if not tickers:
        return jsonify({"error": "No such stock"}), 400

    ticker_list = [ticker.strip() for ticker in tickers.split(",")]
    stock_prices = fetch_prices(ticker_list)

    return jsonify(stock_prices)


if __name__ == "__main__":
    app.run(debug=True)
