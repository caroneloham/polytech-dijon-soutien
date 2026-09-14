import random
import os
#Ne marche que sur windows du a la lib OS qui utilise les fonction du syteme windows pour gerer les fichier a la place de PATH lib je préfére)
print("ne marche que sur windows du a la lib OS qui utilise les fonction du syteme windows")
COULEURS = ["R", "V", "B", "J", "M", "N"]
TAILLE_CODE = 4
MAX_TENTATIVES = 12

chemin = os.path.abspath(__file__)
dossier = os.path.dirname(chemin)
FICHIER = os.path.join(dossier, ".statistiques")


def sauvegarder(parties, total):
    with open(FICHIER, "w", encoding="utf-8") as fichier:
        fichier.write(str(parties) + "\n")
        fichier.write(str(total) + "\n")


def charger():
    if not os.path.exists(FICHIER):
        return 0, 0
    try:
        with open(FICHIER, "r", encoding="utf-8") as fichier:
            parties = int(fichier.readline())
            total = int(fichier.readline())
        if parties >= 0:
            return parties, total
    except ValueError:
        pass
    print("Statistiques invalides, remise à zéro.")
    return 0, 0


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


def preparer_codes():
    codes = [[]]
    for position in range(TAILLE_CODE):
        nouveaux = []
        for code in codes:
            for couleur in COULEURS:
                nouveau_code = code.copy()
                nouveau_code.append(couleur)
                nouveaux.append(nouveau_code)
        codes = nouveaux
    return codes


def jouer_inverse():
    print("Couleurs :", " ".join(COULEURS))
    secret = saisir_code("Choisissez votre code secret : ")
    possibles = preparer_codes()
    restants = possibles.copy()

    for tentative in range(1, MAX_TENTATIVES + 1):
        if random.randint(1, 10) <= 8:
            proposition = random.choice(possibles)
        else:
            proposition = random.choice(restants)

        restants.remove(proposition)
        correct, partiel = verifier_code(secret, proposition)
        print("Essai", tentative, ":", "".join(proposition))
        print("Correct :", correct, "| Partiel :", partiel)

        if correct == TAILLE_CODE:
            score = MAX_TENTATIVES - tentative
            print("L'ordinateur a trouvé ! Score :", score)
            return score

        nouveaux = []
        for code in possibles:
            bien, mal = verifier_code(code, proposition)
            if bien == correct and mal == partiel:
                nouveaux.append(code)
        possibles = nouveaux

    print("L'ordinateur a perdu.")
    return 0


def afficher_stats(parties, total):
    print("Parties jouées :", parties)
    print("Score total :", total)
    print()


def menu():
    parties, total = charger()
    afficher_stats(parties, total)

    while True:
        print("1 - Jouer ou rejouer")
        print("2 - Remettre les statistiques à zéro")
        print("3 - Quitter")
        print("4 - Duel contre l'ordinateur")
        choix = input("Votre choix : ").strip()

        if choix == "3":
            return
        elif choix == "2":
            parties = 0
            total = 0
        elif choix == "1" or choix == "4":
            score = jouer()
            if choix == "4":
                score_ordinateur = jouer_inverse()
                score = score - score_ordinateur
                print("Score du duel :", score)
            parties += 1
            total += score
        else:
            print("Choix invalide.")
            continue

        sauvegarder(parties, total)
        afficher_stats(parties, total)


if __name__ == "__main__":
    menu()
