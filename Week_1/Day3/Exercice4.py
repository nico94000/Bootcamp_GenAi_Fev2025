# Définition de la classe Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []  # Liste vide pour stocker les animaux

    def add_animal(self, new_animal):
        """Ajoute un animal à la liste s'il n'y est pas déjà."""
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        """Affiche tous les animaux du zoo."""
        print(f"Animals in {self.name}: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        """Supprime un animal de la liste s'il est présent."""
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        """Trie les animaux par ordre alphabétique et les regroupe par première lettre."""
        sorted_animals = sorted(self.animals)  # Trie les animaux
        grouped_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0]  # Première lettre de l'animal
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [animal]
            else:
                grouped_animals[first_letter].append(animal)

        return grouped_animals  # Retourne les groupes d'animaux

    def get_groups(self):
        """Affiche les groupes d'animaux triés."""
        groups = self.sort_animals()
        print("Animal groups in the zoo:")
        for key, value in groups.items():
            print(f"{key}: {value}")

# Création de l'objet ramat_gan_safari
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Ajout d'animaux
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")

# Affichage des animaux du zoo
ramat_gan_safari.get_animals()

# Vente d'un animal
ramat_gan_safari.sell_animal("Bear")

# Affichage après la vente
ramat_gan_safari.get_animals()

# Affichage des groupes triés
ramat_gan_safari.get_groups()
