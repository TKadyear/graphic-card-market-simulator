class GraphicCard:
    def __init__(
        self,
        price: float,
        units: int,
        price_fluctuation: float,
        percentage_fluctuation: float = 0.5,
    ):
        self.price = price
        self.units = units
        self.price_fluctuation = price_fluctuation
        self.percentage_fluctuation = percentage_fluctuation

    def calc_price_fluctuation(self):
        return (self.price * self.percentage_fluctuation) / 100

    def buy(self):
        self.units -= 1
        self.price += self.calc_price_fluctuation()
        return self

    def sell(self):
        self.units += 1
        self.price -= self.calc_price_fluctuation()
        return self
