from typing import List

from typeguard import typechecked

from engine.agent import Agent


class AgentManager:
    @typechecked
    def __init__(self) -> None:
        self.agents: List[Agent] = []

    @typechecked
    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)
