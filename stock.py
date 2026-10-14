class Stock:
    def __init__(self, Name, Symbol, Sector, Value):
        self.name = Name
        self.symbol = Symbol
        self.sector = Sector
        self.val = Value

    def priceChange(self, Effect):
        self.val += Effect/100 * self.val