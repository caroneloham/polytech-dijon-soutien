# TP7 - Mastermind

Jeu de Mastermind en Python : trouver une combinaison de 4 couleurs en 12 essais maximum.

## Version console

La version console est terminée dans `main.py` : partie classique, score, sauvegarde des statistiques et duel contre l'ordinateur.

Pour jouer :

```bash
python main.py
```

## Version graphique en cours

`mastermind_graphique.py` contient le début de l'interface Pygame : création de la fenêtre, couleurs, fonctions pour afficher du texte et dessiner les pions, puis initialisation des variables de la partie.

Le fichier s'arrête à `termine = False`. Cette version n'est pas encore jouable : il reste la boucle du jeu, la gestion du clavier, l'affichage des essais et la possibilité de rejouer.

Les fonctions du jeu sont réutilisées avec `import main`.
