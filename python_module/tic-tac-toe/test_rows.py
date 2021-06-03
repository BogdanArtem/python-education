from game import Game
from player import Player
import pytest

@pytest.fixture
def board1():
    """Not a game over for 3x3 3 streak game"""
    return [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['X', '*', 'X'],
    ]

@pytest.fixture
def board2():
    """Game over for 3x3 3 streak game"""
    return [
        ['*', '*', '*'],
        ['*', '*', '*'],
        ['X', 'X', 'X'],
    ]

@pytest.fixture
def board3():
    """Game over for 3x3 3 streak game"""
    return [
        ['X', '*', '*'],
        ['X', '*', '*'],
        ['X', '*', '*'],
    ]

@pytest.fixture
def board4():
    """Not game over for 3x3 3 streak game"""
    return [
        ['X', 'O', 'X'],
        ['X', 'X', 'O'],
        ['O', '*', 'O'],
    ]

@pytest.fixture
def board5():
    """Not game over for 4x4 3 streak game"""
    return [
        ['X', 'X', 'O', 'X'],
        ['X', 'X', '*', 'O'],
        ['*', '*', '*', '*'],
        ['O', 'O', '*', 'O'],
    ]

@pytest.fixture
def board6():
    """Game over from 4x4 3 streak game"""
    return [
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'O', 'O', 'O'],
        ['O', '*', 'O', '*'],
    ]

@pytest.fixture
def board7():
    """Game over from 4x4 4 streak game"""
    return [
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O'],
    ]

@pytest.fixture
def board8():
    """Not a game over from 4x4 4 streak game"""
    return [
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'X'],
    ]

@pytest.fixture
def board9():
    """Game over for 5x5 3 streak game"""
    return [
        ['X', 'X', 'O', 'X', 'O'],
        ['X', 'O', 'X', 'O', 'O'],
        ['X', 'O', 'X', 'O', 'X'],
        ['O', 'X', 'O', 'X', 'O'],
        ['O', 'O', 'X', 'X', 'O'],
    ]

@pytest.fixture
def board10():
    """Not a game over for 5x5 3 streak game"""
    return [
        ['X', 'X', 'O', 'X', 'O'],
        [' ', 'O', 'X', 'O', 'O'],
        ['X', 'O', 'X', ' ', 'X'],
        ['O', ' ', 'O', ' ', 'O'],
        ['O', 'O', 'X', 'X', 'O'],
    ]

@pytest.fixture
def player1():
    return Player(name="Sam", sign="X")

@pytest.fixture
def player2():
    return Player(name="Nick", sign="O")

def test_rows_game_over1(board1, player1, player2):
    new_game = Game(size=3, streak_size=3)
    new_game.add_player(player1)
    new_game.add_player(player2)
    new_game.board = board1
    new_game._check_in_all_dimensions()
    assert not new_game.game_winner

def test_rows_game_over2(board2, player1, player2):
    new_game = Game(size=3, streak_size=3)
    new_game.add_player(player1)
    new_game.add_player(player2)
    new_game.board = board2
    new_game._check_in_all_dimensions()
    assert new_game.game_winner is player1

def test_rows_game_over3(board3, player1, player2):
    new_game = Game(size=3, streak_size=3)
    new_game.add_player(player1)
    new_game.add_player(player2)
    new_game.board = board3
    new_game._check_in_all_dimensions()
    assert new_game.game_winner

def test_rows_game_over4(board4, player1, player2):
    new_game = Game(size=3, streak_size=3)
    new_game.add_player(player1)
    new_game.add_player(player2)
    new_game.board = board4
    new_game._check_in_all_dimensions()
    assert not new_game.game_winner

def test_rows_game_over5(board5, player1, player2):
    new_game = Game(size=4, streak_size=3)
    new_game.add_player(player1)
    new_game.add_player(player2)
    new_game.board = board5
    new_game._check_in_all_dimensions()
    assert not new_game.game_winner

def test_rows_game_over6(board6, player1, player2):
    new_game = Game(size=4, streak_size=3)
    new_game.add_player(player1)
    new_game.add_player(player2)
    new_game.board = board6
    new_game._check_in_all_dimensions()
    assert new_game.game_winner

def test_rows_game_over7(board7, player1, player2):
    new_game = Game(size=4, streak_size=4)
    new_game.add_player(player1)
    new_game.add_player(player2)
    new_game.board = board7
    new_game._check_in_all_dimensions()
    assert new_game.game_winner

def test_rows_game_over8(board8, player1, player2):
    new_game = Game(size=4, streak_size=4)
    new_game.add_player(player1)
    new_game.add_player(player2)
    new_game.board = board8
    new_game._check_in_all_dimensions()
    assert not new_game.game_winner

def test_rows_game_over9(board9, player1, player2):
    new_game = Game(size=5, streak_size=3)
    new_game.add_player(player1)
    new_game.add_player(player2)
    new_game.board = board9
    new_game._check_in_all_dimensions()
    assert new_game.game_winner

def test_rows_game_over10(board10, player1, player2):
    new_game = Game(size=5, streak_size=3)
    new_game.add_player(player1)
    new_game.add_player(player2)
    new_game.board = board10
    new_game._check_in_all_dimensions()
    assert not new_game.game_winner
