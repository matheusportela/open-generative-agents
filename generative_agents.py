import logging

from engine.game_engine import GameEngine

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

if __name__ == "__main__":
    engine = GameEngine()
    engine.run()
