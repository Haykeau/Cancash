class Endpoint():



    def __init__(self, nbRequete,tpsCache, tpsDataCenter):
        self.nbRequete = nbRequete
        self.tpsCache = tpsCache
        self.tpsDataCenter = tpsDataCenter
        self.tpsGagne = self.tempsGagne(tpsCache,tpsDataCenter)
        self.cacheChoisi = self.chooseCache(tpsCache)

    def chooseCache(self,tpsCache):
        mini = min(tpsCache)
        cacheChoisi = tpsCache.index(mini)
        return cacheChoisi

    def tempsGagne(self,tpsCache,tpsDataCenter):
        cacheChoisi = self.chooseCache(tpsCache)
        temps = tpsDataCenter - tpsCache[cacheChoisi]
        return temps
