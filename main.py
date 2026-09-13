import random

COULEURS = ["R", "V", "B", "J", "M", "N"]
TAILLE_CODE = 4
MAX_TENTATIVES = 12


def generer_code():
    code = []
    for i in range(TAILLE_CODE):
        code.append(random.choice(COULEURS))
    return code


def saisir_code(message):
    while True:
        texte = input(message).strip().upper()
        if len(texte) != TAILLE_CODE:
            print("Il faut", TAILLE_CODE, "lettres.")
            continue
        valide = True
        for lettre in texte:
            if lettre not in COULEURS:
                valide = False
        if valide:
            return list(texte)
        print("Couleur invalide.")


def verifier_code(code_secret, proposition):
    secret = code_secret.copy()
    essai = proposition.copy()
    correct = 0
    partiel = 0

    for i in range(TAILLE_CODE):
        if essai[i] == secret[i]:
            correct += 1
            secret[i] = None
            essai[i] = None

    for i in range(TAILLE_CODE):
        if essai[i] is not None and essai[i] in secret:
            partiel += 1
            secret.remove(essai[i])

    return correct, partiel
