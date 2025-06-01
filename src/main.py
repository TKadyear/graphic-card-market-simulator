from graphic_card import GraphicCard
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
card = GraphicCard(
    initial_price_graphic_card,
    initial_units_graphic_card,
    price_fluctuation_graphic_card,
)
market = Market(
    card,
    days,
    create_agents(number_agents, number_agents_trend, number_agents_antitrend),
)
market.startMarket()
