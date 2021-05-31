import re


class LogsReader:
    def __init__(self):
        self._games = []

    def read(self):
        try:
            with open("./tic-tac-toe.log", "r") as logs:
                for log in logs:
                    self._games.append(re.findall('name=(.+?),', log))
        except FileNotFoundError:
            print("Logs have not been created")

    def get_count(self, player1, player2):
        """Return count for player1, player2"""
        p1_count = sum(True for x in self._games if player1 == x[0] and player2 == x[1])
        p2_count = sum(True for x in self._games if player2 == x[0] and player1 == x[1])
        return [p1_count, p2_count]

    @property
    def games(self):
        """Return list of games where first player is winner"""
        return self._games

if __name__ == "__main__":
    lr = LogsReader()
    lr.read()
    print(lr.games)
    print(lr.get_count("Sam", "Nick"))
    print(lr.get_count("Nick", "Sam"))