import logging

from typeguard import typechecked


class Agent:
    @typechecked
    def __init__(self, name: str) -> None:
        self._logger = logging.getLogger(__name__)
        self.name = name

    @typechecked
    def update(self) -> None:
        self._logger.debug(f"Updating agent {self.name}")
