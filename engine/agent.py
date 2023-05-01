import logging

from typeguard import typechecked

from engine.memory import MemoryObject, MemoryObjectType


class Agent:
    '''An agent is an entity that can perceive the world and act on it.'''
    @typechecked
    def __init__(self, name: str) -> None:
        self._logger = logging.getLogger(__name__)
        self.name = name

    @typechecked
    def update(self) -> None:
        '''Update the agent.'''
        self._logger.debug(f"Updating agent {self.name}")

    @typechecked
    def perceive(self) -> MemoryObject:
        '''Generate a memory object based on the agent's perception of the world.'''
        self._logger.debug(f"Perceiving with agent {self.name}")
        return MemoryObject(type=MemoryObjectType.OBSERVATION, description="I see a tree")
