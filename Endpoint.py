class Endpoint():



    def __init__(self, nbRequete,tpsCache, tpsDataCenter):
        self.nbRequete = nbRequete
        self.tpsCache = tpsCache
        self.tpsDataCenter = tpsDataCenter


    def chooseCache(self,tpsCache):
        mini = min(tpsCache)
        cacheChoisi = tpsCache.index(mini)
        return cacheChoisi

    def tpsGagne(self,tpsCache,tpsDataCenter):
        cacheChoisi = self.chooseCache(tpsCache)
        temps = tpsDataCenter - tpsCache[cacheChoisi]
        return temps
