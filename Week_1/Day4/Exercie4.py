class Family:
    def __init__(self, nom_de_nom, membres):
        self.nom_de_nom = nom_de_nom
        self.membres = membres
    
    def born(self, **kwargs):
        self.membres.append(kwargs)
        print(f"Félicitations à la famille {self.nom_de_nom} pour la naissance de {kwargs['name']}!")
    
    def is_18(self, name):
        for membre in self.membres:
            if membre['name'] == name:
                return membre['age'] >= 18
        return False
    
    def family_presentation(self):
        print(f"Famille {self.nom_de_nom}:")
        for membre in self.membres:
            print(f"Nom: {membre['name']}, Âge: {membre['age']}, Sexe: {membre['gender']}, Enfant: {membre['is_child']}")

# Création d'une instance de la classe Family
famille_smith = Family("Smith", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

# Ajout d'un enfant
famille_smith.born(name="Emma", age=0, gender="Female", is_child=True)

# Vérification si un membre a plus de 18 ans
print(f"Michael a plus de 18 ans ? {famille_smith.is_18('Michael')}")
print(f"Emma a plus de 18 ans ? {famille_smith.is_18('Emma')}")

# Présentation de la famille
famille_smith.family_presentation()
