import random
from dogs_exercise import Dog  # Importation de la classe Dog du fichier précédent

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False  # Par défaut, le chien n'est pas dressé
    
    def train(self):
        print(self.bark())  # Affiche l'aboiement du chien
        self.trained = True  # Change l'état du chien en dressé
    
    def play(self, *args):
        dog_names = ", ".join(args)
        print(f"{dog_names} all play together")
    
    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")

# Exemple d'utilisation
dog1 = PetDog("Rex", 5, 20)
dog2 = PetDog("Buddy", 3, 25)
dog3 = PetDog("Charlie", 4, 30)

dog1.train()
dog1.play(dog2.name, dog3.name)
dog1.do_a_trick()
