class Endpoint():



    def __init__(self, nbRequete,tpsCache, tpsDataCenter):
        self.nbRequete = nbRequete
        self.tpsCache = tpsCache
        self.tpsDataCenter = tpsDataCenter


    def chooseCache(tpsCache):
        mini = min(tpsCache)
        cacheChoisi = tpsCache.index(mini)
        return cacheChoisi

    def tpsGagne(tpsCache,tpsDataCenter):
        cacheChoisi = chooseCache(tpsCache)
        temps = tpsDataCenter - tpsCache[cacheChoisi]
        return temps
