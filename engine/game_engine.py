import logging

class GameEngine:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

        # This private variable used to control the main loop of the game.
        self._is_running = False

    # Execute the main loop of the game. It will gracefully exit with CTRL+C.
    def run(self) -> None:
        self._start_game()

        try:
            self._execute_game_loop()
        except KeyboardInterrupt:
            self._stop_game()

    def _start_game(self) -> None:
        self._logger.info("Starting game engine")
        self._is_running = True

    def _execute_game_loop(self) -> None:
        while self._is_running:
            self._execute_step()

    def _execute_step(self) -> None:
        self._logger.debug("Executing game step")

    def _stop_game(self) -> None:
        self._logger.info("Stopping game engine")
        self._is_running = False
