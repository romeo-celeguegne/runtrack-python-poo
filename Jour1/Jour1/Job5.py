class Animal():  # Créer une classe
    # Créer une fonction qui prend en compte tout ce qu'il y a dans la class
    def __init__(self, age, prenom):
        self.age = age  # Créer deux variables age et prenom qui sont reliées à deux attributs
        self.prenom = prenom
        print("L'age de l'animal ", self.age, " ans")

    def vieillir(self):  # Créer une fonction qui va ajouter 1an à l'animal
        self.age += 1
        print("L'age de l'animal ", self.age, " ans")

    def nommer(self, prenom):  # Créer une fonction qui va donner un nom à l'animal
        self.prenom = prenom
        print("L'animal se nomme", self.prenom)


prenom_age = Animal(0, "prenom")
prenom_age.vieillir()
prenom_age.nommer("Luna")
