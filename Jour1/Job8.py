class Cercle():
    def __init__(self, r):
        self.r = r
        print("Rayon de cercle", r)

    def changerRayon(self, r):
        self.r = r
        print("Rayon = ", r)

    def afficherInfos(self):
        print("Circonférence: ", dessin.circonference(), "cm")
        print("Aire: ", dessin.aire(), "cm")
        print("Diamètre du cercle: ", dessin.diametre(), "cm")

    def circonference(self):
        circonference_total = (3.14 * 2 * self.r)
        return circonference_total

    def aire(self):
        aire_total = (3.14 * (self.r ** 2))
        return aire_total

    def diametre(self):
        diametre_total = (self.r * 2)
        return diametre_total


dessin = Cercle(4)
print("Circonférence: ", dessin.circonference(), "cm")
print("Aire: ", dessin.aire(), "cm")
print("Diamètre du cercle: ", dessin.diametre(), "cm\n")
dessin.changerRayon(7)
dessin.afficherInfos()
