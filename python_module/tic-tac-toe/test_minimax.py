# import pytest
# from game import Game
# from player import Player
# from minimax import AI
#
#
# @pytest.fixture
# def board1():
#     """3x3 3 streak game"""
#     return [
#         ['O', 'X', ' '],
#         ['X', ' ', ' '],
#         [' ', ' ', ' '],
#     ]
#
# @pytest.fixture
# def player1():
#     return Player(name="Dave", sign="X")
#
# @pytest.fixture
# def ai():
#     return AI(name="HAL 9000", sign="O")
#
#
# def test_valid_moves(board1, ai):
#     game = Game(size=3, streak_size=3)
#     game.board = board1
#     valid_moves = ai._valid_moves(game)
#     assert (0, 0) not in valid_moves
#     assert (2, 2) in valid_moves
#     assert (2, 0) in valid_moves
#     assert (0, 1) not in valid_moves
#
