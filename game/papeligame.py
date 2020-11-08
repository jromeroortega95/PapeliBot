import numpy as np
import random
import team

class PapeliGame():

    def __init__(self, name):
        self._name = name
        self._players = np.empty(shape=(0,2), dtype=str)
        self._teams = list()
        self._words = np.empty(shape=(0,4), dtype=str)
        self._curent_player = None
        self._current_round = 1
    
    def add_player(self, player_name, team_name = None) :
        self._players = np.append(self._players, [(player_name, team_name)], axis=0)

    def start_game(self) :
        self._check_valid_num_players()
        self._create_teams()
        self._current_round = 1
        self._current_word = random.choice(self._words[self._word])
        self._teams = self.create_teams()
        pass


    def _check_valid_num_players(self):
        num_players = len(self._players)
        if(num_players < 4):
            raise Exception('No hay suficientes jugadores, necesitamos al menos 4 jugadores')
        if(num_players%2 != 0):
            raise Exception('Numero de jugadores invalido, el numero de jugadores debe ser impar')
        unique_teams = set(self._players[:,1])
        min_players = 2*len(unique_teams)
        if(min_players > len(self._players)):
            raise Exception('No hay suficientes jugadores, necesitamos al menos %d jugadores'.format(min_players))


    def _create_teams(self):
        min_teams = len(self._players)//2
        unique_teams = list(set(self._players[self))
        teams_names = unique_teams.append(range(min_teams - len(unique_teams)))
        pass
        
        
    def add_word(self, word) :
        self._words = np.append(self._words, [(word, None, None, None)], axis=0)

    def next_word(self, word) :
        word_not_guessed = self._words[self._words[:, self._current_round] != None]
        self._current_word = random.choice(word_not_guessed)
        return self._current_word

    def accept_current_word(self, team) :
        self._current_word[self._current_round] = team
        print(self._current_word)
        print(self._words)

    def current_player(self) : pass

    def next_player(self) : pass

if __name__ == "__main__":
    game = PapeliGame('jueguito')
    game.add_word('dildo')
    game.add_word('yooo')
    game.add_player('Jose', 'TeamJose')
    game.add_player('Manolo', 'TeamJose')
    game.add_player('Paco')
    game.add_player('Antonio')
    game.start_game()
    game.accept_current_word('team')