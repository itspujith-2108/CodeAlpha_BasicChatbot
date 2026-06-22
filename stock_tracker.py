# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter Stock Name (AAPL, TSLA, GOOGL, MSFT): ").upper()

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock} Investment Value = ${investment}")

    choice = input("Add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value = ${total_investment}")

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")

print("Portfolio saved to portfolio.txt")