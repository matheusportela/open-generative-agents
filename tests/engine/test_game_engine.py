from engine.game_engine import GameEngine
from engine.world import World


def test_game_engine_is_running_after_start():
    engine = GameEngine()
    engine._start_game()
    assert engine._is_running == True


def test_game_engine_is_not_running_after_stop():
    engine = GameEngine()
    engine._start_game()
    engine._stop_game()
    assert engine._is_running == False


def test_game_engine_initialize_world():
    world = World()
    engine = GameEngine(world=world)
    assert engine._world == world
