"""Module to represent tic-tac-toe"""


from collections import deque
import logging
from typing import List, Tuple
from logs_reader import LogsReader


logging.basicConfig(filename='./tic-tac-toe.log',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)


class Game:
    """Class that represents game with adaptive size of board"""

    def __init__(self, size=3, streak_size=3):
        self.streak_size = streak_size
        self._board_size = size
        self.board = [[' '] * size for _ in range(size)]
        self.players = []
        self._game_winner = None
        self._draw = False

    def __repr__(self):
        return str(self.board)

    def __str__(self):
        """Game as string.

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
    def board_size(self):
        """Return board size"""
        return self._board_size

    @property
    def draw(self):
        """Check if game is over"""
        return self._draw

    @draw.setter
    def draw(self, value: bool):
        """Change state of game over"""
        self._draw = value

    @property
    def game_winner(self):
        """Check if game is over"""
        return self._game_winner

    @game_winner.setter
    def game_winner(self, value: bool):
        """Change state of game over"""
        self._game_winner = value

    def start(self):
        """Start the game and play it until draw or game over"""
        logs_reader = LogsReader()
        logs_reader.read()
        while True:
            if self.game_winner:
                count = logs_reader.get_count(self.players[1].name, self.players[0].name)
                print(count)

                logging.info("%s won %s. Count %d:%d", self.players[1],\
                     self.players[0], count[0] + 1, count[1])
                print(f"Congradulations, {self.players[1].name}! You won!")
                break
            if self.draw:
                print(self)
                print("This is draw!")
                logging.info("Draw for %s and %s ", self.players[0], self.players[1])
                break
            self.players[0].make_move(self)
            if self.game_winner:
                count = logs_reader.get_count(self.players[0].name, self.players[1].name)
                logging.info("%s won %s. Count %d:%d", self.players[0], self.players[1], \
                    count[0] + 1, count[1])
                print(self)
                print(f"Congradulations, {self.players[0].name}! You won!")
                break
            if self.draw:
                print("This is draw!")
                logging.info("Draw for %s and %s ", self.players[0], self.players[1])
                break
            self.players[1].make_move(self)

    def change_board(self, x_point: int, y_point: int, sign: str):
        """Edit state of the board using x, y and sing."""
        self.board[x_point][y_point] = sign
        self._check_in_all_dimensions()

    def valid_moves(self) -> List[Tuple]:
        """Return list of tuples with all valid moves for the game"""
        moves = []
        for x, row in enumerate(self.board):
            for y, element in enumerate(row):
                if element == " ":
                    moves.append((x, y))
        return moves

    def move_is_valid(self, x_point: int, y_point: int):
        """Check if x y move is valid for the board"""
        if (x_point, y_point) in self.valid_moves():
            return True
        else:
            print("Please, enter valid coordinates for your move")
            return False

    def add_player(self, player):
        """Add player to the game"""
        if len(self.players) < 2:
            self.players.append(player)
        else:
            print("The game is full")

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

        if self._check_draw():
            self.draw = True

    def _check_draw(self):
        if self.valid_moves():
            return False
        return True

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
                if len(diagonal_queue) == self.streak_size and not self.game_winner:
                    self._check_game_over(diagonal_queue)

    def _check_rows(self, board):
        """"Traverse all rows and find streak of 'X' or 'O' """
        for row in board:
            # Reset queue for each row
            row_queue = deque(maxlen=self.streak_size)
            for element in row:
                row_queue.append(element)
                if len(row_queue) == self.streak_size and not self.game_winner:
                    self._check_game_over(row_queue)

    def _check_game_over(self, sequence):
        """Checks if one of sides has won"""
        win1 = [self.players[0].sign] * self.streak_size
        win2 = [self.players[1].sign] * self.streak_size
        sequence = list(sequence)
        if sequence == win1:
            self.game_winner = self.players[0]
        elif sequence == win2:
            self.game_winner = self.players[1]
