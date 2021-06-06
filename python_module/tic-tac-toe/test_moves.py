import pytest
from game import Game
from player import Player


@pytest.fixture
def board1():
    """3x3 3 streak game"""
    return [
        ['O', 'X', ' '],
        ['X', ' ', ' '],
        [' ', ' ', ' '],
    ]

@pytest.fixture
def player1():
    return Player(name="Sam", sign="X")

@pytest.fixture
def player2():
    return Player(name="Nick", sign="O")


def test_wrong_move(board1, player1, player2):
    game = Game(size=3, streak_size=3)
    game.board = board1
    game.add_player(player1)
    game.add_player(player2)
    assert game.move_is_valid(100, 100) is False
    assert game.move_is_valid(0, 0) is False
    assert game.move_is_valid(1, 1) is True
