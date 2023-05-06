from abc import ABC, abstractmethod
import logging

from llama_cpp import Llama
from typeguard import typechecked


class LargeLanguageModel(ABC):
    '''An abstract class for large language models.'''
    @abstractmethod
    @typechecked
    def complete(self, prompt: str) -> str:
        pass


class EchoLLM(LargeLanguageModel):
    '''A large language model implementation that simply echoes the prompt.'''
    @typechecked
    def complete(self, prompt: str) -> str:
        return prompt


class LlamaLLM(LargeLanguageModel):
    @typechecked
    def __init__(self, model_path: str):
        self._logger = logging.getLogger(__name__)
        self._llm = Llama(model_path=model_path)

    @typechecked
    def complete(self, prompt: str) -> str:
        output = self._llm(
            f'<s> Q: {prompt} A: ',
            max_tokens=256,
            stop=['</s>', 'Q:', '\n']
        )
        self._logger.debug(f"LlamaLLM output: {output}")
        return output['choices'][0]['text']
