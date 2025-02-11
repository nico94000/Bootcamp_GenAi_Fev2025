# family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
# total_cost = 0
# for name, age in family.items():
#     if age < 3:
#         price = 0
#     elif 3 <= age <= 12:
#         price = 10
#     else:
#         price = 15
#     print(f"{name} doit payer {price} $")
#     total_cost += price
#     print(f"Coût total pour la famille : {total_cost} $") 
   
# # Initialiser un dictionnaire vide pour stocker les membres de la famille
# family = {}

# # Demander le nombre de membres de la famille
# while True:
#     try:
#         nb_members = int(input("Combien de membres dans la famille ? "))
#         break  # Sortir de la boucle si l'entrée est correcte
#     except ValueError:
#         print("Erreur : veuillez entrer un nombre entier valide.")

# # Remplir le dictionnaire avec les noms et âges
# for _ in range(nb_members):
#     name = input("Entrez le nom : ")
#     while True:  # Boucle pour s'assurer que l'âge est un nombre valide
#         try:
#             age = int(input(f"Entrez l'âge de {name} : "))
#             break
#         except ValueError:
#             print("Erreur : veuillez entrer un âge valide.")
    
#     family[name] = age  # Ajouter le membre au dictionnaire

# # Initialiser le coût total
# total_cost = 0

# # Calculer combien chaque membre doit payer
# for name, age in family.items():
#     if age < 3:
#         price = 0
#     elif 3 <= age <= 12:
#         price = 10
#     else:
#         price = 15
    
#     print(f"{name} doit payer {price} $")
#     total_cost += price  # Ajouter au total

# # Afficher le coût total de la famille
# print(f"Coût total pour la famille : {total_cost} $")
# #exercice 2

def describe_city(city, country="France"):
    print(f"{city} is in {country}.")

# Appel de la fonction avec différentes villes
describe_city("Paris")
describe_city("Reykjavik", "Iceland")
describe_city("New York", "USA")

