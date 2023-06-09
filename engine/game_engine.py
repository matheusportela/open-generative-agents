import logging

from typeguard import typechecked

from .world import World
from .large_language_model import LargeLanguageModel, EchoLLM


class GameEngine:
    '''Engine for the game, containing the main loop.'''
    @typechecked
    def __init__(self, llm: LargeLanguageModel = EchoLLM(), world: World = World()) -> None:
        self._logger = logging.getLogger(__name__)
        self._is_running = False
        self._llm = llm
        self._world = world

    @typechecked
    def run(self) -> None:
        '''Execute the main loop of the game. It will gracefully exit with CTRL+C.'''
        self._start_game()

        try:
            self._execute_game_loop()
        except KeyboardInterrupt:
            self._stop_game()

    @typechecked
    def _start_game(self) -> None:
        self._logger.info("Starting game engine")
        self._is_running = True

    @typechecked
    def _execute_game_loop(self) -> None:
        while self._is_running:
            self._execute_step()

    @typechecked
    def _execute_step(self) -> None:
        self._logger.debug("Executing game step")
        self._world.update()

    @typechecked
    def _stop_game(self) -> None:
        self._logger.info("Stopping game engine")
        self._is_running = False
