"""
@poker.py
@the application allows players to play a game of planning poker
"""
import json
import pygame
import sys

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

    # Display the text on button
    def display_text(self, texte, font, surface, x, y):
        texte_surface = font.render(texte, True, [0,0,0])
        texte_rect = texte_surface.get_rect()
        texte_rect.topleft = (x, y)
        surface.blit(texte_surface, texte_rect)

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

pygame.init()
game = Poker()

mouse = pygame.mouse.get_pos()
bouton = pygame.Rect(150,150,100,50)
pygame.draw.rect(pygame.display.set_mode((400, 300)), [255, 255, 0], bouton)
font = pygame.font.Font(None, 36)
window = pygame.display.set_mode((400, 300))
while True:
    window.fill([0, 0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 <= mouse[0] <= 250 and 150 <= mouse[1] <= 200:
                game.init()
        mouse = pygame.mouse.get_pos()

        # Coordonnées et taille du bouton
        bouton = pygame.Rect(150, 150, 100, 50)

        # Dessiner le bouton
        pygame.draw.rect(window, [255, 0, 0], bouton)

        # Afficher le texte du bouton
        font = pygame.font.Font(None, 36)
        game.display_text("Lancer", font, window, 160, 160)

        pygame.display.update()