"""
@poker.py
@the application allows players to play a game of planning poker
@author LEFAURE Evan ODIN Gabin
"""
import json
import pygame
import sys

class Poker:
    """
    @class Poker
    @desc class
    @brief Class handling the planning poker game

    @param online: bool: determine if the poker is online or local
    @param tab: a tab containing all the available cards to play in the poker
    @param player_choices: List to store player choices
    @param online: Boolean determining if the poker is online or local
    @param card_values: Set containing all available cards to play in the poker
    @param card_positions: Positions of the cards on the window
    @param card_votes: Dictionary to store the votes for each card
    @param pseudo: Player pseudonym
    @param player_number: Number of players
    @param task_number: Number of tasks
    @param tasks: List containing the tasks
    @param mode: Game mode
    @param game_start: Boolean indicating whether the game has started or not
    @param WHITE: RGB color value
    @param GRAY: RGB color value
    @param BLACK: RGB color value
    """
    player_choices = []
    online = False
    card_values = {"0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "cafe", "??"}
    card_positions = [(50 + i * 110, 500 // 2 - 600 // 2) for i in range(len(card_values))]
    card_votes = {card: 0 for card in card_values}
    pseudo =""
    player_number = 0
    task_number = 0
    tasks = []
    mode = 0
    game_start = False
    #colors
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    BLACK = (0, 0, 0)
    def display_text(self, texte, font, surface, x, y):
        texte_surface = font.render(texte, True, [0,0,0])
        texte_rect = texte_surface.get_rect()
        texte_rect.topleft = (x, y)
        surface.blit(texte_surface, texte_rect)

    def draw_cards(self):
        """
        @brief Method to draw the cards on the window
        """
        for i, value in enumerate(game.card_values):
            card_rect = pygame.Rect(game.card_positions[i], (100, 50))
            pygame.draw.rect(window, (200,200,200), card_rect)
            text = font.render(str(value), True, game.BLACK)
            text_rect = text.get_rect(center=card_rect.center)
            window.blit(text, text_rect)

    def find_winning_card(self):
        """
        @brief Method to find the card with the most votes
        @return The card with the most votes
        """
        winning_card = max(self.card_votes, key=self.card_votes.get)
        return winning_card

    def json_save(self):
        """
        @brief Method to save player choices in a JSON file
        """
        with open('player_choices.json', 'w') as json_file:
            json.dump(self.player_choices, json_file)

    def init(self):
        """
        @brief Method to initialize the game
        """
        clock = pygame.time.Clock()
        self.game_start = True
        window.fill((50, 50, 50))

        # Draw text input area
        input_rect = pygame.Rect(100, 0, 140, 32)
        pygame.draw.rect(window, [255, 255, 255], input_rect, 2)

        game.player_number = int(input("Enter the number of players: "))
        game.task_number = int(input("Enter the number of tasks: "))
        for _ in range(game.task_number):
            game.tasks += [input("Enter the task: ")]

        # Display "Enter Players" text in the text input area
        font_input = pygame.font.Font(None, 24)
        text_surface = font_input.render("Players count: " +  str(game.player_number), True, [255, 255, 255])
        window.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        count = 0
        for i in range(game.task_number):
            count += 1
            print("Task", game.tasks[i], "")
            for _ in range(game.player_number):
                choice = input("Choose a card: ")
                game.card_votes[choice] += 1
            game.player_choices += game.task[i] + game.find_winning_card()

        self.json_save()

pygame.init()
game = Poker()

window = pygame.display.set_mode((400, 300))
font = pygame.font.Font(None, 36)
button_rect = pygame.Rect(150, 150, 100, 50)
mouse = pygame.mouse.get_pos()
window.fill([50, 50, 50])

while True:
    mouse = pygame.mouse.get_pos()  # Update mouse position inside the loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(mouse) and not game.game_start:
                game.init()

    if not game.game_start:
        pygame.draw.rect(window, [255, 0, 0], button_rect)
        game.display_text("Start", font, window, 160, 160)

    pygame.display.update()