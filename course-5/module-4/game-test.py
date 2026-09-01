
# Given the code from the Game class stored in a file named game.py, generate a set of meaningful unit tests for this class using the pytest module in Python. The tests should cover these scenarios:*
# *Correct answer given*
# *Incorrect answer given*
# *Invalid input (out of range)* 
# *Invalid input (non-numeric)*
# *Provide the code for a set of the unit tests and instructions on how to set up the tests.*

import pytest
from game import Game

def test_initial_state():
    game = Game()
    assert game.score == 0
    assert not game.is_game_over()

def test_get_final_score_before_game_over():
    game = Game()
    with pytest.raises(ValueError):
        game.get_final_score()

def test_get_final_score_after_game_over():
    game = Game()
    game._game_over = True
    assert game.get_final_score() == 0
