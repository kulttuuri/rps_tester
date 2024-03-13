'''
This file contains all enums (enumerators) to be used in the game.
'''

from enum import Enum

class EnumBase(Enum):
    '''
    Acts as a base class for all Enums. Contains the method to get key for enum by value.
    '''
    @classmethod
    def get_key_by_value(cls, value):
        return next((member.name for member in cls if member.value == value), None)

class AddressEnum(EnumBase):
    GET_OPTION = "/api/get_option"
    POST_RESULT = "/api/post_result"

class OptionEnum(EnumBase):
    PAPER = "paper"
    SCISSORS = "scissors"
    ROCK = "rock"
    NO_OPTION = ""

class EventEnum(EnumBase):
    NO_EVENT = "No events in play."
    FIRE_STRIKE = "Event Fire Strike begins. All paper will burn and lose!"
    CHEAP_SCISSORS = "Event Cheap Scissors begins. Scissors always lose!"
    KRYPTONITE = "Event Kryptonite begins. Rock is engrawed with kryptonite and always wins!"