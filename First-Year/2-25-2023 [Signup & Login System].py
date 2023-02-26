'''
Understand
Boolean operators
Octal and Hexdecimal variables
Mathematical operators, specifically, know the order of operations.
Write code that demonstrates your understanding of the following:

Write code that will use all the mathematical operators we have learned (+,-,*,/,**,//,%)  
'''
import threading
import time
securityRequirements = {"minLength": 8, "containSpecialCharacter": True, "Security": {"maxRetries": 3, "timeOut": 10}, "Login": {"checkIfUser": False, "enforceInputLength": False}}
retries = {"system": 0 }

try:
  open("userInformation.txt","r").close()
except:
  open("userInformation.txt", "w").close()

def removeWhitespace(text: str):
  a = ""
  for b in text:
    if b.isspace():
      continue
    a += b
  return a

def isUsernameAvailable(username: str):
  f = open("userInformation.txt", "r")
  for b in f:
    b = removeWhitespace(str(b).replace("\n", "")).split(":")
    if b[0].lower().replace("\n", "") == username.lower():
      f.close()
      return False
  f.close()
  return True

def security():
  if retries["system"] >= securityRequirements["Security"]["maxRetries"]:
    print("RATELIMITED TRY AGAIN LATER")
    time.sleep(securityRequirements["Security"]["timeOut"])
    retries["system"] = 0
    return False
  def init():
    retries["system"] += 1
    time.sleep(securityRequirements["Security"]["timeOut"])
    retries["system"] -= 1
  threading.Thread(target = init).start()

def doesUserPasswordMatch(username:str, password: str):
  f = open("userInformation.txt", "r")
  for b in f:
    b = removeWhitespace(str(b).replace("\n", "")).split(":")
    if b[0].lower() == username.lower():
      f.close()
      return password == str(b[1])
  f.close()
  return False

class accountManager():
  def __init__(self):
    self.username = None
    self.password = None
    print("\nUser Login")
    def getUsername():
      user = removeWhitespace(str(input("\nInput your username: ")).lower())
      if securityRequirements["Login"]["enforceInputLength"] and len(user) < 4:
        print("INVALID USERNAME")
        return getUsername()
      if securityRequirements["Login"]["checkIfUser"] and isUsernameAvailable(user):
        print("User does not exist!")
        return getUsername()
      return user
    self.username = getUsername()
    def inputPassword():
      password = removeWhitespace(str(input("\nInput your (case sensitive) password: ")))
      if securityRequirements["Login"]["enforceInputLength"] and len(password) < 4:
        print("INVALID PASSWORD ")
        return inputPassword()
      return password
    self.password = inputPassword()

  def login(self):
    security()
    if doesUserPasswordMatch(self.username, self.password): 
      print("logged in")
      return True
    print('INVALID USERNAME OR PASSWORD')

class createAccount():
    def __init__(self):
        self.username = None
        self.password = None

        def selectUsername():
            user = removeWhitespace(str(input("\nCreate a username\nMin length: 4 characters\n")))
            if len(user) < 4:
                print("Invalid length, min length is 4 character")
                return selectUsername()
            if not isUsernameAvailable(user):
                print("Account Username was taken")
                return selectUsername()
            return user
        self.username = selectUsername()
        
        def createPassword():
          password = removeWhitespace(str(input("\nCreate a password\nMin length: 8 characters,\nMust contain atleast 1 special character ( !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ )\n")))
          if securityRequirements["minLength"]:
            if len(password) < securityRequirements["minLength"]:
              print("Password must be atleast {} characters long!".format(str(securityRequirements["minLength"])))
              return createPassword()
          if securityRequirements["containSpecialCharacter"] == True:
            specialCharacters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
            def find():
              for special in specialCharacters:
                if password.find(str(special)) != -1:
                  return True
              return False
  
            if not find():
              print("Password must contain a special character!")
              return createPassword()
          return password
        self.password = createPassword()    
    def verifyAccount(self):
      def verify():
        i = removeWhitespace(str(input(("\n\nPlease confirm that you want to CREATE an account with the following:\nUsername: {}\nPassword: {}\n\nEnter yes (y) to create account or no (n) to cancel!\n").format(str(self.username), str(self.password)))))
        if i.find("n") != -1:
          print("\n\nCANCELLING ACCOUNT CREATION")
          self.username = None
          self.password = None
          print("CANCELED ACCOUNT CREATION")
          return False
        elif i.find("y") != -1:
          print("\n\nCREATING ACCOUNT")
          f = open("userInformation.txt", "a")
          f.write("\n{}:{}".format(self.username, self.password))
          f.close()
          print("ACCOUNT CREATED")
          return True
        else:
          return verify()
      return verify()
      
def run(forceLogin: bool):
  type = "l" if forceLogin  else input("login or signup?\n").lower()

  if type.find("c") != -1:
    exit()
  if type.find("s") != -1:
    security()
    print("Create an account")
    u = createAccount()
    if not u.verifyAccount():
      run(False)
    print("\nPlease login!\n")
    run(True)
    
  if type.find("l") != -1:
    if not forceLogin:
      security()
    u = accountManager()
    u.login()
  run(False)
run(False)
