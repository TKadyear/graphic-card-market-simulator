import random
from app_store import AppStore
from abc import ABC, abstractmethod
import uuid
from utils.logger import logger


class BaseAgent(ABC):
    def __init__(self, store: AppStore, balance: float, card_possession: int = 0):
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

    def show_status(self):
        logger.info(
            f"Agent Type: {self.__class__.__name__}; Agent ID: {self.id}; Balance: {self._balance}; Graphic Cards: {self._card_possession}"
        )

    def act(self):
        decision = self.evaluation_possible_options()
        chosenAction = random.choices(
            decision["options"], weights=decision["weights"], k=1
        )[0]
        chosenAction()

    def can_buy(self):
        return self._balance >= self._store.get_graphic_card_price()

    def can_sell(self):
        return self._card_possession >= 1

    def buy(self):
        if self.can_buy():
            self._store.buy_graphic_card()
            self._balance -= self._store.get_graphic_card_price()
            self._card_possession += 1
            logger.info(
                f"Agent ID: {self.id}; Action: Buy; Result:OK; Cards: {self._card_possession}; Balance: {self._balance}"
            )
        else:
            logger.info(
                f"Agent ID: {self.id}; Action: Buy; Result: The graphic card is not affordable; Price Card: {self._store.get_graphic_card_price()}; Balance: {self._balance}"
            )

    def sell(self):
        if self.can_sell():
            self._store.sell_graphic_card()
            self._balance += self._store.get_graphic_card_price()
            self._card_possession -= 1
            logger.info(
                f"Agent ID: {self.id}; Action: Sell; Result:OK; Cards: {self._card_possession}; Balance: {self._balance}"
            )
        else:
            logger.info(
                f"Agent ID: {self.id}; Action: Sell; Result: The agent does not have any graphics cards to sell."
            )

    def nothing(self):
        logger.info(f"Agent ID: {self.id}; Action: Nothing")


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
        if percentage_fluctuation <= 1:
            return {"options": [self.buy, self.nothing], "weights": [0.75, 0.25]}
        else:
            return {"options": [self.sell, self.nothing], "weights": [0.2, 0.8]}


class AgentCustom(BaseAgent):
    def evaluation_possible_options(self):
        percentage_fluctuation = self._store.get_total_fluctuation()
        progress = self._store.iteration / self._store.total_iterations
        threshold_fluctuation = 5
        impact_fluctuation = min(
            abs(percentage_fluctuation) / threshold_fluctuation, 1.0
        )

        weight_progress = 0.2
        weight_fluctuation = 0.8
        
        main_action_probability = (impact_fluctuation * weight_fluctuation) + (
            progress * weight_progress
        )
        remaining_probability = 1 - main_action_probability
        if self._store.iteration >= 990:
            return {
                "options": [self.sell, self.nothing],
                "weights": [main_action_probability, remaining_probability],
            }
        if percentage_fluctuation >= 1:
            return {
                "options": [self.sell, self.nothing],
                "weights": [main_action_probability, remaining_probability],
            }
        else:
            return {
                "options": [self.buy, self.nothing],
                "weights": [main_action_probability, remaining_probability],
            }
