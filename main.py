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


def jouer():
    secret = generer_code()
    print("Couleurs :", " ".join(COULEURS))

    for tentative in range(1, MAX_TENTATIVES + 1):
        proposition = saisir_code("Votre combinaison : ")
        correct, partiel = verifier_code(secret, proposition)
        print("Correct :", correct, "| Partiel :", partiel)
        print("Tentative :", tentative, "/", MAX_TENTATIVES)

        if correct == TAILLE_CODE:
            score = MAX_TENTATIVES - tentative
            print("Bravo ! Score :", score)
            return score

    print("Perdu ! Le code était :", "".join(secret))
    return 0


if __name__ == "__main__":
    jouer()
