# NEW WAY #
input("THIS CODE CAN STALL AND CRASH COMPUTERS.\nBy running this, you are accepting the risk!\nPress return/enter to continue...");i={"dict": [True],"array": "self","string": 1,"number": True,"bool": {"stat" :True}};exec('try:\n str(2+"s")\nexcept:print(\"Can\'t add string to int")');#Can't add string to int
r=lambda: [print(v, type(v)) and r(v) for v in i.values()] ## stack overflow (or RecursionError)'
exec('while True:\n try:\n  r(i) \n except:\n  print("stack overflow (or RecursionError)")\nraise "Error cause raise is an error statement... also, not in a function"');print("ALSO, the first line has an error... I will let you find it. (Hint: Try looking a comment...):D") # Have fun! :D

# OLD WAY #
input("THIS CODE CAN STALL AND CRASH COMPUTERS.\nBy running this, you are accepting the risk!\nPress return/enter to continue...");i={"dict": [True],"array": "self","string": 1,"number": True,"bool": {"stat" :True}};exec('try:\n str(2+"s")\nexcept:print(\"Can\'t add string to int")');#Can't add string to int
r=lambda:[print(self,type(self))for self in i.values()] ## stack overflow (or RecursionError)
exec('while True: r()\nraise "Error cause raise is an error statement... also, not in a function"');print("ALSO, the first line has an error... I will let you find it. (Hint: Try looking a comment...):D") # Have fun! :D
