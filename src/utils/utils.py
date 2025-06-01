from agents import Agent, AgentAntiTrend, AgentTrend


def create_agents(
    numberAgents: int, numberAgentsTrend: int, numberAgentsAntiTrends: int
) -> list[Agent | AgentTrend | AgentAntiTrend]:
    print(numberAgents, numberAgentsAntiTrends, numberAgentsTrend)
    initial_balance=1000
    initial_cards=0
    agents = []
    agents += [Agent(initial_balance,initial_cards) for _ in range(numberAgents)]
    agents += [AgentTrend(initial_balance,initial_cards) for _ in range(numberAgents)]
    agents += [AgentAntiTrend(initial_balance,initial_cards) for _ in range(numberAgents)]
    return agents
