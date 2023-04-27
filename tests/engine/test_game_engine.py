from engine.game_engine import GameEngine

def test_game_engine_is_running_after_start():
    engine = GameEngine()
    engine._start_game()
    assert engine._is_running == True

def test_game_engine_is_not_running_after_stop():
    engine = GameEngine()
    engine._start_game()
    engine._stop_game()
    assert engine._is_running == False
