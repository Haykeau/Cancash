from Endpoint import*
nbRequete = [1500,10000,300]
tpsCache = [230,111,340,245]
tpsDataCenter = 1000

endpoint = Endpoint(nbRequete,tpsCache,tpsDataCenter)

cacheChoisi = endpoint.chooseCache()
temps = endpoint.tpsGagne()

print(cacheChoisi)
print(temps)
