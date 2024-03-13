from dataclasses import dataclass
import requests
import os
from .enums import AddressEnum, OptionEnum
from .game import Game

@dataclass
class Player:
    number : int
    name : str
    address : str
    current_option : OptionEnum = OptionEnum.NO_OPTION

    def endpoint_get_option(self):
        return self.address + AddressEnum.GET_OPTION.value
    
    def endpoint_post_result(self):
        return self.address + AddressEnum.POST_RESULT.value
    
    def get_new_option(self, game : Game):
        try:
            server_option = requests.get(f"{self.endpoint_get_option()}?sessionId={game.sessionId}").json()["option"]
            self.current_option = OptionEnum[OptionEnum.get_key_by_value(server_option)]
        except Exception as e:
            print(f"{os.linesep}Error getting option result for player {self.number}: {e}")
            self.current_option = OptionEnum.NO_OPTION
        return self.current_option
    
    def post_result(self, game : Game, youWin : bool, youLose : bool, tie : bool):
        return requests.post(f'''{self.endpoint_post_result()}?sessionId={game.sessionId}&youWin={youWin}&youLose={youLose}&tie={tie}&winningOption={game.round.winning_option.value}&losingOption={game.round.losing_option.value}''').json()