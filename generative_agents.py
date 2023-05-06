import logging

from engine.agent import Agent
from engine.world import World
from engine.game_engine import GameEngine
from engine.large_language_model import LlamaLLM


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

if __name__ == "__main__":
    llm = LlamaLLM(
        model_path='/Users/portela/Documents/Programming/llama.cpp/models/open_llama_7b_preview_300bt/open_llama_7b_preview_300bt_transformers_weights/ggml-model-f16.bin'
    )

    world = World()
    world.add_agent(Agent(name='Anna'))

    engine = GameEngine(llm=llm, world=world)
    engine.run()
