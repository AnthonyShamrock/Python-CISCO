# -- Settings -- #
evenMoreRandomness = True

# -- Ignore below unless you are a epic programmer -- # 
import random
nerdList = []
alphabet=[]
for x in "qwertyuiopasdfghjklzxcvbnm":
    alphabet.append(x)

alphabetLen = len(alphabet)

stupidWords = ["stupid1", "FredTheBuilder", "TELNET","ForgotToOffsetBy1?","antidisestablishmentarianism","badworp"]

def getRandomText():
    returntext = ""
    for c in range(0,random.randrange(10,25)):
        if random.randrange(1,100)==1: 
            returntext+=stupidWords[random.randrange(0,len(stupidWords)-1)]
        returntext += alphabet[random.randrange(0,alphabetLen)]
    return returntext

for a in range(0,random.randrange(4,25)):
    nerdList.append(getRandomText())

print("BEFORE:",nerdList)
random.shuffle(nerdList)
nerdListLen = len(nerdList)

while nerdListLen != 0:
    nerdListLen -= 1
    if evenMoreRandomness:
     nerdList[nerdListLen] = getRandomText()
    print(nerdList[nerdListLen])
