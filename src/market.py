from iterator import RandomOrderIterator
from agents import BaseAgent
from app_store import AppStore
from utils.logger import logger

class MarketSimulation:
    __store: AppStore = None
    __agents: BaseAgent =None
    
    def __init__(
        self,
        store: AppStore,
        agents: list[BaseAgent],
    ):
        self.__store = store
        self.__agents = agents

    def __finish(self):
        logger.info("---- Final Status ----")
        for agent in self.__agents:
            agent.show_status()
    def start(self):
        for iteration in range(self.__store.total_iterations):
            self.__store.iteration = iteration
            logger.info(f"----Iteration {self.__store.iteration} ----")
            marketOrder = RandomOrderIterator(self.__agents)
            for agent in marketOrder:
                agent.act()
            self.__store.save_last_iteration_price()
        self.__finish()

