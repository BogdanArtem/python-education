import pytest
from main import Board


@pytest.fixture
def board1():
    """Game over for 3x3 3 streak game"""
    return [
        ['X', 'O', 'X'],
        ['X', 'X', 'O'],
        ['O', '*', 'X'],
    ]

@pytest.fixture
def board2():
    """Game over for 3x3 3 streak game"""
    return [
        ['X', 'O', 'O'],
        ['X', 'O', 'O'],
        ['O', '*', 'X'],
    ]

@pytest.fixture
def board3():
    """Not a game over for 3x3 3 streak game"""
    return [
        ['X', 'O', 'O'],
        ['X', '*', 'O'],
        ['O', '*', 'X'],
    ]


@pytest.fixture
def board4():
    """Game over for 4x4 3 streak game"""
    return [
        ['X', 'X', 'O', 'X'],
        ['X', 'X', '*', 'O'],
        ['*', '*', 'X', '*'],
        ['O', 'O', '*', 'O'],
    ]

@pytest.fixture
def board5():
    """Game over for 4x4 3 streak game"""
    return [
        ['X', 'X', 'O', 'O'],
        ['X', 'X', 'O', 'O'],
        ['*', 'O', '*', '*'],
        ['O', 'O', '*', 'O'],
    ]

@pytest.fixture
def board6():
    """Not a game over for 5x5 4 streak game"""
    return [
        ['X', 'X', 'O', 'X', 'O'],
        ['*', 'O', 'X', 'O', 'O'],
        ['X', 'O', 'O', '*', 'X'],
        ['O', 'X', 'O', 'O', 'O'],
        ['O', 'O', 'X', 'X', '*'],
    ]

@pytest.fixture
def board7():
    """Game over for 5x5 4 streak game"""
    return [
        ['X', 'X', 'O', 'X', 'O'],
        ['*', 'O', 'X', 'O', 'O'],
        ['X', 'O', 'O', '*', 'X'],
        ['O', 'X', 'O', 'O', 'O'],
        ['O', 'O', 'X', 'X', 'O'],
    ]

def test_game_over1(board1):
    new_board = Board()
    new_board.board = board1
    new_board._check_in_all_dimensions()
    assert new_board.game_over == True

def test_game_over2(board2):
    new_board = Board()
    new_board.board = board2
    new_board._check_in_all_dimensions()
    assert new_board.game_over == True

def test_game_over3(board3):
    new_board = Board()
    new_board.board = board3
    new_board._check_in_all_dimensions()
    assert new_board.game_over == False

def test_game_over4(board4):
    new_board = Board(streak_size=3, size=4)
    new_board.board = board4
    new_board._check_in_all_dimensions()
    assert new_board.game_over == True


def test_game_over5(board5):
    new_board = Board(streak_size=3, size=4)
    new_board.board = board5
    new_board._check_in_all_dimensions()
    assert new_board.game_over == True

def test_game_over6(board6):
    new_board = Board(streak_size=4, size=5)
    new_board.board = board6
    new_board._check_in_all_dimensions()
    assert new_board.game_over == False

def test_game_over7(board6):
    # Changed streak_size
    new_board = Board(streak_size=3, size=5)
    new_board.board = board6
    new_board._check_in_all_dimensions()
    assert new_board.game_over == True

def test_game_over8(board7):
    new_board = Board(streak_size=4, size=5)
    new_board.board = board7
    new_board._check_in_all_dimensions()
    assert new_board.game_over == True
