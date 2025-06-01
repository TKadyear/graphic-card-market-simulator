from iterator import RandomOrderIterator
from agents import Agent, AgentTrend, AgentAntiTrend
from graphic_card import GraphicCard


class Market:
    def __init__(
        self,
        product: GraphicCard,
        days: int,
        agents: list[Agent | AgentAntiTrend | AgentTrend],
    ):
        self.__product = product
        self._days = days
        self._agents = agents

    def start(self):
        for day in range(self._days):
            print("Day", day + 1)
            marketOrder = RandomOrderIterator(self._agents)
            for agent in marketOrder:
                agent.act()
            self.__product.last_price = self.__product.price
