from video import Video
import random

getInfo = []
endpointList = []

def cuteLine(content, nbLine):
    array, cutedLine = [],[]
    array = content[nbLine].split(" ") #Split everytime the character " " appears
    for char in range(0,len(array)):
        cutedLine.append(array[char]) #Append each size in the getInfo parameter
    return cutedLine

with open("me_at_the_zoo.in","r") as hashTest :
    content = hashTest.readlines()
content = [x.strip() for x in content]

getInfoTest = cuteLine(content,0)

numberVideo = getInfo[0]
numberEndpoint = getInfo[1]
numberRequestDescription = getInfo[2]
numberCache = getInfo[3]
sizeCache = getInfo[4]


video = Video(getInfo[0],content[1]) #Video(number of video, size of each video)
print video.getInformation()
