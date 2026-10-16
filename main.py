from random import choice
from time import perf_counter
from stock import Stock
from event import Event
from math import floor
import os
import subprocess

# Init
CLOCKRATE = 10 # 10 seconds per update - basically clock speed

# Events

randomEvents = ["none"]

randomEvents.append(Event(1, "Market crash", "The market has crashed", -50))
randomEvents.append(Event(2, "Market growth", "The market has grown", 50))

# Stocks

sectors = {"all"}

stocks = []

stocks.append(Stock("Car Co.", "CARC", "automobile", 100))
stocks.append(Stock("Chug Soda Ltd.", "CGSO", "beverages", 40))
stocks.append(Stock("Guch Soda & Co.", "GCSO", "beverages", 35))
stocks.append(Stock("Teckux", "TUX", "technology", 20))
stocks.append(Stock("Tractors Inc.", "TRAC", "automobile", 90))

# Adds the available sectors - will be needed for random events
for stock in stocks:
    sectors.add(stock.sector)

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

def main():
    startTime = perf_counter()
    EventHappened = False
    while True:
        time = perf_counter() - startTime
        if floor(time) % CLOCKRATE == 0 and not EventHappened: # Clock is one update per 10 seconds(CLOCKRATE)

            clearScreen()
            
            affectedSector = choice(list(sectors)) # Chooses an affected sector
            eventType = choice(randomEvents) # Chooses a random event
            EventHappened = True

            stockDisplay(stocks, affectedSector, eventType)

        elif floor(time) % CLOCKRATE != 0 and EventHappened:
            EventHappened = False

if __name__ == "__main__":
    main()