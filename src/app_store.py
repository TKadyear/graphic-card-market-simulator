from graphic_card import GraphicCard

class AppStoreMeta(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]

class AppStore(metaclass=AppStoreMeta):
    _iteration: int = None
    _total_iterations: int = None
    _graphic_card: GraphicCard = None

    def __init__(self, graphic_card: GraphicCard, total_iterations: int):
        self._graphic_card = graphic_card
        self._total_iterations = total_iterations
        self._iteration = 0

    @property
    def iteration(self):
        return self._iteration
    @property
    def total_iterations(self):
        return self._total_iterations

    @iteration.setter
    def iteration(self, iteration: int):
        self._iteration = iteration
        return self

    def save_last_iteration_price(self):
        self._graphic_card.last_price = self._graphic_card.price

    def get_last_iteration_price(self):
        return self._graphic_card.last_price

    def get_total_fluctuation(self):
        return self._graphic_card.get_total_fluctuation()

    def get_graphic_card_price(self):
        return self._graphic_card.price
    
    def buy_graphic_card(self, amount: int = 1):
        self._graphic_card.buy(amount)

    def sell_graphic_card(self, amount: int = 1):
        self._graphic_card.sell(amount)
