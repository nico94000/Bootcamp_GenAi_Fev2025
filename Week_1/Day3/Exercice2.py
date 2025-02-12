# Définition de la classe Dog
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Création de l'objet davids_dog
davids_dog = Dog("Rex", 50)

# Affichage des détails du chien de David et appel des méthodes
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

# Création de l'objet sarahs_dog
sarahs_dog = Dog("Teacup", 20)

# Affichage des détails du chien de Sarah et appel des méthodes
print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Comparaison des tailles des chiens et affichage du plus grand
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print(f"The bigger dog is {sarahs_dog.name}.")
