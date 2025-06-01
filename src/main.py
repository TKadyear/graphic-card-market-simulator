from graphic_card import GraphicCard, GraphicCardConfig
from utils.utils import create_agents
from market import Market

config = {
    "graphic_card": {"units": 100000, "price": 200, "percentage_fluctuation": 0.5},
    "agents": {
        "initial_balance": 1000,
        "number_random_agents": 51,
        "number_antitrend_agents": 24,
        "number_trend_agents": 24,
        "number_custom_agents": 1,
    },
    "days": 1000
}


class Setup:
    def __init__(self, graphic_card: GraphicCardConfig, agents: dict, days: int):
        self.graphic_card = GraphicCard.from_config(graphic_card)
        self.config_agents = {**agents, "store": self.graphic_card}
        self.agents = create_agents(**self.config_agents)
        self.market = Market(self.graphic_card, days, self.agents)

    def start(self):
        self.market.start()


setup = Setup(**config)

setup.start()