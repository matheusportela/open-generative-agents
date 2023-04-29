import logging

from typeguard import typechecked

from engine.perception import Perception


class Agent:
    @typechecked
    def __init__(self, name: str) -> None:
        self._logger = logging.getLogger(__name__)
        self.name = name

    @typechecked
    def update(self) -> None:
        self._logger.debug(f"Updating agent {self.name}")

    # Agent can perceive the world and update its memory stream with the
    # acquired information.
    @typechecked
    def perceive(self) -> Perception:
        self._logger.debug(f"Perceiving with agent {self.name}")
        return Perception()
