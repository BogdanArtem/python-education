"""Tic-Tac-Toe game with arbitrary size of board and size of streak"""


import sys
from player import Player
from minimax import AI
from game import Game


def get_player():
    """Get user input"""
    p_inp = False
    while not p_inp:
        try:
            name, sign = input("Enter the \
player name and it's sign, e.g. 'Alex X': ").split()
            is_ai = input("Is it AI? Y/N: ").lower()
            if len(sign) > 1:
                raise ValueError
            if is_ai not in ("y", "n"):
                raise ValueError
            p_inp = True
            is_ai = True if is_ai == "y" else False
        except ValueError:
            print("Please, enter valid data")
    return AI(name, sign) if is_ai else Player(name, sign)


def get_game():
    """Get user input for game"""
    p_inp = False
    while not p_inp:
        try:
            size, streak = [int(x) for x in input("Enter the size \
of the board and streak size like '5 3': ").split()]
            if streak > size:
                raise ValueError
            p_inp = True
        except ValueError:
            print("Please, enter valid name and sign")
    return Game(size, streak)


def new_game():
    """Start new game with adaptive size of board"""
    game = get_game()
    player1 = get_player()
    player2 = get_player()
    game.add_player(player1)
    game.add_player(player2)
    game.start()


def check_logs():
    """Print all logs form file"""
    with open('tic-tac-toe.log', 'r') as file:
        logs = file.read()
        if logs == '':
            print("The file is empty")
        else:
            print(logs)


def delete_logs():
    """Delete all logs from file"""
    with open('tic-tac-toe.log', 'w') as _:
        print("Logs are cleaned")
    main()


def main():
    """Entrypoint for the game"""

    print("1 - New game")
    print("2 - Check logs")
    print("3 - Delete logs")
    print("4 - Exit")

    num = int(input('\n-> '))
    if num == 1:
        new_game()
    elif num == 2:
        check_logs()
    elif num == 3:
        delete_logs()
    elif num == 4:
        sys.exit()
    else:
        print("Wrong number!")


if __name__ == '__main__':
    main()
