class Bot:
    def __init__(self, buyFluctuation, acceptRange):
        self.money = 1000
        self.buyFluc = buyFluctuation # In percentage. When the market fluctuates how much, it will buy. How whale it is
        self.acceptRange = acceptRange # In percentage. What is the range they are willing to sell stocks for. How impulsive they are
        self.stocks = []

    def evaluate(self, NewStocks, OldStocks, marketPrices):
        for NewStock in NewStocks:
            for OldStock in OldStocks:
                if OldStock.name == NewStock.name and abs(NewStock.val - OldStock.val)/OldStock.val <= self.buyFluc/100:
                    # Gets the value of the new stock and calculates maximum stocks the bot is able to purchase.
                    if (self.money // NewStock.val) >= NewStock.amount:
                        amountToBuy = NewStock.amount
                    else:
                        amountToBuy = self.money // NewStock.val

                    # Purchase the stock
                    for marketStock in marketPrices:
                        if marketStock.name == NewStock.name:
                            self.purchase(NewStock.val, marketStock.val, amountToBuy) # Going to have to find a way to get the market listing price Perhaps pass the list of stocks around?

                            # This is hellish and is 100% going to need a double check in the future.

    def purchase(self, ListPrice, availablePrice, purchaseAmount, stock):
        if availablePrice >= (ListPrice - ListPrice * self.acceptRange/100) and availablePrice <= (ListPrice + ListPrice * self.acceptRange/100):
            self.money -= purchaseAmount * ListPrice
            self.stocks.append(stock)