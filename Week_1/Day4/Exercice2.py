class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Étape 1 : Création de la classe Siamese
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Étape 2 : Création de la liste all_cats avec trois instances de chats
bengal_cat = Bengal("Tiger", 2)
chartreux_cat = Chartreux("Shadow", 3)
siamese_cat = Siamese("Luna", 1)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Étape 3 : Création d'une instance de Pets avec all_cats
sara_pets = Pets(all_cats)

# Étape 4 : Emmener tous les chats en promenade
sara_pets.walk()
