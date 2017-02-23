
class CacheServer:
    def __init__ (self, numero, taille, endPoints):
        self.numero = numero
        self.endPoints = endPoints
        self.classementVideo = []
        self.videoAGarder = []
        self.tailleRestante = taille
        self.nombreVideo = 0


    def classement():
        for i in self.endPoints:
            for j in i.nbRequete:
                self.classementVideo.append(i.nbRequete * i.tpsGagne)

    def decision():
        cp = self.classementVideo
        computing = True
        while(computing):
            indexTop = cp.index(max(cp))

            if video[indexTop].taille < self.tailleRestante:
                self.videoAGarder.append(indexTop)
                self.nombreVideo += 1
            cp[indexTop] = 0

            computing = False
            for i in video:
                if i.taille < self.tailleRestante:
                    computing = True

cache = CacheServer(1,100,[])
