import pytest
from game import Game


@pytest.fixture
def board1():
    """Game over for 3x3 2 streak game"""
    return [
        ['*', 'X', '*'],
        ['X', '*', '*'],
        ['*', '*', 'X'],
    ]

@pytest.fixture
def board2():
    """Game over for 3x3 2 streak game"""
    return [
        ['*', '*', '*'],
        ['O', '*', '*'],
        ['*', 'O', '*'],
    ]

@pytest.fixture
def board3():
    """Not a game over for 3x3 2 streak game"""
    return [
        ['*', 'O', '*'],
        ['X', '*', 'X'],
        ['*', 'O', '*'],
    ]

@pytest.fixture
def board4():
    """Game over for 4x4 3 streak game"""
    return [
        ['*', 'O', 'X', '*'],
        ['O', 'X', '*', 'O'],
        ['X', '*', 'X', 'X'],
        ['*', 'O', 'X', '*'],
    ]

@pytest.fixture
def board5():
    """Game over for 4x4 3 streak game"""
    return [
        ['*', 'X', 'X', '*'],
        ['X', 'X', '*', 'X'],
        ['*', '*', 'X', 'X'],
        ['*', 'X', 'X', '*'],
    ]

@pytest.fixture
def board6():
    """Not a game over for 5x5 4 streak game"""
    return [
        ['*', '*', 'X', 'X', '*'],
        ['*', 'X', 'X', '*', '*'],
        ['X', '*', '*', '*', '*'],
        ['X', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*'],
    ]

@pytest.fixture
def board7():
    """Game over for 5x5 4 streak game"""
    return [
        ['*', 'X', '*', '*', '*'],
        ['*', '*', 'X', '*', '*'],
        ['*', '*', '*', 'X', '*'],
        ['*', '*', '*', '*', 'X'],
        ['*', '*', '*', '*', '*'],
    ]

def test_game_over1(board1):
    new_game = Game(streak_size=2)
    new_game.board = board1
    new_game._check_in_all_dimensions()
    assert new_game.game_over == True

def test_game_over2(board2):
    new_game = Game(streak_size=2)
    new_game.board = board2
    new_game._check_in_all_dimensions()
    assert new_game.game_over == True

def test_game_over3(board3):
    new_game = Game(streak_size=2)
    new_game.board = board3
    new_game._check_in_all_dimensions()
    assert new_game.game_over == False

def test_game_over4(board4):
    new_game = Game(streak_size=3, size=4)
    new_game.board = board4
    new_game._check_in_all_dimensions()
    assert new_game.game_over == True


def test_game_over5(board5):
    new_game = Game(streak_size=3, size=4)
    new_game.board = board5
    new_game._check_in_all_dimensions()
    assert new_game.game_over == True

def test_game_over6(board6):
    new_game = Game(streak_size=4, size=5)
    new_game.board = board6
    new_game._check_in_all_dimensions()
    assert new_game.game_over == False

def test_game_over7(board6):
    # Changed streak_size
    new_game = Game(streak_size=3, size=5)
    new_game.board = board6
    new_game._check_in_all_dimensions()
    assert new_game.game_over == True

def test_game_over8(board7):
    new_game = Game(streak_size=4, size=5)
    new_game.board = board7
    new_game._check_in_all_dimensions()
    assert new_game.game_over == True
