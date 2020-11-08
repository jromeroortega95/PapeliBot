import numpy as np

class PapeliGame():

    def __init__(self, name):
        self._name = name
        self._players = list()
        self._teams = list()
        self._words = list()
        self._curent_player = None
        self._current_round = 0
    
    def add_player(self, player_name, team_name = None) :
        self._players.append((player_name, team_name))

    def start_game(self) : pass

    def add_word(self, word) :
        self._words.append((word, None, None, None))

    def accept_current_word(self, team) : pass

    def current_player(self) : pass

    def next_player(self) : pass

if __name__ == "__main__":
    game = PapeliGame('jueguito')
    game.add_player('jm')
    game.add_player('ja')
    game.add_word('oo')