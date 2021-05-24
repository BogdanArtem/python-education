"""Tic-Tac-Toe game with arbitrary size of board and size of streak"""


import logging
from typing import Tuple
from collections import deque
logging.basicConfig(level='INFO')


class Board:
    def __init__(self, size=3, streak_size=3):
        self.streak_size = streak_size
        self.board = [['*'] * size for _ in range(size)]
        self.size = size
        self.symbols = ['X', 'O']
        self.game_over = False
        self.turns = 1

    def __str__(self):
        for row in self.board:
            return str(row)

    def play(self):
        while not self.game_over:
            x, y = [int(x) for x in input("Your move: ").split()]
            self.move(x, y)

    def move(self, x, y):
        symbol = self.symbols[self.turns//2]
        logging.info(f"Player {symbol} is moving")
        logging.info(f"Making move at x:{x}, y:{y}...")
        self.board[x][y] = symbol
        logging.info(self)
        # self.turns += 1
        logging.info(f"Turn number: {self.turns}")
        self._check_in_all_dimensions()
        logging.info(f"Game over is: {self.game_over}")


    def _check_in_all_dimensions(self):
        # Copy for board rotation
        board_copy = self.board.copy()

        self._check_rows(board_copy)
        self._check_major_diagonal(board_copy)
        self._check_minor_diagonals(board_copy)
        # Rotate board clockwise
        board_copy = list(zip(*board_copy[::-1]))

        self._check_rows(board_copy)
        self._check_major_diagonal(board_copy)
        self._check_minor_diagonals(board_copy)

        board_copy = list(zip(*board_copy[::-1]))
        self._check_minor_diagonals(board_copy)

        board_copy = list(zip(*board_copy[::-1]))
        self._check_minor_diagonals(board_copy)


    def _check_rows(self, board):
        for row in board:
            # Reset queue for each row
            winning_queue = deque(maxlen=self.streak_size)
            for element in row:
                winning_queue.append(element)
                if len(winning_queue) == self.streak_size and not self.game_over:
                    self._check_game_over(winning_queue)

    def _check_minor_diagonals(self, board):
        """Check small diagonals in one corner of the board
        
        To check all 4 corners the board has to be rotated"""
        pass

    def _check_major_diagonal(self, board):
        """Check the largest diagonal (left-top to bottom-right) for endgame"""
        sequence = (board[x][x] for x in range(len(board)))
        winning_queue = deque(maxlen=self.streak_size)
        for element in sequence:
            #TODO: don't check if less that streak size
            if not self.game_over: 
                winning_queue.append(element)
                self._check_game_over(winning_queue)

    def _check_game_over(self, sequence):
        """Checks if one of sides has won"""
        win1 = [self.symbols[0]] * self.streak_size
        win2 = [self.symbols[1]] * self.streak_size
        final = list(sequence)
        if final == win1:
            self.game_over = True
        elif final == win2:
            self.game_over = True



def main():
    game = Board(size=4, streak_size=3)
    game.play()

    


if __name__ == '__main__':
    main()