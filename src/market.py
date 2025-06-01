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
        self.product = product
        self.days = days
        self.agents = agents

    def startMarket(self):
        for day in range(self.days):
            print("Day", day + 1)
            marketOrder = RandomOrderIterator(self.agents)
            for agent in marketOrder:
                agent.hello()