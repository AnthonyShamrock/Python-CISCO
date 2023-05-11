''' ## Oh look, instructions!
Create code where you use lists.  ## EPIC COMMENT LINE 1
to get credit, your code must use .insert(), .append(), and negative indexes.  ## EPIC COMMENT LINE 2
USE comments to show tthat you understand what your code is doing! ## EPIC COMMENT LINE 3
''' ## Epic Comment

# -- Ignore below unless you are a epic programmer -- # 
import random # Import module for random ranges, and shuffle lists!
nerdList = [] # HEY LOOK IT IS A LIST! 
alphabet=[] # WAIT A SECOND? ANOTHER LIST? 
for x in "qwertyuiopasdfghjklzxcvbnm": ## I was too lazy to add each letter so COMPUTER do for it me!
    alphabet.append(x) 

alphabetLen = len(alphabet) ## Len of the alphabet

# List of stupid words to randomly be mixxed in 
stupidWords = ["stupid1", "FredTheBuilder", "TELNET","ForgotToOffsetBy1?","antidisestablishmentarianism","badworp"]

def getRandomText(): ## FUNCTION MAN
    returntext = "" ## Throwing random characters the list
    for c in range(0,random.randrange(10,25)): # Random length for each string to ensure uniqueness!
        if random.randrange(1,100)==1: ## Easter egg conditional statement so random words form stupidWords are mixed in
            returntext+=stupidWords[random.randrange(0,len(stupidWords)-1)] # Did I mention the stupid words are funny? It make sure no errors happen by offsetting by 1
        returntext += alphabet[random.randrange(0,alphabetLen)] # Please add a random letter is the mix!
    return returntext ## Return the random string of characters

for a in range(0,random.randrange(4,25)): # Can I get a list of random words and characters?
    nerdList.append(getRandomText()) ## I want to add something important to the list

nerdList[-1] = nerdList ## Reserve List == list.reserve()
print("BEFORE:",nerdList) # Print statement of before shuffle cause  it is funny
random.shuffle(nerdList) ## Shuffles the list random
for a in nerdList: ## Print the random strings please
    print(a) # OH YA IT PRINTS!

