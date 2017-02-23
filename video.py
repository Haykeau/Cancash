# -*- coding: utf-8 -*-
class Video:

    def __init__(self, numero, taille):
        self.numero = numero
        self.taille = taille

    def getInformation(self):
        return "There are " + self.numero + " videos"
