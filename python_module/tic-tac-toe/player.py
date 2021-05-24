import logging


logging.basicConfig(filename='tic-tac-toe.log',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)



class Player:
    def __init__(self, name, sign):
        self._name = name
        self._sign = sign

    def make_move(self, game):
        print(game)
        print(f"Hi, {self.name} aka '{self.sign}'")
        x_point, y_point = [int(x) for x in input("Enter your move as 'X Y': ").split()]
        game.change_board(x_point, y_point, self.sign)
        if game.game_over == True:
            print(game)
            logging.info(f"Player {self.name} won")
            print(f"Congradulations, {self.name}! You won!")

    @property
    def name(self):
        return self._name

    @property
    def sign(self):
        return self._sign
