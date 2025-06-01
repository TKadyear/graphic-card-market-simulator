from agents import Agent, AgentAntiTrend, AgentCustom, AgentTrend, BaseAgent
from app_store import AppStore

def create_agents(
    initial_balance: float,
    number_random_agents: int,
    number_trend_agents: int,
    number_antitrend_agents: int,
    number_custom_agents: int,
    store: AppStore,
) -> list[BaseAgent]:
    initial_balance = 1000
    agents = []
    agents += [Agent(store, initial_balance) for _ in range(number_random_agents)]
    agents += [AgentTrend(store, initial_balance) for _ in range(number_trend_agents)]
    agents += [
        AgentAntiTrend(store, initial_balance) for _ in range(number_antitrend_agents)
    ]
    agents += [AgentCustom(store, initial_balance) for _ in range(number_custom_agents)]
    return agents
