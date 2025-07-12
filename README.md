## 🌌 Stock Price Checker

A simple web app to check real-time stock prices using their ticker symbols (like AAPL or MSFT). It’s made with Python (Flask) for the backend and HTML/CSS/JavaScript for the frontend. The app also has a cool animated galaxy background made with Spline.

---

## 🚀 What This App Does

* Type in stock symbols (like AAPL, TSLA) separated by commas
* Get the current price of each stock using Yahoo Finance data
* Works on desktop and mobile
* Clean UI with a galaxy-themed background ✨

---

## 🧰 What It's Made With

**Frontend:**

* HTML, CSS, and JavaScript
* Spline (for the animated background)

**Backend:**

* Python
* Flask
* yfinance (for stock data)

---

## 🗂️ Folder Structure

```
stock-price-checker/
├── backend.py                 # Flask app (runs the server)
├── fetch_stock_prices.py     # Code to fetch stock prices
├── templates/
│   └── index.html            # HTML frontend
└── static/
    └── style.css             # CSS styling file
```

---

## 🛠️ How to Run It (Step-by-Step)

1. **Download the project** (or clone it if you're using GitHub):

```bash
https://github.com/your-username/stock-price-checker.git
cd stock-price-checker
```

2. **(Optional)** Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install the required Python packages**:

```bash
pip install flask yfinance
```

4. **Run the app**:

```bash
python backend.py
```

5. **Open your browser** and go to:

```
http://127.0.0.1:5000/
```

---

## 📡 API Info (For Developers)

**Endpoint:** `/api/prices` (POST)

**Example Request:**

```json
{
  "tickers": "AAPL, MSFT, TSLA"
}
```

**Example Response:**

```json
{
  "AAPL": "203.57",
  "MSFT": "345.66",
  "TSLA": "887.21"
}
```

---

## 🖼️ UI Preview

* Enter stock tickers in a form
* Click "Check Prices"
* See prices listed below
* Smooth and stylish look with animated galaxy background 🌌

---

## 🔮 Future Ideas

* Show stock graphs
* Let users save a portfolio
* Toggle between dark and light mode
* Add better error messages and validations

---

## 📃 License

MIT License. You can use or improve this however you like.

---

## 🙌 Built By

Made by [Ojas Patil](https://github.com/Ojas-Patil26)

---

> "The stock market is a device for transferring money from the impatient to the patient." – Warren Buffett
