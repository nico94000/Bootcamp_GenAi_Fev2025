# Définition de la classe Farm
class Farm:
    def __init__(self, farm_name):
        """Initialisation avec le nom de la ferme et un dictionnaire d'animaux."""
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal, count=1):
        """Ajoute un animal à la ferme, ou incrémente son nombre si déjà présent."""
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        """Retourne une description formatée des animaux de la ferme."""
        result = f"{self.name}'s farm\n"
        for animal, count in sorted(self.animals.items()):
            result += f"{animal} : {count}\n"
        result += "\nE-I-E-I-0!"
        return result

    def get_animal_types(self):
        """Retourne une liste triée des types d'animaux présents à la ferme."""
        return sorted(self.animals.keys())

    def get_short_info(self):
        """Retourne une phrase décrivant les animaux de la ferme avec des pluriels adaptés."""
        animals_list = [f"{animal}s" if self.animals[animal] > 1 else animal for animal in self.get_animal_types()]
        return f"{self.name}'s farm has {', '.join(animals_list[:-1])} and {animals_list[-1]}."

# Création de la ferme de MacDonald
macdonald = Farm("McDonald")

# Ajout d'animaux
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Affichage des informations sur la ferme
print(macdonald.get_info())

# Vérification des types d'animaux
print(macdonald.get_animal_types())

# Affichage de l'info courte
print(macdonald.get_short_info())
