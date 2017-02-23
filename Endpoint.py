class Endpoint():
    //docstring for Endpoint.


    def __init__(self, nbRequete,tpsCache, tpsDataCenter):
        self.nbRequete = nbRequete
        self.tpsCache = tpsCache
        self.tpsDataCenter = tpsDataCenter
        self.numEndPoint = numEndPoint

    def chooseCache(tpsCache):
        mini = min(tpsCache)
        cacheChoisi = tpsCache.index(mini)
        return cacheChoisi

    def tpsGagne(nbRequete,tpsCache,tpsDataCenter):
        cacheChoisi = chooseCache(tpsCache)
        moyenne = 0
        for video in nbRequete:
            
