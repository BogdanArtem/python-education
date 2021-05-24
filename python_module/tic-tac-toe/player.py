class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def make_move(self, game):
        print(game)
        print(f"Hi, {self.name} aka '{self.sign}'")
        x_point, y_point = [int(x) for x in input("Enter your move as 'X Y': ").split()]
        game.change_board(x_point, y_point, self.sign)
        if game.game_over == True:
            print(game)
            print(f"Congradulations, {self.name}! You won!")
