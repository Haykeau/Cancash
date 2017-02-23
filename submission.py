from readFiles import *
from cacheServer import *

class submission:

    def __init__(self,nmbCacheServer, videosContenu):
        self.nmbCacheServer = nmbCacheServer
        self.videosContenu = videosContenu

        fichier = open("submission.txt", "w")
        fichier.write(nmbCacheServer)
        fichier.write("/n")
        i = 0
        y = 0
        while ( i <= nmbCacheServer):
            fichier.write(i + " ")
            for y in CacheServer.viderAGarder:
                fichier.write(y)
            fichier.write("/n")
            i +=1
        fichier.close()
