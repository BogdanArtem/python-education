from copy import deepcopy
from player import Player
from game import Game


# class AI(Player):
#     def make_move(self, game):
#         game_copy = deepcopy(game)
#         moves = self.valid_moves(game_copy)
#         for move in moves:
#             self.make_move()

    # @staticmethod
    # def valid_moves(game: Game) -> List[Tuple]:
    #     """Return list of tuples with all valid moves for the game"""
    #     moves = []
    #     for x, row in enumerate(game.board):
    #         for y, element in enumerate(row):
    #             if element == " ":
    #                 moves.append((x, y))
    #     return moves
