from iterator import RandomOrderIterator
from agents import Agent, AgentTrend, AgentAntiTrend
from graphic_card import GraphicCard


class Market:
    def __init__(
        self,
        product: GraphicCard,
        iterations: int,
        agents: list[Agent | AgentAntiTrend | AgentTrend],
    ):
        self.__product = product
        self._iterations = iterations
        self._agents = agents

    def start(self):
        for iteration in range(self._iterations):
            print("Iteration", iteration + 1)
            marketOrder = RandomOrderIterator(self._agents)
            for agent in marketOrder:
                agent.act()
            self.__product.last_price = self.__product.price
