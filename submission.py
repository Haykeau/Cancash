class submission:

    def __init__(self,nmbCacheServer, videosContenu):
        self.nmbCacheServer = nmbCacheServer
        self.videosContenu = videosContenu

        fichier = open("submission.txt", "w")
        fichier.write(numberCache)
        fichier.write("/n")
        i = 0
        y = 0
        while ( i <= numberCache):
            while(y <= CacheServer.nombreVideo):
                fichier.write("CacheServer.videoAGarder[i] ")
                y += 1
            fichier.write("/n")
            i +=1
        fichier.close()
