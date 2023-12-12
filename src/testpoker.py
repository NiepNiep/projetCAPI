"""
@poker.py
@the application allows players to play a game of planning poker
"""


class Poker:
    """
    @class Poker
    @desc class

    @param online: bool: determin if the poker is online or local
    @param tab: a tab containing all the available cards to play in the poker
    """
    online = False
    tab = {"0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "cafe", "??"}
    pseudo =""
    mode = 0
    cpt = "0"

    def init():
        nbjoueur = input("enter the number of players")
        print(nbjoueur)

        for x in range(nbjoueur):
            cpt = cpt + 1
            print("joueur", cpt, "")

    