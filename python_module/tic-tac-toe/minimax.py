"""Module that provides ai player"""

from copy import deepcopy
from functools import lru_cache
from player import Player


class AI(Player):
    """Minimax AI player implementation"""
    def make_move(self, game):
        moves = []
        for valid_move in game.valid_moves():
            points = self.minimax(game, valid_move, self, -1)
            moves.append((points, valid_move))

        best_move = max(moves)
        # print(best_move)
        # print("Best move: ", best_move)
        # print("Moves: ", moves)
        game.change_board(*best_move[1], self.sign)

    # @lru_cache(maxsize=None)
    def minimax(self, game, move, player, maximize=1):
        """Return move object with index and points parameters"""
        # print(self.minimax.cache_info())
        game_copy = deepcopy(game)
        game_copy.change_board(*move, player.sign)

        # Exit condition
        if game_copy.game_winner:
            if game_copy.game_winner == self:
                return 3
            else:
                return -3
        if game_copy.draw:
            return 0

        valid_moves = game_copy.valid_moves()
        if maximize == 1:
            player = self
            moves = []
            for valid_move in valid_moves:
                game_copy2 = deepcopy(game_copy)
                points = self.minimax(game_copy2, valid_move, player, maximize=-1)
                moves.append((points, valid_move))
            best_move = max(moves) # max?
            # Return points for minimizing player
            return best_move[0]

        else:
            assert player in game.players
            player = game.players[1] if game.players[0] == player else game.players[0]
            moves = []
            for valid_move in valid_moves:
                game_copy2 = deepcopy(game_copy)
                points = self.minimax(game_copy2, valid_move, player)
                moves.append((points, valid_move))
            best_move = min(moves)
            return best_move[0]
