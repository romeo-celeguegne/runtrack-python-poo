class Operation():  # Créer une classe
    # Créer une fonction qui prend en compte tout ce qu'il y a dans la class
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1  # Créer deux variables nombre qui sont reliées à deux attributs
        self.nombre2 = nombre2

    def afficher(self):  # Créer une fonction qui va afficher les deux nombres choisis dans une phrase
        print("Le nombre1 est", (self.nombre1))
        print("Le nombre2 est", (self.nombre2))


nombres = Operation(4, 5)  # Choisir deux nombres
nombres.afficher()  # Afficher la fonction
