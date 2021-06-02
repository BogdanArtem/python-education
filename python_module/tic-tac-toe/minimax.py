"""Module that provides ai player"""

from copy import deepcopy
from functools import lru_cache
from collections import namedtuple
from player import Player


class AI(Player):
    """Minimax AI player implementation"""
    def make_move(self, game):
        moves = []
        for valid_move in game.valid_moves():
            game_copy = deepcopy(game)
            moves.append(self.minimax(game_copy, valid_move, self.sign))

        best_move = min(moves, key=lambda x: x.points)
        print(moves)
        print("Best move: ", best_move)
        game.change_board(*best_move.index, self.sign)

    @lru_cache(maxsize=None)
    def minimax(self, game, move, sign, maximaze=1):
        """Return move object with index and points parameters"""
        Move = namedtuple("Move", ["index", "points"])
        game_copy = deepcopy(game)
        game_copy.change_board(*move, sign)
        if game_copy.game_over:
            return Move(move, maximaze*3)
        if game_copy.draw:
            return Move(move, 0)

        valid_moves = game_copy.valid_moves()
        other_sign = game_copy.players[0].sign if game_copy.players[1].sign == sign \
            else game_copy.players[1].sign
        if maximaze:
            # List of Move objects
            moves = []
            for valid_move in valid_moves:
                moves.append(self.minimax(game_copy, valid_move, other_sign, maximaze=-1))
            return max(moves, key=lambda x: x.points)
        else:
            # List of Move objects
            moves = []
            other_sign = game_copy.players[1].sign
            for valid_move in valid_moves:
                moves.append(self.minimax(game_copy, valid_move, other_sign))
            return min(moves, key=lambda x: x.points)
