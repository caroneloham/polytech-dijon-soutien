import pygame
import main

pygame.init()
fenetre = pygame.display.set_mode((660, 740))
pygame.display.set_caption("Mastermind graphique")
police = pygame.font.SysFont("arial", 22)
horloge = pygame.time.Clock()

couleurs = {
    "R": "red",
    "V": "green",
    "B": "blue",
    "J": "yellow",
    "M": "magenta",
    "N": "black"
}


def texte(message, x, y):
    image = police.render(message, True, "black")
    fenetre.blit(image, (x, y))


def dessiner_code(code, y):
    for i in range(main.TAILLE_CODE):
        couleur = "white"
        if i < len(code):
            couleur = couleurs[code[i]]
        centre = (65 + i * 55, y)
        pygame.draw.circle(fenetre, couleur, centre, 16)
        pygame.draw.circle(fenetre, "black", centre, 16, 1)


secret = main.generer_code()
proposition = []
essais = []
resultats = []
message = "Entrez votre combinaison."
termine = False
