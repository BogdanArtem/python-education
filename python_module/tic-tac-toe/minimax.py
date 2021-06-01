from copy import deepcopy
from collections import namedtuple
from player import Player


class AI(Player):
    def make_move(self, game):
        moves = []
        for valid_move in game.valid_moves():
            game_copy = deepcopy(game)
            moves.append(self.minimax(game_copy, valid_move))

        best_move = max(moves, key=lambda x: x.points)
        game.change_board(*best_move.index, self.sign)

    def minimax(self, game, move, maximaze=1):
        """Return move object with index and points parameters"""
        Move = namedtuple("Move", ["index", "points"])
        game_copy = deepcopy(game)
        game_copy.change_board(*move, self.sign)
        if game_copy.game_over:
            return Move(move, maximaze*3)
        if game_copy.draw:
            return Move(move, 0)

        valid_moves = game_copy.valid_moves()
        if maximaze:
            # List of Move objects
            moves = []
            for valid_move in valid_moves:
                moves.append(self.minimax(game_copy, valid_move, maximaze=-1))
            return max(moves, key=lambda x: x.points)
        else:
            # List of Move objects
            moves = []
            for valid_move in valid_moves:
                moves.append(self.minimax(game_copy, valid_move))
            return min(moves, key=lambda x: x.points)
