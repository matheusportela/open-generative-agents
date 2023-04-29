from engine.agent import Agent
from engine.perception import Perception


def test_agent_has_name():
    agent = Agent(name='Anna')
    assert agent.name == 'Anna'


def test_agent_can_perceive():
    agent = Agent(name='Anna')
    perception = agent.perceive()
    assert type(perception) is Perception
