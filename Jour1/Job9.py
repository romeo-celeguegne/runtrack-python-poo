class Produits():
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT + (self.TVA * self.prixHT)
        return prixTTC

    def afficher(self):
        produits = ("Produit:", self.nom, "Prix HT", self.prixHT, "€",
                    "TVA:", self.TVA, "Prix TTC:", self.CalculerPrixTTC(), "€")
        return produits

    def modif_Nom(self, nom):
        self.nom = nom

    def modif_PrixHT(self, prixHT):
        self.prixHT = prixHT

    def afficher_Nom(self):
        return self.nom

    def afficher_PrixHT(self):
        return self.prixHT

    def afficher_TVA(self):
        return self.TVA

    def afficher_PrixTTC(self):
        return self.CalculerPrixTTC()


console = Produits("Playstation 5", 458, 0.20)
print("Produits:", console.afficher_Nom())
print("Prix HT:", console.afficher_PrixHT(), "€")
print("TVA", console.afficher_TVA())
print("Prix TTC:", console.afficher_PrixTTC(), "€\n")


jeux_video = Produits("EA SPORT FOOTBALL 2023", 42, 0.20)
print(jeux_video.afficher())
jeux_video.modif_Nom("FIFA 23")
jeux_video.modif_PrixHT(21)
print("\nProduits:", jeux_video.afficher_Nom())
print("Prix HT:", jeux_video.afficher_PrixHT(), "€")
print("TVA", jeux_video.afficher_TVA())
print("Prix TTC:", jeux_video.afficher_PrixTTC(), "€\n")
