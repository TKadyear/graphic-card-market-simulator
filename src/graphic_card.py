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
        self._price = price
        self._units = units
        self._percentage_fluctuation = percentage_fluctuation
        self._last_price = price

    @classmethod
    def from_config(cls, config: GraphicCardConfig) -> "GraphicCard":
        return cls(**config)

    @property
    def price(self):
        return self._price

    @property
    def last_price(self):
        return self._last_price

    @last_price.setter
    def last_price(self, last_price: float):
        self._last_price = last_price
        return self

    def get_total_fluctuation(self) -> float:
        return (self._price * 100) / self._last_price - 100

    def _calc_price_fluctuation(self, amount: int):
        return (self._price * self._percentage_fluctuation * amount) / 100

    def buy(self, amount: int = 1):
        # Add logic when there is no more graphic cards
        self._units -= amount
        self._price += self._calc_price_fluctuation(amount)
        return self

    def sell(self, amount: int = 1):
        self._units += amount
        self._price -= self._calc_price_fluctuation()
        return self
