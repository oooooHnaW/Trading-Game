from random import choice

class Event:
    def __init__(self, IDnum, Name, Message, Sector, Effect):
        self.IDnum = IDnum
        self.name = Name
        self.msg = Message
        self.sector = Sector
        self.effect = Effect

class Stock:
    def __init__(self, Name, Symbol, Sector, Value):
        self.name = Name
        self.symbol = Symbol
        self.sector = Sector
        self.val = Value

    def priceChange(self, Effect):
        self.val += Effect/100 * self.val

randomEvents = {}

def main():
    pass

if __name__ == "__main__":
    main()