# Tester for Rock-Paper-Scissors Server

This app is being used to test the RPS (rock-paper-scissors) competition server. The competition is being held at SAMK in a course "Server-Side Programming".

## Requirements

- Python 3.x
- requests pip package

## Running the Server

First, set your server settings in the `settings.py` file.

Then, run the script `run` located in the main folder. You might need to set run permissions to the file first by running the command `chmod +x run`.

## Implementing your own Server

Your own web server should have these REST endpoints set:

### /api/get_option

#### Method
GET

#### Query Parameters
- sessionId (str): ID of the current game session

#### Example Call
http://localhost:8000/api/get_option?sessionId=asd

#### Description

The test script will call this endpoint and pass the ID of the current game session to it.

Your endpoint should output this type of JSON back:

```json
{
    "option": "rock"
}
```

The option should be either `"rock"`, `"paper"`, or `"scissors"`.

### /api/post_result

#### Method
POST

#### Query Parameters
- sessionId (str): ID of the current game session
- youWin (bool): True if you won the round, False otherwise
- youLose (bool): True if you lost the round, False otherwise
- tie (bool): True if the game was a tie, False otherwise
- winningOption (str): "rock", "paper", "scissors" or "" if tie
- losingOption (str): "rock", "paper", "scissors" or "" if tie

#### Example Call
http://localhost:8000/api/post_result?sessionId=asd&youWin=True&youLose=False&tie=False&winningOption=paper&losingOption=rock

#### Description

The test script will call this endpoint whenever the result of the game has been determined. You can then determine if there was a tie, or if you won or lost and the winning and losing option.

The endpoint should just output this information back:

```json
{
    "acknowledged": True
}
```