from datetime import datetime
from enum import Enum

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
