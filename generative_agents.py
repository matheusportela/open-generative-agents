import logging

from engine.agent import Agent
from engine.world import World
from engine.game_engine import GameEngine


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

if __name__ == "__main__":
    world = World()
    world.add_agent(Agent(name='Anna'))

    engine = GameEngine(world=world)
    engine.run()
