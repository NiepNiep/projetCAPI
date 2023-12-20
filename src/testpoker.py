"""
@poker.py
@the application allows players to play a game of planning poker
"""
import json

class Poker:
    """
    @class Poker
    @desc class

    @param online: bool: determin if the poker is online or local
    @param tab: a tab containing all the available cards to play in the poker
    """
    game_in_progress = {
            "tasks": [
                {
                    "name": "Task 1",
                    "estimations": {
                        "Player 1": 5,
                        "Player 2": 3,
                    }
                },
                {
                    "name": "Task 2",
                    "estimations": {
                        "Player 1": 8,
                        "Player 2": 13,
                    }
                },
            ],
        }

    online = False
    tab = {"0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "cafe", "??"}
    pseudo =""
    mode = 0

    def init(self):
        num_players = int(input("Enter the number of players: "))
        print(num_players)
        count = 0
        for _ in range(num_players):
            count += 1
            print("Task", count, "")
            for _ in range(num_players):
                choice = input("Choose a card: ")

        with open('game_planning_poker.json', 'w') as json_file:
            json.dump(self.game_in_progress, json_file)

    
game = Poker()
game.init()