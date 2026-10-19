class Stock:
    def __init__(self, Name, Symbol, Sector, Value, Amount):
        self.name = Name
        self.symbol = Symbol
        self.sector = Sector
        self.val = Value
        self.amount = Amount

    def priceChange(self, Effect):
        self.val += round(Effect/100 * self.val, 2)