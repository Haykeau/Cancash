
class CacheServer:
    def __init__ (self, numero, taille, endPoints):
        self.numero = numero
        self.endPoints = endPoints
        self.classementVideo = []
        self.videoAGarder = []
        self.tailleRestante = taille


    def classement():
        for i in self.endPoints:
            for j in i.nbRequete:
                self.classementVideo = i.nbRequete * i.tpsGagne
        self.classementVideo.sort()
        self.classementVideo[::-1]

    def decision():
        for i in classementVideo:
            if gb.video[].taille < self.tailleRestante:
                self.videoAGarder.append()
