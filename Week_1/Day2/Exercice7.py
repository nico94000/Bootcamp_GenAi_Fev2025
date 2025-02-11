import random

def get_random_temp(saison):
    if saison == "hiver":
        return round(random.uniform(-10, 16), 1)
    elif saison == "printemps":
        return round(random.uniform(5, 22), 1)
    elif saison == "été":
        return round(random.uniform(15, 40), 1)
    elif saison == "automne":
        return round(random.uniform(5, 25), 1)
    else:
        print("Saison invalide. Utilisation de l'été par défaut.")
        return round(random.uniform(15, 40), 1)

def main():
    mois = int(input("Entrez un numéro de mois (1 = janvier, 12 = décembre) : "))

    if mois in [12, 1, 2]:
        saison = "hiver"
    elif mois in [3, 4, 5]:
        saison = "printemps"
    elif mois in [6, 7, 8]:
        saison = "été"
    elif mois in [9, 10, 11]:
        saison = "automne"
    else:
        print("Mois invalide. Utilisation de l'été par défaut.")
        saison = "été"

    temperature = get_random_temp(saison)
    
    print(f"\nLa température actuelle est de {temperature}°C ({saison}).")

    if temperature < 0:
        print("❄️ Brrr, c'est glacial ! Portez quelques couches supplémentaires aujourd'hui.")
    elif 0 <= temperature < 16:
        print("🧥 Assez froid ! N'oubliez pas votre manteau.")
    elif 16 <= temperature < 23:
        print("🌤️ Température agréable. Profitez de la journée !")
    elif 23 <= temperature < 32:
        print("☀️ Il fait chaud, pensez à vous hydrater.")
    else:
        print("🔥 Il fait très chaud ! Restez à l'ombre et buvez beaucoup d'eau.")

main()
