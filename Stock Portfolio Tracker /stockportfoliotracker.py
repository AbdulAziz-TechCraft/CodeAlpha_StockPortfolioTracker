stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2900,
    "AMZN": 3500,
    "MSFT": 300
}

portfolio = {}
total_value = 0

print("Enter your stock portfolio (type 'done' to finish):")

while True:
    stock = input("Stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Try again.")
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = quantity
    total_value += stock_prices[stock] * quantity

print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock]*qty}")
print("Total Investment Value: $", total_value)

# Save to file (optional)
with open("portfolio_summary.txt", "w") as file:
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
    file.write(f"Total Investment Value: ${total_value}\n")

print("\nSummary saved to 'portfolio_summary.txt'")
