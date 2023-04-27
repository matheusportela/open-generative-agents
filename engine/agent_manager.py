from engine.agent import Agent


class AgentManager:
    def __init__(self) -> None:
        self.agents = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)
