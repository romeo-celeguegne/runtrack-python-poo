class Personnage():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y -= 1

    def haut(self):
        self.y += 1

    def position(self):
        coordonnees = (self.x, self.y)
        return coordonnees


deplacer = Personnage(10, 10)
print(deplacer.position())
deplacer.gauche()
print(deplacer.position())
deplacer.bas()
print(deplacer.position())
deplacer.droite()
print(deplacer.position())
deplacer.haut()
print(deplacer.position())
