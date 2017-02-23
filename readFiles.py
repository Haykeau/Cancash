import Endpoint
import video
import random

with open("me_at_the_zoo.in","r") as hashTest :
    content = hashTest.readlines()
content = [x.strip() for x in content]

getInfo = []
endpointList = []
size = []

for i in range(0,100) :
    size.append(int(random.random()*10))


array = content[0].split(" ")
for char in range(0,len(array)):
    getInfo.append(array[char])

numberVideo = getInfo[0]
numberEndpoint = getInfo[1]
numberRequestDescription = getInfo[2]
numberCache = getInfo[3]
sizeCache = getInfo[4]

video = Video(numberVideo,size)



print getInfo
