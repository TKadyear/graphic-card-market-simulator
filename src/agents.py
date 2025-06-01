import random

from graphic_card import GraphicCard
from abc import ABC, abstractmethod
import uuid


class BaseAgent(ABC):
    def __init__(self, store: GraphicCard, balance: float, card_possession: int = 0):
        self.store = store
        self.balance = balance
        self.card_possession = card_possession
        self.id = str(uuid.uuid4())

    @abstractmethod
    def evaluation_possible_options(self):
        pass

# Todo: Remove this method after adding logger to all classes
    def hello(self):
        print("Hello Agent",self.id)

    def act(self):
        decision = self.evaluation_possible_options()
        chosenAction = random.choices(
            decision["options"], weights=decision["weights"], k=1
        )[0]
        chosenAction()

    def can_buy(self):
        return self.balance >= self.store.price

    def can_sell(self):
        return self.card_possession >= 1

    def buy(self):
        if self.can_buy():
            print("ID:",self.id,"; AgentType:Agent; Action: Buy")
            self.store.buy()
            self.balance -= self.store.price
            self.card_possession += 1
        else:
            print("The graphic card is not affordable. Balance:", self.balance, "Price Graphic Card:",self.store.price )
        return self

    def sell(self):
        if self.can_sell():
            self.store.sell()
            self.balance += self.store.price
            self.card_possession -= 1
            print("ID:",self.id,";AgentType:Agent;Action: Sell")
        else:
            print("The agent does not have any graphics cards to sell.")

        return self

    def nothing(self):
        print("ID:",self.id,";AgentType:Agent;Action: Nothing")
        return self


class Agent(BaseAgent):
    def evaluation_possible_options(
        self,
    ):
        options = [self.buy, self.sell, self.nothing]
        weights = [0.33, 0.33, 0.33]
        return {"options": options, "weights": weights}


class AgentTrend(BaseAgent):
    def evaluation_possible_options(
        self, price_graphic_card: float, last_iteration_price: float
    ):
        percentage_fluctuation = (price_graphic_card * 100) / last_iteration_price - 100
        print("percentage_fluctuation", percentage_fluctuation)
        if percentage_fluctuation >= 1:
            return {
                "options": [(self.buy, True), (self.nothing, False)],
                "weights": [0.75, 0.25],
            }
        else:
            return {
                "options": [(self.sell, True), (self.nothing, False)],
                "weights": [0.75, 0.25],
            }


class AgentAntiTrend(BaseAgent):
    def evaluation_possible_options(
        self, price_graphic_card: float, last_iteration_price: float
    ):
        percentage_fluctuation = (price_graphic_card * 100) / last_iteration_price - 100
        print("percentage_fluctuation", percentage_fluctuation)
        if percentage_fluctuation <= 1:
            return {
                "options": [(self.buy, True), (self.nothing, False)],
                "weights": [0.75, 0.25],
            }
        else:
            return {
                "options": [(self.sell, True), (self.nothing, False)],
                "weights": [0.75, 0.25],
            }


class AgentCustom(BaseAgent):
    def evaluation_possible_options(
        self, price_graphic_card: float, last_iteration_price: float
    ):
        percentage_fluctuation = (price_graphic_card * 100) / last_iteration_price - 100
        print("percentage_fluctuation", percentage_fluctuation)
        if(percentage_fluctuation <= 1):
            return {
                "options": [(self.buy, True),(self.nothing, False)],
                "weights": [0.75,0.25]
            }
        else:
            return {
                "options": [(self.sell, True),(self.nothing, False)],
                "weights": [0.75,0.25]
            }