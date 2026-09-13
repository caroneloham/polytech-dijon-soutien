import random

COULEURS = ["R", "V", "B", "J", "M", "N"]
TAILLE_CODE = 4
MAX_TENTATIVES = 12


def generer_code():
    code = []
    for i in range(TAILLE_CODE):
        code.append(random.choice(COULEURS))
    return code
