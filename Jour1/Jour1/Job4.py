class Personne():  # Créer une classe
    # Créer une fonction qui prend en compte tout ce qu'il y a dans la class
    def __init__(self, prenom, nom):
        self.nom = nom  # Créer deux variables nom et prenom qui sont reliées à deux attributs
        self.prenom = prenom

    # Créer une fonction qui va afficher les noms et prénoms choisis dans une phrase
    def SePresenter(self):
        print("Je suis", self.prenom, self.nom)


# Choisir les noms et prenoms
nom1 = Personne("John", "Doe")
nom2 = Personne("Jean", "Dupond")
nom1.SePresenter()  # afficher la fonction
nom2.SePresenter()
