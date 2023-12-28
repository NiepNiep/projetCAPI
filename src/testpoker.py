"""
@poker.py
@the application allows players to play a game of planning poker
@author LEFAURE Evan ODIN Gabin
"""
import json
import pygame
import sys


class PokerModel:
    """
    @class PokerModel
    @brief Class representing the model of the application, containing the game logic.
    """
    def __init__(self):
        """
        @brief Constructor method initializing the PokerModel class.
        Attributes:
            player_choices (list): Records the choices made by players for each task.
            player_names (list): Stores the names of the players participating in the game.
            card_values (set): Set containing the available card values to play with.
            card_votes (dict): Keeps track of the votes each card receives during the game.
            player_number (int): Number of players participating in the game.
            task_number (int): Number of tasks planned for the game.
            tasks (list): Contains the descriptions of each task.
            mode (str): Indicates the selected mode of the game (e.g., 'strict', 'average').
            game_start (bool): Tracks whether the game has started or not.
        """
        self.player_choices = []
        self.player_names = []
        self.card_values = {"0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "cafe", "??"}
        self.card_votes = {card: 0 for card in self.card_values}
        self.player_number = 0
        self.task_number = 0
        self.tasks = []
        self.mode = ""
        self.game_start = False

    def play_strict_mode(self):
        """
        @brief Initiates the game in strict mode, prompting players to choose cards for each task until unanimity is reached,
        recording the winning card for each task, and then finding the card with the most votes
        @return: None
        """
        for task in self.tasks:
            unanimous = False
            while not unanimous:
                choices = {}  # Utiliser un dictionnaire pour stocker les choix de chaque joueur pour cette tâche
                for player, name in enumerate(self.player_names, 1):  # Parcourir les joueurs avec leurs noms
                    choice = input("{} - Choose a card for task {}: ".format(name, task))
                    if choice in self.card_values:
                        choices[player] = choice
                    else:
                        print("Invalid card choice. Please choose from available cards.")
                        break
                else:
                    # Si tous les joueurs ont voté sans choix invalide, vérifiez l'unanimité
                    if len(set(choices.values())) == 1:
                        unanimous = True
                        winning_card = list(choices.values())[0]
                        print("Task {} - Winning Card: {}".format(task, winning_card))
                        self.card_votes[winning_card] += 1
                        self.player_choices.append(
                            (task, winning_card))  # Ajouter le choix gagnant pour cette tâche
                    else:
                        print("Not unanimous. Please vote again.")

        winning_card = self.find_winning_card()
        print("Winning Card: {}".format(winning_card))
        self.card_votes = {card: 0 for card in self.card_values}

    def play_average_mode(self):
        """
        @brief Initiates the game in average mode, allowing players to choose cards for each task, calculating the average choice,
        finding the nearest card value from the available set, and recording the choices for each task.
        @param: None
        @return: None
        """
        for task in self.tasks:
            choices = {}  # Utiliser un dictionnaire pour stocker les choix de chaque joueur pour cette tâche
            for player, name in enumerate(self.player_names, 1):  # Parcourir les joueurs avec leurs noms
                choice = int(input("{} - Choose a card for task {}: ".format(name, task)))
                choices[player] = choice

            # Calcul de la moyenne des choix des joueurs pour cette tâche
            average_choice = sum(choices.values()) / len(choices)

            # Convertir la moyenne en entier
            average_choice = int(average_choice)

            # Vérifier si la moyenne calculée est dans la liste card_values
            if str(average_choice) not in self.card_values:
                # Trouver la valeur la plus proche dans card_values
                closest_value = min(self.card_values, key=lambda x: abs(float(x) - average_choice))
                average_choice = int(closest_value)

            print("Task {} - Average Choice: {:.2f}".format(task, average_choice))
            self.player_choices.append((task, str(average_choice)))

            # Mise à jour des votes de la carte basée sur la moyenne des choix des joueurs pour cette tâche
            self.card_votes[str(average_choice)] += 1

        winning_card = self.find_winning_card()
        print("Winning Card: {}".format(winning_card))
        self.card_votes = {card: 0 for card in self.card_values}

    def json_save(self):
        """
        @brief Saves player choices for tasks in a JSON file named 'player_choices.json'.
        @param: None
        @return: None
        """
        with open('player_choices.json', 'w') as json_file:
            json.dump(self.player_choices, json_file)

    def find_winning_card(self):
        """
        @brief Finds the card with the most votes based on player choices for tasks.
        @param: None
        @return The card with the most votes
        """
        winning_card = max(self.card_votes, key=self.card_votes.get)
        return winning_card

    def start_game(self):
        """
        @brief Starts the game by prompting the number of players, their names, the number of tasks, and the selected mode (strict or average).
        Initiates gameplay based on the chosen mode and saves the player choices.
        @param: None
        @return: None
        """
        self.player_number = int(input("Enter the number of players: "))
        for i in range(1, self.player_number + 1):
            name = input("Enter the name for Player {}: ".format(i))
            self.player_names.append(name)

        self.task_number = int(input("Enter the number of tasks: "))
        for _ in range(self.task_number):
            self.tasks.append(input("Enter the task: "))

        selected_mode = input("Select the game mode (strict/average): ")

        if selected_mode == "strict":
            self.play_strict_mode()
        elif selected_mode == "average":
            self.play_average_mode()
        else:
            print("Invalid mode selection. Please choose either 'strict' or 'average'.")

        self.json_save()

class GameDisplay:
    def __init__(self):
        """
        @brief Constructor method initializing the GameDisplay class.
        """
        pygame.init()
        self.window = pygame.display.set_mode((400, 300))
        self.font = pygame.font.Font(None, 36)
        self.start_button_rect = pygame.Rect(150, 150, 100, 50)

    def draw_start_button(self):
        """
        @brief Draw the start button on the game window
        """
        pygame.draw.rect(self.window, [255, 0, 0], self.start_button_rect)
        self.display_text("Start", self.font, self.window, 160, 160)

    def update_display(self):
        """
        @brief Update the game window
        """
        pygame.display.update()

    def display_text(self, text, font, surface, x, y):
        """
        @brief Display text on the game window
        @param text: text to display
        @param font: font of the text
        @param surface: surface on which the text is displayed
        @param x: x position of the text
        @param y: y position of the text
        @return: None
        """
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_surface, text_rect)


class GameController:
    """
    @class GameController
    @brief Class representing the controller of the application, containing the event handling logic.
    """
    def __init__(self, model, view):
        """
        @brief Constructor method initializing the GameController class.
        @param model: model of the application
        @param view: view of the application
        """
        self.model = model
        self.view = view

    def handle_events(self):
        """
        @brief Handle events in the game window
        @param: None
        @return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.start_button_rect.collidepoint(event.pos):
                    self.model.start_game()

    def start_game(self):
        """
        @brief Start the game
        @return: None
        """
        self.model.start_game()



# Code principal
if __name__ == "__main__":
    model = PokerModel()
    view = GameDisplay()
    controller = GameController(model, view)

    while not model.game_start:
        controller.handle_events()
        view.draw_start_button()
        view.update_display()

    model.start_game()

