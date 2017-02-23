from video import Video
from Endpoint import Endpoint
import random

global content

def cutLine(nbLine):
    array, cutedLine = [],[]
    array = content[nbLine].split(" ") #Split everytime the character " " appears
    for char in range(0,len(array)):
        cutedLine.append(array[char]) #Append each size in the getInfo parameter
    return cutedLine

def createList(nbLine):
    endList = []
    pingList = []
    theseLines = cutLine(nbLine)
    nbItterations = theseLines[1]
    itsPing = theseLines[0]
    for i in range(0,int(theseLines[1])):
        numberLine = nbLine+i
        itte = cutLine(numberLine)
        endList[i] = itte[0]
        pingList[i] = itte[1]
    return endList,pingList

with open("me_at_the_zoo.in","r") as hashTest :
    content = hashTest.readlines()
content = [x.strip() for x in content]

getInfo = cutLine(0)

numberVideo = getInfo[0]
numberEndpoint = getInfo[1]
numberRequestDescription = getInfo[2]
numberCache = getInfo[3]
sizeCache = getInfo[4]


video = Video(getInfo[0],content[1]) #Video(number of video, size of each video)
a,b = createList(2)
print a
print b
