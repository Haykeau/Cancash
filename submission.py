class submission:

    def __init__(self,nmbCacheServer, videosContenu):
        self.nmbCacheServer = nmbCacheServer
        self.videosContenu = videosContenu

        fichier = open("submission.txt", "w")
        fichier.write(numberCache)
        fichier.write("/n")
        for i in numberCache:
            for i in CacheServer.nombreVideo:
                fichier.write("CacheServer.videoAGarder[i] ")
            fichier.write("/n")
