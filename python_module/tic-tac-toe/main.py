"""Tic-Tac-Toe game with arbitrary size of board and size of streak"""


import logging
from collections import deque
from player import Player


logging.basicConfig(level='INFO')


class Game:
    """Class that represents game with players"""

    def __init__(self, size=3, streak_size=3):
        self.streak_size = streak_size
        self.board_size = size
        self.board = [[' '] * size for _ in range(size)]
        self.symbols = ['X', 'O']
        self._game_over = False
        self.turns = 1

    def __repr__(self):
        """Game representation.
        
        Row consists of 3 textual lines. Contiguous rows share 1 textual line"""
        render = ""
        for num, row in enumerate(self.board):
            line1 = "".join([" -- " for _ in row]) + "\n"
            line2 = "".join(["| " + element + " " for element in row]) + "| " + str(num) + "\n"
            render += (line1 + line2)
        render += "".join([" -- " for _ in row]) + "\n"
        render += "".join([f"  {num} " for num, _ in enumerate(self.board)])
        return render

    @property
    def game_over(self):
        return self._game_over

    @game_over.setter
    def game_over(self, value: bool):
        self._game_over = value

    # def move(self, x_point, y_point):
    #     """Change symbols on board."""
    #     symbol = self.symbols[self.turns//2]
    #     logging.info("Player %s is moving", symbol)
    #     logging.debug("Making move at x:%d, y:%d...", x_point, y_point)
    #     self.board[x_point][y_point] = symbol

    #     # self.turns += 1
    #     logging.info("Turn number: %d", self.turns)
    #     self._check_in_all_dimensions()
    #     logging.info("Game over is: %")

    def change_board(self, x_point, y_point, sign):
        try:
            if self.board[x_point][y_point] != " ":
                raise ValueError(f"Sector [{x_point}] [{y_point}] is already filled")
            self.board[x_point][y_point] = sign
        except ValueError as e:
            logging.exception(e)
        self._check_in_all_dimensions()

    def _check_in_all_dimensions(self):
        """Check for endgame in rows and diagonals.

        After check of all rows and diagonals the board is
        Turned at 90 degrees for another check
        """
        # Copy for board rotation
        board_copy = self.board.copy()
        for _ in range(2):
            self._check_rows(board_copy)
            self._check_diagonals(board_copy)
            # Rotate board clockwise
            board_copy = list(zip(*board_copy[::-1]))

    def _check_diagonals(self, board):
        """Traverse matrix diagonally.

        Link to the algorithm https://www.youtube.com/watch?v=T8ErAYobcbc
        """
        row = len(board)
        col = len(board[0])
        for line in range(1, (row + col)):
            start_col = max(0, line - row)
            count = min(line, (col - start_col), row)
            diagonal_queue = deque(maxlen=self.streak_size)
            for j in range(0, count):
                diagonal_queue.append(board[min(row, line) - j - 1][start_col + j])
                if len(diagonal_queue) == self.streak_size and not self.game_over:
                    self._check_game_over(diagonal_queue)

    def _check_rows(self, board):
        """"Traverse all rows and find streak of 'X' or 'O' """
        for row in board:
            # Reset queue for each row
            row_queue = deque(maxlen=self.streak_size)
            for element in row:
                row_queue.append(element)
                if len(row_queue) == self.streak_size and not self.game_over:
                    self._check_game_over(row_queue)

    def _check_game_over(self, sequence):
        """Checks if one of sides has won"""
        win1 = [self.symbols[0]] * self.streak_size
        win2 = [self.symbols[1]] * self.streak_size
        sequence = list(sequence)
        if sequence == win1 or sequence == win2:
            self.game_over = True


def main():
    """Entrypoint for the game"""
    game = Game(size=3, streak_size=3)
    player1 = Player(name="Dima", sign="X")
    player2 = Player(name="Vasya", sign="O")

    while True:
        if game.game_over:
            break
        player1.make_move(game)

        if game.game_over:
            break
        player2.make_move(game)


if __name__ == '__main__':
    main()
