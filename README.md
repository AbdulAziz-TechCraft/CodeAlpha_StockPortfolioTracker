# 📊 Task 2: Stock Portfolio Tracker

## ✅ Goal:
Build a simple **Stock Portfolio Tracker** that calculates the total investment value based on manually defined stock prices.

---

## 🧠 Concepts Used:
- Python dictionaries
- User input/output
- Basic arithmetic operations
- File handling (optional: save summary to `.txt` file)

---

## 🔧 Features:
- User can enter stock symbols and quantities interactively
- Prices are hardcoded in a dictionary (`e.g., {"AAPL": 180, "TSLA": 250}`)
- Calculates and displays:
  - Per-stock value
  - Total portfolio value
- Optionally saves the summary to a file (`portfolio_summary.txt`)

---

## 📁 File:
- `portfolio_tracker.py` — Main Python script

---

## ▶️ How to Run:

### Option 1: Using Terminal or CMD
```bash
python portfolio_tracker.py

Option 2: Run in VS Code
Open the script file in VS Code

Click Run or use the terminal: python portfolio_tracker.py

💡 Sample Output:
pgsql
Copy
Edit
Enter your stock portfolio (type 'done' to finish):
Stock symbol (e.g., AAPL): AAPL
Enter quantity of AAPL: 5
Stock symbol (e.g., AAPL): TSLA
Enter quantity of TSLA: 3
Stock symbol (e.g., AAPL): done

--- Portfolio Summary ---
AAPL: 5 shares @ $180 = $900
TSLA: 3 shares @ $250 = $750
Total Investment Value: $1650

Summary saved to 'portfolio_summary.txt'
📝 Notes:
You can modify the hardcoded stock_prices dictionary to include more stocks

File saving is optional but useful for logging/reporting

Great starting point to extend into CSV input/output or API integration

👨‍💻 Author:
Submitted for CodeAlpha Internship – Task 2
