# ---
# Here you can define the addresses of two servers that will fight each another
# Both servers can also even point to a same address of course to test out your server
# You could also run two servers in two different ports on your own computer with command below:
# (First server file named as server.py): uvicorn server:app --port 8000
# (Second server file named as server2.py): uvicorn server2:app --port 8001
user_settings = {
    "player1": {
        "name": "Server 1", # Name of server 1
        "server": "http://localhost:8000", # Address of server 1, for example: http://localhost:8000
    },
    "player2": {
        "name": "Server 2", # Name of server 2
        "server": "http://localhost:8001", # Address of server 2, for example: http://localhost:8000
    },
    "game_amount": 20, # How many games to play, for ex: 50
    "halftime_rounds": 5, # How many games to play after each half-time, for ex. 5
    "announce_halftime" : True, # If set to True, will wait the determined amount every half-time rounds. Otherwise, when False, runs all games through
    "halftime_sleep": 0 # How many seconds to wait after each half-time, for ex. 3 or 1.5
}