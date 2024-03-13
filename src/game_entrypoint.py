import random, os, time, sys
from pathlib import Path

from .modules.enums import AddressEnum, OptionEnum, EventEnum
from .modules.game import Game
from .modules.gameround import GameRound
from .modules.player import Player

def start(user_settings : dict):
    game = Game()
    game.set_player1(Player(1, user_settings.get("player1")["name"], user_settings.get("player1")["server"]))
    game.set_player2(Player(2, user_settings.get("player2")["name"], user_settings.get("player2")["server"]))

    while game.rounds_played < user_settings["game_amount"]:
        game.rounds_played = game.rounds_played + 1

        # Get results for players 1 & 2
        game.get_player_options_from_server()

        # Figure out results for the game and store the results
        result_server1 = game.player1.current_option
        result_server2 = game.player2.current_option
        current_event = game.current_event

        # Both are empty, tie
        if (result_server1 == OptionEnum.NO_OPTION and result_server2 == OptionEnum.NO_OPTION):
            game.set_tie()
        # Result from server 1 is empty, player 2 wins
        elif (result_server1 == OptionEnum.NO_OPTION):
            game.set_player2_win()
        # Result from server 2 is empty, player 1 wins
        elif (result_server2 == OptionEnum.NO_OPTION):
            game.set_player1_win()
        # Tie
        elif (result_server1 == result_server2):
            game.set_tie()
        # Event fire strike: Player 1 with paper loses
        elif (current_event == EventEnum.FIRE_STRIKE and result_server1 == OptionEnum.PAPER):
            game.set_player2_win()
        # Event fire strike: Player 2 with paper loses
        elif (current_event == EventEnum.FIRE_STRIKE and result_server2 == OptionEnum.PAPER):
            game.set_player1_win()
        # Event cheap scissors: Player 1 with scissors loses
        elif (current_event == EventEnum.CHEAP_SCISSORS and result_server1 == OptionEnum.SCISSORS):
            game.set_player2_win()
        # Event cheap scissors: Player 2 with scissors loses
        elif (current_event == EventEnum.CHEAP_SCISSORS and result_server2 == OptionEnum.SCISSORS):
            game.set_player1_win()
        # Event kryptonite: Player 1 with rock wins
        elif (current_event == EventEnum.KRYPTONITE and result_server1 == OptionEnum.ROCK):
            game.set_player1_win()
        # Event kryptonite: Player 2 with rock wins
        elif (current_event == EventEnum.KRYPTONITE and result_server2 == OptionEnum.ROCK):
            game.set_player2_win()
        # Player 1 uses scissors to win paper
        elif (result_server1 == OptionEnum.SCISSORS and result_server2 == OptionEnum.PAPER):
            game.set_player1_win()
        # Player 2 uses scissors to win paper
        elif (result_server2 == OptionEnum.SCISSORS and result_server1 == OptionEnum.PAPER):
            game.set_player2_win()
        # Player 1 uses rock to win scissors
        elif (result_server1 == OptionEnum.ROCK and result_server2 == OptionEnum.SCISSORS):
            game.set_player1_win()
        # Player 2 uses rock to win scissors
        elif (result_server2 == OptionEnum.ROCK and result_server1 == OptionEnum.SCISSORS):
            game.set_player2_win()
        # Player 1 uses paper to win rock
        elif (result_server1 == OptionEnum.PAPER and result_server2 == OptionEnum.ROCK):
            game.set_player1_win()
        # Player 2 uses paper to win rock
        elif (result_server2 == OptionEnum.PAPER and result_server1 == OptionEnum.ROCK):
            game.set_player2_win()

        #print(result_server1, result_server2)

        try:
            game.player1.post_result(game, game.round.player1_win, game.round.player2_win, game.round.tie)
        except Exception as e:
            print(f"{os.linesep}Error posting results to player 1:")
            print(e)
        try:
            game.player2.post_result(game, game.round.player2_win, game.round.player1_win, game.round.tie)
        except Exception as e:
            print(f"{os.linesep}Error posting results to player 2:")
            print(e)
        
        # Print the results every x games and calculate if an event begins
        if game.rounds_played % user_settings.get("halftime_rounds") == 0:
            
            # Print the results if wanting to
            if game.rounds_played is not user_settings.get("game_amount") and user_settings.get("announce_halftime"):
                game.print_game_results()

            # Determine the current event
            random_val = random.randint(0, 100)
            if random_val >= 0 and random_val <= 10:
                game.current_event = EventEnum.FIRE_STRIKE
            elif random_val >= 10 and random_val <= 20:
                game.current_event = EventEnum.CHEAP_SCISSORS
            elif random_val >= 20 and random_val <= 30:
                game.current_event = EventEnum.KRYPTONITE
            else:
                game.current_event = EventEnum.NO_EVENT

            print(os.linesep + game.current_event.value)

            # Sleep if wanting to
            if game.rounds_played is not user_settings.get("game_amount") and user_settings.get("announce_halftime"):
                time.sleep(user_settings["halftime_sleep"])
        
        game.reset_round()

    # Print the results of all games
    print(os.linesep + "FINAL RESULTS OF THE GAMES:")
    game.print_game_results()