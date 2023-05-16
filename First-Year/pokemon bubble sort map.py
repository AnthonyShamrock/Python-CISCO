import requests
import json
import random

def getPokemon():
  returnList = []
  rad = random.randrange(1,1225)
  a = requests.get(f'https://pokeapi.co/api/v2/pokemon/?offset={rad}&limit=5')
  for b in json.loads(a.text)["results"]:
    try:
      returnList.append(b['name'])
    except:
      print("ERROR")
  return returnList    

def sort(targetList):
    compareList = targetList # Just to compare of they are same
    lenList = len(targetList)
    
    for a in range(lenList-1):
        for b in range(lenList-1):
            if targetList[b] > targetList[b+1]:
                targetList[b], targetList[b+1] = targetList[b+1], targetList[b]
                print("CHANGE IN LIST:", targetList)
                
        if compareList == targetList:
            print("NO CHANGES NEEDED")
            return targetList
        return targetList

l = getPokemon()
print("ORGINIAL LIST:", l)
print("FINAL LIST:", sort(l))
