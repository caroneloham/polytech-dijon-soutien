# TP7 - Mastermind

Jeu de Mastermind réalisé en Python.

![Plateau de jeu Mastermind](img/mastermind.jpg)

## Règles

Trouver un code de 4 couleurs en 12 essais maximum.
Une couleur peut apparaître plusieurs fois.

Couleurs disponibles : R, V, B, J, M, N.

Après chaque essai :

- Correct : bonne couleur à la bonne place.
- Partiel : bonne couleur à la mauvaise place.

## Jouer

Lancer la version console :

```bash
python main.py
```

Le menu permet de jouer, consulter ses statistiques, les remettre à zéro et faire un duel contre l'ordinateur.

## Fichiers

- `main.py` : jeu console et fonctions du Mastermind.
- `mastermind_graphique.py` : début de la version graphique avec Pygame, pas encore jouable.

## Historique des commits

```mermaid
flowchart TD
    C1["1. debut du mastermind"]
    C2["2. ajout de la carte des commits"]
    C1 --> C2
    C3["3. mise a jour du lien du depot tp7"]
    C2 --> C3
    C4["4. remplacement de la carte par mermaid"]
    C3 --> C4
    C5["5. ajout de la saisi et verification des couleurs"]
    C4 --> C5
    C6["6. ajout de la partie et du score"]
    C5 --> C6
    C7["7. ajout des stats et du menu pour rejouer"]
    C6 --> C7
    C8["8. preparation des combinaisons avec des boucles"]
    C7 --> C8
    C9["9. ajout du mode inverse et du duel"]
    C8 --> C9
    C10["10. debut de la version graphique et mise a jour du readme"]
    C9 --> C10
    C11["11. mise a jour du readme et historique en mermaid"]
    C10 --> C11
```
