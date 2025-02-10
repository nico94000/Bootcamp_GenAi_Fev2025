import random

def number_guessing_game():
    # 1) Générer un nombre aléatoire entre 1 et 100
    random_number = random.randint(1, 100)

    # 2) Définir le nombre maximum de tentatives
    max_attempts = 7

    # 3) Afficher des informations pour l'utilisateur
    print("Bienvenue dans le Jeu de Devinettes de Nombres !")
    print("Je viens de penser à un nombre entre 1 et 100.")
    print(f"Vous avez {max_attempts} tentatives pour le trouver.\n")

    # 4) Utiliser une boucle for pour gérer chaque tentative
    for attempt in range(1, max_attempts + 1):
        # 5) Demander la saisie de l’utilisateur
        guess_str = input(f"Tentative {attempt} - Entrez votre nombre : ")

        # 6) Convertir en entier + gérer les erreurs
        try:
            guess = int(guess_str)
        except ValueError:
            print("Vous devez saisir un ENTIER. Réessayez.\n")
            continue  # on repart à la tentative suivante

        # 7) Comparer la supposition au nombre aléatoire
        if guess < random_number:
            print("Too low!\n")
        elif guess > random_number:
            print("Too high!\n")
        else:
            # Si c'est juste, on félicite l'utilisateur et on arrête le jeu
            print(f"Bravo ! Vous avez trouvé le nombre {random_number} "
                  f"en {attempt} tentatives.")
            break
    else:
        # 8) Si on sort de la boucle sans break, c’est qu’on n’a pas trouvé
        print(f"Dommage ! Le nombre correct était {random_number}.")

# Optionnel : on peut exécuter la fonction si on lance ce script directement
if __name__ == "__main__":
    number_guessing_game()
