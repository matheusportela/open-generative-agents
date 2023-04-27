from engine.agent import Agent
from engine.world import World


def test_agent_manager_adds_agents():
    agent_manager = World()
    agent = Agent(name='Anna')
    agent_manager.add_agent(agent)
    assert agent_manager.agents == [agent]
