class TheIncredibles(Family):
    def __init__(self, nom_de_nom, membres):
        super().__init__(nom_de_nom, membres)
    
    def use_power(self, name):
        for membre in self.membres:
            if membre['name'] == name:
                if membre['age'] < 18:
                    raise Exception(f"{name} n'a pas encore 18 ans et ne peut pas utiliser son pouvoir!")
                print(f"{name} utilise son pouvoir: {membre['power']}")
                return
        print(f"{name} n'est pas dans la famille!")
    
    def incredible_presentation(self):
        print("**Voici notre puissante famille**")
        super().family_presentation()

# Création d'une instance de TheIncredibles
incredible_family = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'Mr. Fly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'Mind Reader'}
])

# Appel de la méthode incredible_presentation
incredible_family.incredible_presentation()

# Ajout de Baby Jack
incredible_family.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='Baby Jack')

# Nouvelle présentation après l'ajout de Jack
incredible_family.incredible_presentation()