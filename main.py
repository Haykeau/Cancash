from cacheServer import *
from Endpoint import *
from video import *
from readFiles import *
from submission import *

nbRequete = [2333,58884,5455,2]
tpsCache = [122, 56, 55, 5]
infoVideos = [25,65,9,45]
videos = []
i = 0
for j in videos:
    videos.append(Video(i, j))
    i += 1

endpoints = Endpoint(nbRequete,tpsCache, tpsDataCenter)
cache = CacheServer(1, 300, endpoints)
