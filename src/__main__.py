from agents import BaseAgent
from graphic_card import GraphicCard, GraphicCardConfig
from app_store import AppStore
from utils.utils import create_agents
from market import MarketSimulation
from utils.logger import logger

config = {
    "graphic_card": {"units": 100000, "price": 200, "percentage_fluctuation": 0.5},
    "agents": {
        "initial_balance": 1000,
        "number_random_agents": 51,
        "number_antitrend_agents": 24,
        "number_trend_agents": 24,
        "number_custom_agents": 1,
    },
    "total_iterations": 1000,
}


class Setup:
    __graphic_card: GraphicCard = None
    __store: AppStore = None
    __agents: list[BaseAgent] = None
    __market_simulation: MarketSimulation = None

    def __init__(
        self, graphic_card: GraphicCardConfig, agents: dict, total_iterations: int
    ):
        self.__graphic_card = GraphicCard.from_config(graphic_card)
        self.__store = AppStore(self.__graphic_card, total_iterations)
        config_agents = {**agents, "store": self.__store}
        self.__agents = create_agents(**config_agents)
        self.__market_simulation = MarketSimulation(self.__store, self.__agents)

    def start(self):
        self.__market_simulation.start()


logger.info("---Configuration Simulation---")
logger.info(config)
setup = Setup(**config)

logger.info("Start Simulation")
setup.start()
