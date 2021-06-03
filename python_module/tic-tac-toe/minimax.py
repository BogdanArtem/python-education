"""Module that provides ai player"""

from copy import deepcopy
from functools import lru_cache
from player import Player


class AI(Player):
    """Minimax AI player implementation"""
    def make_move(self, game):
        moves = []
        for valid_move in game.valid_moves():
            game_copy = deepcopy(game)
            points = self.minimax(game_copy, valid_move, self)
            moves.append((points, valid_move))

        best_move = max(moves)
        print(best_move)
        print("Best move: ", best_move)
        print("Moves: ", moves)
        game.change_board(*best_move[1], self.sign)

    # @lru_cache(maxsize=None)
    def minimax(self, game, move, player, maximize=1):
        """Return move object with index and points parameters"""
        # print(self.minimax.cache_info())
        debug = True
        game_copy = deepcopy(game)
        if maximize == -1:
            assert player in game_copy.players
            player = game_copy.players[1] if game_copy.players[0] == player else game_copy.players[0]
        if maximize == 1:
            player = self
        game_copy.change_board(*move, player.sign)

        # Exit condition
        if game_copy.game_winner:
            if game_copy.game_winner == self:
                if debug: print(game_copy)
                if debug: print(player)
                if debug: print(move)
                if debug: print(f"Player{self} won")
                return 3
            else:
                if debug: print(game_copy)
                if debug: print(player)
                if debug: print(move)
                if debug: print(f"Player{self} lost")
                return -3
        if game_copy.draw:
            if debug: print("This is draw")
            if debug: print(player)
            if debug: print(move)
            if debug: print(game_copy)
            return 0

        valid_moves = game_copy.valid_moves()

        if maximize == 1:
            # Move of minimizing player
            moves = []
            for valid_move in valid_moves:
                points = self.minimax(game_copy, valid_move, player, maximize=-1)
                moves.append((points, valid_move))
            best_move = max(moves)
            if debug: print("="*10)
            if debug: print(game)
            if debug: print("Maximize moves:")
            if debug: print(moves)
            if debug: print("Best move: ", best_move)
            if debug: print("=" * 10)
            # Return points for minimizing player
            return best_move[0]

        else:
            # Move of maximizing player
            moves = []
            for valid_move in valid_moves:
                points = self.minimax(game_copy, valid_move, player)
                moves.append((points, valid_move))
            best_move = min(moves)

            if debug: print(game)
            if debug: print("Minimize moves:")
            if debug: print(moves)
            if debug: print("Best move: ", best_move)

            return best_move[0]
