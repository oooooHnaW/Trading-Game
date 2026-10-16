from random import choice
from time import perf_counter
from stock import Stock
from event import Event
from math import floor

# Init
CLOCKRATE = 10 # 10 seconds per update - basically clock speed

# Events

randomEvents = ["none"]

randomEvents.append(Event(0, "Market crash", "The market has crashed", -50))
randomEvents.append(Event(1, "Market growth", "The market has grown", 50))

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
        if floor(time) % CLOCKRATE == 0 and not EventHappened: # Clock is one update per 10 seconds(CLOCKRATE)
            affectedSector = choice(list(sectors)) # Chooses an affected sector
            eventType = choice(randomEvents) # Chooses a random event
            EventHappened = True

            if eventType != "none": # Checks that an event has happened first.
                print(f"Affected sector: {affectedSector} | Event type: {eventType.name}") # Displays information and changes to the market
                for stock in stocks:
                    if eventType != "none": # Checks that an event has happened first

                        if affectedSector == "all":
                            print(f"Stock: {stock.symbol} - {stock.name} | Sector: {stock.sector} | Old price: ${stock.val}", end="")
                            stock.priceChange(eventType.effect)
                            print(f" | New price: ${stock.val}\n")
                        elif stock.sector == affectedSector:
                            print(f"Stock: {stock.symbol} - {stock.name} | Sector: {stock.sector} | Old price: ${stock.val}", end="")
                            stock.priceChange(eventType.effect)
                            print(f" | New price: ${stock.val}\n")
            else:
                print("An uneventful 10 seconds...")

        elif floor(time) % CLOCKRATE != 0 and EventHappened:
            EventHappened = False

if __name__ == "__main__":
    main()