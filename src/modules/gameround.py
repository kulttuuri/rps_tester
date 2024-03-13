from dataclasses import dataclass
from .enums import OptionEnum

@dataclass
class GameRound:
    player1_win : bool = False
    player2_win : bool = False
    tie : bool = False
    winning_option : OptionEnum = None
    losing_option : OptionEnum = None