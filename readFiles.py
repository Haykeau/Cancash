with open("me_at_the_zoo.in","r") as hashTest :
    content = hashTest.readlines()
content = [x.strip() for x in content]

getInfo = []

array = content[0].split(" ")
for char in range(0,len(array)):
    getInfo.append(array[char])

numberVideo = getInfo[0]
numberEndpoint = getInfo[1]
numberRequestDescription = getInfo[2]
numberCache = getInfo[3]
sizeCache = getInfo[4]

print getInfo
