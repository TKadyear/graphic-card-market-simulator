import random


class GraphicCard:
    def __init__(self, price: float, units: int, price_fluctuation: float):
        self.price = price
        self.units = units
        self.price_fluctuation = price_fluctuation

    def calc_price_fluctuation(self):
        return (self.price * 0.5) / 100

    def buy(self):
        self.units -= 1
        self.price += self.calc_price_fluctuation()
        return self

    def sell(self):
        self.units += 1
        self.price -= self.calc_price_fluctuation()
        return self


card = GraphicCard(200, 100000, 0.5)
card.buy()
print(card.price)
print(card.units)


class Agent:
    def __init__(self, balance: float, card_possession: int = 0):
        self.balance = balance
        self.card_possession = card_possession

    def behaviour(self, price_graphic_card: float):
        options = [
            (self.buy, True), 
            (self.sell, True), 
            (self.nothing, False)
            ]
        weights = [0.33, 0.33, 0.33]
        decision, need_args = random.choices(options, weights=weights, k=1)[0]
        
        if need_args:
            decision(price_graphic_card)
        else:
            decision()
        print("Behavior WIP")

    def buy(self, price_graphic_card: float):
        print("Action: Buy")
        self.balance -= price_graphic_card
        self.card_possession += 1
        return self

    def sell(self, price_graphic_card: float):
        self.balance += price_graphic_card
        self.card_possession -= 1
        print("Action: Sell")
        return self

    def nothing(self):
        print("Action: Nothing")
        return self


agent = Agent(1000, 0)
agent.behaviour(200)
