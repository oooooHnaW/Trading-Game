from random import choice
from time import perf_counter
from stock import Stock
from event import Event
from math import floor

# Init
CLOCKRATE = 10 # 10 seconds per update - basically clock speed

# Events

randomEvents = []

Crash = Event(0, "Market crash", "The market has crashed", -50)
Growth = Event(1, "Market growth", "The market has grown", 50)

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

def main():
    startTime = perf_counter()
    EventHappened = False
    while True:
        time = perf_counter() - startTime
        if floor(time) % CLOCKRATE == 0 and not EventHappened: # Clock is one update per minute
            affectedSector = choice(list(sectors))
            print(affectedSector) # Gets a sector to affect every minute
            EventHappened = True
        elif floor(time) % CLOCKRATE != 0 and EventHappened:
            EventHappened = False

if __name__ == "__main__":
    main()