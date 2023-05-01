import logging
from typing import List

from typeguard import typechecked

from engine.agent import Agent


class World:
    '''The world is where the agents live.'''
    @typechecked
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)
        self.agents: List[Agent] = []

    @typechecked
    def add_agent(self, agent: Agent) -> None:
        '''Add an agent to the world.'''
        self.agents.append(agent)

    @typechecked
    def update(self) -> None:
        '''Update the world and its agents.'''
        self._logger.debug("Updating world")

        for agent in self.agents:
            agent.update()
