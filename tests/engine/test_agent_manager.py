from engine.agent import Agent
from engine.agent_manager import AgentManager


def test_agent_manager_adds_agents():
    agent_manager = AgentManager()
    agent = Agent(name='Anna')
    agent_manager.add_agent(agent)
    assert agent_manager.agents == [agent]
