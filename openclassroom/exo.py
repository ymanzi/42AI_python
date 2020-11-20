#!/usr/bin/python2.7

class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    
    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""
    def ecrire(self, message):
        if self.surface != "":
            self.surface += "\n"
        self.surface += message
    def lire(self):
        print(self.surface)
    def effacer(self):
        self.surface = ""

yves = TableauNoir()

yves.ecrire("Yves")
yves.ecrire("LOL")

yves.lire()
