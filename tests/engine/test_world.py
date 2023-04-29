from engine.agent import Agent
from engine.world import World


def test_world_adds_agents():
    world = World()
    agent = Agent(name='Anna')
    world.add_agent(agent)
    assert world.agents == [agent]
