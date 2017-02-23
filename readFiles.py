from video import Video
import random

with open("me_at_the_zoo.in","r") as hashTest :
    content = hashTest.readlines()
content = [x.strip() for x in content]

getInfo = []
endpointList = []

array = content[0].split(" ")
for char in range(0,len(array)):
    getInfo.append(array[char])

numberVideo = getInfo[0]
numberEndpoint = getInfo[1]
numberRequestDescription = getInfo[2]
numberCache = getInfo[3]
sizeCache = getInfo[4]

video = Video(getInfo[0],content[1])
print video.getInformation()
