# projetCAPI
Documentation is in the other githbranch named "gh-page"

# Project Workflow:

. Run the code.
. Click on the "start" button in the Pygame window.
. Engage in the game through the Python console.
. Enter the number of players and their names.
. Input the number of tasks and their titles.
. Choose between the game modes "strict" and "average."
. For each listed task, a voting system using cards is implemented.
. Players input, one by one, the card they prefer for each task. For game integrity, kindly use cards from the following list: {"0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "coffee", "??"}.
. A final card is assigned to the task based on players' votes and the selected game mode.
. A JSON file named "player_choices.json," summarizing the planning poker session, is generated.
. Close the Pygame window or stop the code to conclude the game.
. The "player_choices.json" file will be replaced after a new game session.

# Game Modes:
. Strict: Task value requires unanimous agreement. If players disagree on the selected card for a task, they must revote until unanimous agreement is reached.
. Average: Task value is the average of the cards selected by players for that task. If the average value isn't present in the card list, the nearest card value is chosen.
