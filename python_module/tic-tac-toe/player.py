"""This module tracks winning and loosing of players"""


import logging


logging.basicConfig(filename='tic-tac-toe.log',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)

class Player:
    """Representation of player that has name and sign"""
    def __init__(self, name, sign):
        self._name = name
        self._sign = sign

    def make_move(self, game):
        """Change state of game's board"""
        print(game)
        print(f"Hi, {self.name} aka '{self.sign}'")
        x_point, y_point = [int(x) for x in input("Enter your move as 'X Y': ").split()]
        game.change_board(x_point, y_point, self.sign)
        if game.game_over is True:
            print(game)
            logging.info("Player %s won", self.name)
            print(f"Congradulations, {self.name}! You won!")

    @property
    def name(self):
        """Get person's name"""
        return self._name

    @property
    def sign(self):
        """Get person's sign"""
        return self._sign
