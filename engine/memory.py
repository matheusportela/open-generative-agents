from datetime import datetime
from enum import Enum
from typing import List

from typeguard import typechecked


class MemoryObjectType(Enum):
    OBSERVATION = 'observation'
    REFLECTION = 'reflection'
    PLAN = 'plan'


class MemoryObject:
    '''A memory that can be stored in a memory stream.'''
    @typechecked
    def __init__(self, type: MemoryObjectType, description: str, timestamp: datetime = datetime.now()) -> None:
        self.type = type
        self.description = description
        self.created_at = timestamp
        self.accessed_at = timestamp

    @typechecked
    def access(self) -> 'MemoryObject':
        '''Access this memory object, which updates the accessed_at timestamp.'''
        self.accessed_at = datetime.now()
        return self


class MemoryStream:
    '''An in-memory storage and retrieval unit of memory objects.'''
    @typechecked
    def __init__(self) -> None:
        self._memory_objects = []

    #
    @typechecked
    def store(self, memory_object: MemoryObject) -> None:
        '''Store a memory object in this memory stream.'''
        self._memory_objects.append(memory_object)

    @typechecked
    def retrieve(self) -> List[MemoryObject]:
        '''Retrieve the most important memory objects from this memory stream.

        This updates the accessed_at timestamp of the retrieved objects.
        '''
        retrieved_objects = [obj.access() for obj in self._memory_objects]
        return retrieved_objects
