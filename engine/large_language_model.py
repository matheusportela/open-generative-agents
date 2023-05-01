from abc import ABC, abstractmethod

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
