from datetime import datetime

import typeguard

from engine.memory import MemoryObjectType, MemoryObject


def test_memory_object_stores_type_observation():
    memory_object = MemoryObject(
        type=MemoryObjectType.OBSERVATION,
        description='A red apple'
    )
    assert memory_object.type == MemoryObjectType.OBSERVATION


def test_memory_object_stores_type_reflection():
    memory_object = MemoryObject(
        type=MemoryObjectType.REFLECTION,
        description='A red apple'
    )
    assert memory_object.type == MemoryObjectType.REFLECTION


def test_memory_object_stores_type_plan():
    memory_object = MemoryObject(
        type=MemoryObjectType.PLAN,
        description='A red apple'
    )
    assert memory_object.type == MemoryObjectType.PLAN


def test_memory_object_raises_error_with_invalid_type():
    try:
        MemoryObject(type='not valid', description='A red apple')
        assert False
    except typeguard.TypeCheckError:
        assert True


def test_memory_object_stores_description():
    memory_object = MemoryObject(
        type=MemoryObjectType.OBSERVATION,
        description='A red apple'
    )
    assert memory_object.description == 'A red apple'


def test_memory_object_assigns_now_to_created_at():
    now = datetime(2023, 4, 29, 17, 4, 40, 865693)
    memory_object = MemoryObject(
        type=MemoryObjectType.OBSERVATION,
        description='A red apple',
        timestamp=now
    )
    assert memory_object.created_at == now


def test_memory_object_assigns_now_to_accessed_at():
    now = datetime(2023, 4, 29, 17, 4, 40, 865693)
    memory_object = MemoryObject(
        type=MemoryObjectType.OBSERVATION,
        description='A red apple',
        timestamp=now
    )
    assert memory_object.accessed_at == now


def test_memory_object_created_at_and_accessed_at_are_initialized_equal():
    memory_object = MemoryObject(
        type=MemoryObjectType.OBSERVATION,
        description='A red apple'
    )
    assert memory_object.created_at == memory_object.accessed_at
