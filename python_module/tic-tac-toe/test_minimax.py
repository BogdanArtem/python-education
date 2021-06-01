import pytest
from game import Game
from player import Player
from minimax import AI


@pytest.fixture
def board1():
    """3x3 3 streak game. 1 move to win"""
    return [
        ['O', 'X', 'X'],
        ['X', 'O', ' '],
        ['O', 'X', ' '],
    ]

@pytest.fixture
def board2():
    """3x3 3 streak game. 1 move to win"""
    return [
        ['O', 'X', 'X'],
        [' ', 'O', 'X'],
        ['O', 'X', ' '],
    ]


@pytest.fixture
def player1():
    return Player(name="Dave", sign="X")

@pytest.fixture
def ai():
    return AI(name="HAL 9000", sign="O")


def test_make_move1(board1, ai, player1):
    new_game = Game(size=3, streak_size=3)
    new_game.add_player(player1)
    new_game.add_player(ai)
    new_game.board = board1
    ai.make_move(new_game)
    assert new_game.game_over is True

def test_make_move2(board2, ai, player1):
    new_game = Game(size=3, streak_size=3)
    new_game.add_player(player1)
    new_game.add_player(ai)
    new_game.board = board1
    ai.make_move(new_game)
    assert new_game.game_over is True
