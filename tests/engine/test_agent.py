from engine.agent import Agent

def test_agent_has_name():
    agent = Agent(name='Anna')
    assert agent.name == 'Anna'
