givenPrompt = '''
Today's config comes to you courtesy of Tyler Hilliard You are to configure your Router. You need to follow the best practices we have studied. The device should be named Cookies. All passwords must be at least five characters long. Three bad login attempts within 22 seconds should result in a lockout of three minutes.  Privileged Exec should be protected with the word 0r30! In-Band access should be limited to the most recent version of SSH and a user named ChocolateChip should be able to get in with the word sug4rc0oki3. The domain is walmart.com. SSH sessions should be limited to two login attempts with a timeout of 34 seconds.  Out-of-band access should be protected the same way that in-band access is protected. Anyone attempting to log in should see the following warning: Anyone who tries to hack this device will get poisoned Oreos! You should protect against shoulder-surfing. Untended sessions (in-band and/or out-of-band) should close after Seven minutes. Keep the device from being annoying.
'''
#givenPrompt = input("INSERT PROMPT").strip()

settings = {
  "deviceType": False,
  "hostname": False,
  "security password min-length": 0,
}


questions = {
  "deviceType": {
    "offsetWord": 0,
    "lookFor": ["switch", "router"]
  },
  "hostname": {
    "offsetWord": 1,
    "lookFor": ["named", "called"]
  },
  "security password min-length": {
    "offsetWord": 4,
    "lookFor": ["password"]
  }
}


promptSplit = givenPrompt.strip().split(" ")

def findWordPos(word):
  for index,value in enumerate(promptSplit):
    if value.lower() == word.lower():
      print(index,value)
      return int(index)
  return -1


def wordToInt(text):
  return


for command in questions:
  print(command, type(command), questions[command]["lookFor"], type(questions[command]["lookFor"]))

  if type(questions[command]["lookFor"]) is dict:
    for subLookFor in questions[command]["lookFor"]:
      if givenPrompt.lower().find(questions[command]["lookFor"][subLookFor]) != -1:
        settings[command] = questions["command"]["lookFor"][subLookFor]
        continue
        
  elif type(questions[command]["lookFor"]) is list:
    for subLookFor in range(len(questions[command]["lookFor"])):
      if givenPrompt.lower().find(questions[command]["lookFor"][subLookFor]):
        
        if questions[command]["offsetWord"] > 0:
          pos = findWordPos(questions[command]["lookFor"][subLookFor])
          if pos == -1:
            continue
          settings[command] = promptSplit[pos+questions[command]["offsetWord"]]
          continue
          
        settings[command] = questions[command]["lookFor"][subLookFor]
        
print(settings)
