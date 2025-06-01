from typing import TypedDict

class GraphicCardConfig(TypedDict):
    price: float
    units: int
    percentage_fluctuation: float

class GraphicCard:
    def __init__(
        self,
        price: float,
        units: int,
        percentage_fluctuation: float = 0.5,
    ):
        self.price = price
        self.units = units
        self.percentage_fluctuation = percentage_fluctuation
    
    @classmethod
    def from_config(cls, config: GraphicCardConfig) -> "GraphicCard":
        return cls(**config)

    def calc_price_fluctuation(self, amount: int):
        return (self.price * self.percentage_fluctuation * amount) / 100

    def buy(self, amount: int = 1):
        # Add logic when there is no more graphic cards
        self.units -= amount
        self.price += self.calc_price_fluctuation(amount)
        return self

    def sell(self, amount: int = 1):
        self.units += amount
        self.price -= self.calc_price_fluctuation()
        return self
