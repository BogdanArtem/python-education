"""Tic-Tac-Toe game with arbitrary size of board and size of streak"""


import sys
import logging
from player import Player
from game import Game


player1 = Player(name="Default1", sign="X")
player2 = Player(name="Default2", sign="O")

def custom_players():
    name1 = input("Enter name for player1: ")
    name2 = input("Enter name for player2: ")

    global player1 
    global player2 
    player1 = Player(name1, sign="X")
    player2 = Player(name2, sign="O")
    print("Names changed \n")
    main()

def new_game():
    size, streak_size = [int(x) for x in input("Enter the size of the board and streak size like '5 3': ").split()]
    game = Game(size=size, streak_size=streak_size)
    while True:
        if game.game_over:
            break
        player1.make_move(game)

        if game.game_over:
            break
        player2.make_move(game)

def check_logs():
    with open('tic-tac-toe.log', 'r') as f:
        logs = f.read()
        if logs == '':
            print("The file is empty")
        else:
            print(logs)

def delete_logs():
    with open('tic-tac-toe.log', 'w') as f:
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
    if num == 1: new_game()
    elif num == 2: custom_players()
    elif num == 3: check_logs()
    elif num == 4: delete_logs()
    elif num == 5: sys.exit()
    else: print("Wrong number!")


if __name__ == '__main__':
    main()
