from datetime import datetime
from enum import Enum
from typing import List

from typeguard import typechecked


class MemoryObjectType(Enum):
    OBSERVATION = 'observation'
    REFLECTION = 'reflection'
    PLAN = 'plan'


class MemoryObject:
    @typechecked
    def __init__(self, type: MemoryObjectType, description: str, timestamp: datetime = datetime.now()) -> None:
        self.type = type
        self.description = description
        self.created_at = timestamp
        self.accessed_at = timestamp

    # Memory objects can be accessed, which updates the accessed_at timestamp.
    @typechecked
    def access(self) -> 'MemoryObject':
        self.accessed_at = datetime.now()
        return self


class MemoryStream:
    @typechecked
    def __init__(self) -> None:
        self._memory_objects = []

    # Memory stream can store memory objects.
    @typechecked
    def store(self, memory_object: MemoryObject) -> None:
        self._memory_objects.append(memory_object)

    # Memory stream can retrieve memory objects by accessing them. This
    # updates the accessed_at timestamp.
    @typechecked
    def retrieve(self) -> List[MemoryObject]:
        retrieved_objects = [obj.access() for obj in self._memory_objects]
        return retrieved_objects
