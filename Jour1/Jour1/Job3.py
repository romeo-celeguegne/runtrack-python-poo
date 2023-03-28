class Operation():  # Créer une classe
    # Créer une fonction qui prend en compte tout ce qu'il y a dans la class
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1  # Créer deux variables nombre qui sont reliées à deux attributs
        self.nombre2 = nombre2

    def additioner(self):  # Créer une fonction qui va additioner les deux nombres choisis
        print((self.nombre1)+(self.nombre2))


nombres = Operation(12, 3)  # Choisir deux nombres
nombres.additioner()  # Afficher la fonction
