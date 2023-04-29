import logging
from typing import List

from typeguard import typechecked

from engine.agent import Agent


class World:
    @typechecked
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)
        self.agents: List[Agent] = []

    @typechecked
    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    @typechecked
    def update(self) -> None:
        self._logger.debug("Updating world")

        for agent in self.agents:
            agent.update()
