class Point():  # Créer une classe
    def __init__(self, x, y):  # Créer une fonction qui prend en compte tout ce qu'il y a dans la class
        self.x = x  # Créer deux variables x et y qui sont reliées à deux attributs
        self.y = y

    # Créer une fonction qui va afficher les coordonnées rentrés
    def afficherLesPoints(self):
        print("coordonnées: ", self.x, self.y)

    def afficherX(self):  # Créer une fonction qui va afficher seulement le coordonnée x
        print("coordonnée de x: ", self.x)

    def afficherY(self):  # Créer une fonction qui va afficher seulement le coordonnée y
        print("coordonnée de y: ", self.y)

    def changerX(self, x):  # Créer une fonction qui va changer le coordonnée x
        self.x = x
        print("coordonnée changé de x: ", self.x)

    def changerY(self, y):  # Créer une fonction qui va changer le coordonnée y
        self.y = y
        print("coordonnée changé de y: ", self.y)


coordonnees = Point(60, 128)
coordonnees.afficherLesPoints()
coordonnees.afficherX()
coordonnees.afficherY()
coordonnees.changerX(69)  # Choisir le coordonnée à changer
coordonnees.changerY(44)
