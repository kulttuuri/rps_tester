from dataclasses import dataclass
import os
import random, string, time
from .enums import EventEnum, OptionEnum
from dataclasses import dataclass, field
from .gameround import GameRound

@dataclass
class Game:
    sessionId : str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    player1 : "Player" = None
    player2 : "Player" = None
    current_event : EventEnum = EventEnum.NO_EVENT
    player1_wins : int = 0
    player2_wins : int = 0
    ties : int = 0
    rounds_played : int = 0
    round: GameRound = field(default_factory=lambda: GameRound())

    def set_player1(self, player : "Player"):
        self.player1 = player

    def set_player2(self, player : "Player"):
        self.player2 = player

    def set_player1_win(self):
        self.player1_wins = self.player1_wins + 1
        self.round.player1_win = True
        self.round.winning_option = self.player1.current_option
        self.round.losing_option = self.player2.current_option

    def set_player2_win(self):
        self.player2_wins = self.player2_wins + 1
        self.round.player2_win = True
        self.round.winning_option = self.player2.current_option
        self.round.losing_option = self.player1.current_option

    def set_tie(self):
        self.ties = self.ties + 1
        self.round.tie = True
        self.round.winning_option = OptionEnum.NO_OPTION
        self.round.losing_option = OptionEnum.NO_OPTION
    
    def reset_round(self):
        self.round = GameRound()
    
    def get_player_options_from_server(self):
        self.player1.get_new_option(self)
        self.player2.get_new_option(self)
    
    def get_winning_option(self) -> OptionEnum:
        if self.round.tie == True:
            return OptionEnum.NO_OPTION

        if self.round.player1_win == True:
            return self.player1.current_option
        else:
            return self.player2.current_option

    def get_losing_option(self) -> OptionEnum:
        if self.round.tie == True:
            return OptionEnum.NO_OPTION

        if self.round.player1_win == False:
            return self.player1.current_option
        else:
            return self.player2.current_option

    def print_game_results(self):
        print(f"{os.linesep}#########")
        print(f"Total of {self.rounds_played} games have been played.")
        print(f"Ties: {self.ties}")
        print(f"Player 1 ({self.player1.name}) wins: {self.player1_wins}")
        print(f"Player 2 ({self.player1.name}) wins: {self.player2_wins}")