import requests # Allows program to send API requests
import json # decodes JSON

i = input("insert random string: ").strip() # Input string and remove whitespace

def checkIfWord(word: str): #Sends string to API to check if word. 
    try:
      json.loads(requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').text)[0]["word"] # Errors if not a word
      return True
    except:
      return False
      
l = [] # List (almost) every possible combinations of string
for a in i: # Loop through string first and set the first letter
  word = a # the word to compare
  for b in i: # Checks loop through each character 
    if b == a: # prevent duplicate words
      continue
    word += b # add character to word
    if not checkIfWord(str(word)): #Check if word is real
      print("NOT A WORD", word)
      continue
    l.append(word) ## Adds to list
    
print(l)
