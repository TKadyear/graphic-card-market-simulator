from graphic_card import GraphicCard,GraphicCardConfig
from utils.utils import create_agents
from market import Market

number_agents = 1
number_agents_trend = 1
number_agents_antitrend = 1
# number_agents = 51
# number_agents_trend = 24
# number_agents_antitrend = 24
initial_price_graphic_card = 200
initial_units_graphic_card = 100000
days = 10

price_fluctuation_graphic_card = 0.5
# card = GraphicCard(
#     initial_price_graphic_card,
#     initial_units_graphic_card,
#     price_fluctuation_graphic_card,
# )
# market = Market(
#     card,
#     days,
#     create_agents(number_agents, number_agents_trend, number_agents_antitrend),
# )
# market.startMarket()

config = {
    "graphic_card": {"units": 100000, "price": 200, "percentage_fluctuation": 0.5},
    "agents": {
        "initial_balance": 1000,
        "number_random_agents": 51, 
        "number_antitrend_agents": 24, 
        "number_trend_agents": 24, 
        "number_custom_agents": 1, 
    }
}


class Setup:
    def __init__(self, graphic_card: GraphicCardConfig):
        self.graphic_card = GraphicCard.from_config(graphic_card)


setup = Setup(**config)
