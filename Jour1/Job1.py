class Operation():  # Créer une classe
    # Créer une fonction qui prend en compte tout ce qu'il y a dans la class
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1  # Créer deux variables nombre qui sont reliées à deux attributs
        self.nombre2 = nombre2


# Créer une variable qui appelle la class
nombres = Operation(4, 5)
print(nombres)  # afficher la variable
