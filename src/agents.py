import random


class Agent:
    def __init__(self, balance: float, card_possession: int = 0):
        self.balance = balance
        self.card_possession = card_possession

    def evaluation_possible_options(
        self, 
    ):
        options = [(self.buy, True), (self.sell, True), (self.nothing, False)]
        weights = [0.33, 0.33, 0.33]
        return {
                "options": options,
                "weights": weights
        }
    def hello(self):
        print("Hello Agent")
    def behaviour(self, price_graphic_card: float):
        decision =self.evaluation_possible_options()
        chosenAction, need_args = random.choices(decision["options"], weights=decision["weights"], k=1)[0]

        if need_args:
            chosenAction(price_graphic_card)
        else:
            chosenAction()

    def buy(self, price_graphic_card: float):
        print("AgentType:Agent;Action: Buy")
        self.balance -= price_graphic_card
        self.card_possession += 1
        return self

    def sell(self, price_graphic_card: float):
        self.balance += price_graphic_card
        self.card_possession -= 1
        print("AgentType:Agent;Action: Sell")
        return self

    def nothing(self):
        print("AgentType:Agent;Action: Nothing")
        return self


class AgentTrend:
    def __init__(self, balance: float, card_possession: int = 0):
        self.balance = balance
        self.card_possession = card_possession

    def hello(self):
        print("Hello Agent Trend")
    def evaluation_possible_options(
        self, price_graphic_card: float, last_iteration_price: float
    ):
        percentage_fluctuation = (price_graphic_card * 100) / last_iteration_price - 100
        print("percentage_fluctuation", percentage_fluctuation)
        if(percentage_fluctuation >= 1):
            return {
                "options": [(self.buy, True),(self.nothing, False)],
                "weights": [0.75,0.25]
            }
        else:
            return {
                "options": [(self.sell, True),(self.nothing, False)],
                "weights": [0.75,0.25]
            }


    def behaviour(self, price_graphic_card: float, last_iteration_price: float):
        decision =self.evaluation_possible_options(price_graphic_card, last_iteration_price)
        chosenAction, need_args = random.choices(decision["options"], weights=decision["weights"], k=1)[0]

        if need_args:
            chosenAction(price_graphic_card)
        else:
            chosenAction()

    def buy(self, price_graphic_card: float):
        print("AgentType:AgentTrend; Action: Buy")
        self.balance -= price_graphic_card
        self.card_possession += 1
        return self

    def sell(self, price_graphic_card: float):
        self.balance += price_graphic_card
        self.card_possession -= 1
        print("AgentType:AgentTrend; Action: Sell")
        return self

    def nothing(self):
        print("AgentType:AgentTrend; Action: Nothing")
        return self

class AgentAntiTrend:
    def __init__(self, balance: float, card_possession: int = 0):
        self.balance = balance
        self.card_possession = card_possession

    def hello(self):
        print("Hello Agent AntiTrend")
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


    def behaviour(self, price_graphic_card: float, last_iteration_price: float):
        decision =self.evaluation_possible_options(price_graphic_card, last_iteration_price)
        chosenAction, need_args = random.choices(decision["options"], weights=decision["weights"], k=1)[0]

        if need_args:
            chosenAction(price_graphic_card)
        else:
            chosenAction()

    def buy(self, price_graphic_card: float):
        print("AgentType:AgentAntiTrend; Action: Buy")
        self.balance -= price_graphic_card
        self.card_possession += 1
        return self

    def sell(self, price_graphic_card: float):
        self.balance += price_graphic_card
        self.card_possession -= 1
        print("AgentType:AgentAntiTrend; Action: Sell")
        return self

    def nothing(self):
        print("AgentType:AgentAntiTrend; Action: Nothing")
        return self