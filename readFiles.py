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

def createList(nbItt, loop):
    if(loop):
        endList = []
        pingList = []
        theseLines = cutLine(nbItt)
        returnItt = int(theseLines[1])+int(nbItt)
        nbItt = int(theseLines[1])
        itsPing = theseLines[0]
    itt = 0
    print "need stop " + str(nbItt)
    while itt < nbItt:
        print "il y a " + str(itt)
        itte = cutLine(itt)
        endList.append(int(itte[0]))
        pingList.append(int(itte[1]))
        itt +=1
    return endList,pingList, returnItt

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

endList,pingList,nextIt = createList(2,True)

for i in range(0,8):
    print endList
    print pingList
    endTemp, pingTemp, nextIt = createList(nextIt, False)
    endList.append(endTemp)
    pingList.append(pingTemp)

print endlist
