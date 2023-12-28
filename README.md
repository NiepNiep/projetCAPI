# projetCAPI
Documentation is in the other githbranch named "gh-page"

# Fonctionnement du projet
- run le code
- cliquer sur le bouton "start" de la fenetre pygame
- participer au jeu dans la console python
- Saisir le nombre de joueur puis leurs noms
- Saisir le nombre de tâches puis leurs intitulés
- Choisir entre les modes de jeu "strict" et "average"
- Pour chaque tâches listés un système de votes par cartes est mis en place
- Les joueurs saisissent tour à tour la carte qu'ils souhaitent pour chaque tâches, par soucis de respect du jeu veuillez saisir des cartes présentes dans la liste suivante {"0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "cafe", "??"}
- Une carte finale est attribué à la tâche en fonction des votes des joueurs et du mode de jeu utilisé
- Un fichier json "player_choices.json" résumant la partie de planning poker est créé
- Fermer la fenêtre pygame ou arreter le code pour mettre fin au jeu
- Le fichier json "player_choices.json" sera remplacé après une nouvelle partie

  # Mode de jeu
  Strict : La valeur d'une tâche est validé à l'unanimité, si les joueurs ne sont pas tous d'accord sur la carte séléctionné lors du vote d'une tâche alors ils doivent revoter jusqu'à l'unanimité
  Moyenne : La valeur d'une tâche est la moyenne des cartes séléctionné par les joueurs pour cette tâche, si la valeur de la moyenne n'est pas présente dans la liste des cartes alors on séléctionne la carte la plus proche de cette valeur.
