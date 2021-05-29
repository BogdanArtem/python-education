"""Tic-Tac-Toe game with arbitrary size of board and size of streak"""


import sys
from player import Player
from game import Game


player1 = Player(name="Default1", sign="X")
player2 = Player(name="Default2", sign="O")

def custom_players():
    """Change default players"""
    name1, sign1 = input("Enter the name of player1 and it's sign, e.g. 'Alex X': ").split()
    name2, sign2 = input("Enter the name of player1 and it's sign, e.g. 'Alex X': ").split()

    global player1
    global player2
    player1 = Player(name1, sign1)
    player2 = Player(name2, sign2)
    print("Names changed \n")
    main()

def new_game():
    """Start new game with adaptive size of board"""
    size, streak_size = [int(x) for x in \
        input("Enter the size of the board and streak size like '5 3': ").split()]
    game = Game(size=size, streak_size=streak_size)
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
    print("2 - Custom names")
    print("3 - Check logs")
    print("4 - Delete logs")
    print("5 - Exit")

    num = int(input('\n-> '))
    if num == 1:
        new_game()
    elif num == 2:
        custom_players()
    elif num == 3:
        check_logs()
    elif num == 4:
        delete_logs()
    elif num == 5:
        sys.exit()
    else: print("Wrong number!")


if __name__ == '__main__':
    main()
