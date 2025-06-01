import random
from graphic_card import GraphicCard
from abc import ABC, abstractmethod
import uuid
from utils.logger import logger

class BaseAgent(ABC):
    def __init__(self, store: GraphicCard, balance: float, card_possession: int = 0):
        self._store = store
        self._balance = balance
        self._card_possession = card_possession
        self.id = str(uuid.uuid4())
        self._turn = 0

    @abstractmethod
    def evaluation_possible_options(self):
        pass
    
    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self, value: int):
        self._turn = value

    # Todo: Remove this method after adding logger to all classes
    def hello(self):
        logger.info("Hello Agent")

    def act(self):
        logger.info("action")
        decision = self.evaluation_possible_options()
        chosenAction = random.choices(
            decision["options"], weights=decision["weights"], k=1
        )[0]
        chosenAction()

    def can_buy(self):
        return self._balance >= self._store.price

    def can_sell(self):
        return self._card_possession >= 1

    def buy(self):
        if self.can_buy():
            print("ID:", self.id, "; AgentType:Agent; Action: Buy")
            self._store.buy()
            self._balance -= self._store.price
            self._card_possession += 1
        else:
            print(
                "The graphic card is not affordable. Balance:",
                self._balance,
                "Price Graphic Card:",
                self._store.price,
            )
        return self

    def sell(self):
        if self.can_sell():
            self._store.sell()
            self._balance += self._store.price
            self._card_possession -= 1
            print("ID:", self.id, ";AgentType:Agent;Action: Sell")
        else:
            print("ID:", self.id,"The agent does not have any graphics cards to sell.")

        return self

    def nothing(self):
        print("ID:", self.id, ";AgentType:Agent;Action: Nothing")
        return self


class Agent(BaseAgent):
    def evaluation_possible_options(
        self,
    ):
        options = [self.buy, self.sell, self.nothing]
        weights = [0.33, 0.33, 0.33]
        return {"options": options, "weights": weights}


class AgentTrend(BaseAgent):
    def evaluation_possible_options(self):
        percentage_fluctuation = self._store.get_total_fluctuation()
        print("percentage_fluctuation", percentage_fluctuation)
        if percentage_fluctuation >= 1:
            return {
                "options": [self.buy, self.nothing],
                "weights": [0.75, 0.25],
            }
        else:
            return {
                "options": [self.sell, self.nothing],
                "weights": [0.2, 0.8],
            }


class AgentAntiTrend(BaseAgent):
    def evaluation_possible_options(self):
        percentage_fluctuation = self._store.get_total_fluctuation()
        print("percentage_fluctuation", percentage_fluctuation)
        if percentage_fluctuation <= 1:
            return {"options": [self.buy, self.nothing], "weights": [0.75, 0.25]}
        else:
            return {"options": [self.sell, self.nothing], "weights": [0.2, 0.8]}


class AgentCustom(BaseAgent):
    def evaluation_possible_options(self):
        percentage_fluctuation = self._store.get_total_fluctuation()
        print("percentage_fluctuation", percentage_fluctuation)
        # Todo: Refactor this logic
        if percentage_fluctuation <= 1:
            return {"options": [self.buy, self.nothing], "weights": [0.75, 0.25]}
        else:
            return {"options": [self.sell, self.nothing], "weights": [0.75, 0.25]}
