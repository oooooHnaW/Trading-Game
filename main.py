from random import choice
from time import perf_counter
from stock import Stock
from event import Event

# Events

randomEvents = []

fullCrash = Event(0, "Market crash", "The market has completely crashed", "all", -50)

# Stocks

Stocks = []

Stocks.append(Stock("Car Co.", "CARC", "automobile", 100))
Stocks.append(Stock("Chug Soda Ltd.", "CGSO", "beverages", 40))
Stocks.append(Stock("Guch Soda & Co.", "GCSO", "beverages", 35))
Stocks.append(Stock("Teckux", "TUX", "technology", 20))
Stocks.append(Stock("Tractors Inc.", "TRAC", "automobile", 90))

def marketPotential():
    pass

def main():
    pass

if __name__ == "__main__":
    main()