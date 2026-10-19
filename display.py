import os
import subprocess

def clearScreen():
    if os.name == "nt":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear")

def stockDisplay(stocks, sector, event):
    if event != "none":
        for stock in stocks:
            if stock.sector != sector and sector != "all":
                print(f"Stock: {stock.symbol} - {stock.name} | Sector: {stock.sector} | Price: ${stock.val}\n")
            else:
                if event.effect < 0:
                    stockDecrease(stock, event)
                else:
                    stockIncrease(stock, event)

        # Displays information about what has happened this round
        print("BREAKING NEWS")
        print(f"Event: {event.name} | Affected sectors: {sector} | Percentage change: {event.effect}%")
    else:
        for stock in stocks:
            print(f"Stock: {stock.symbol} - {stock.name} | Sector: {stock.sector} | Price: ${stock.val}\n")

def stockDecrease(stock, event):
    print(f"Stock: {stock.symbol} - {stock.name} | Sector: {stock.sector} | Price: ${stock.val}", end="")
    stock.priceChange(event.effect)
    print(f" | New price:\033[31m ${stock.val}\033[0m\n")

def stockIncrease(stock, event):
    print(f"Stock: {stock.symbol} - {stock.name} | Sector: {stock.sector} | Price: ${stock.val}", end="")
    stock.priceChange(event.effect)
    print(f" | New price:\033[32m ${stock.val}\033[0m\n")