class Voiture:

    def __init__(self):
        self.nom = "Modus"
        self.roues = 4
    def _get_roues(self):
        print("Nombre de roues : ")
        return self.roues
    def _set_roues(self, r):
        self.roues = r
        print("Chg de roues")

    roues=property(_get_roues, _set_roues)
