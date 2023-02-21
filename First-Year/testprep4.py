input("THIS CODE CAN SHALL AND CRASH COMPUTERS.\nBy running this, you are accepting the risk!\nPress return/enter to continue...");i={"dict": [True],"array": "self","string": 1,"number": True,"bool": {"stat" :True}};exec('try:\n str(2+"s")\nexcept:print(\"Can\'t add string to int")');#Can't add string to int
r=lambda:[print(self,type(self))for self in i.values()] ## stack overflow (or RecursionError)
exec('while True: r()\nraise "Error cause raise is an error statement... also, not in a function"');print("ALSO, the first line has an error... I will let you find it. (Hint: Try looking a comment...):D") # Have fun! :D

'''
**HINT: READ THE TOP LINE OF CODE FOR THE 3RD ERROR!**

Happy Treasure hinting! 😀

Can’t find them?
1. One line catch error?
str(2+"s")
Hint: It is the orange text which means it in quotations… 
This function is built-in to Python, and most people don’t know about it. It took me a while to find how make try..except.. Statement to become compressed. Lucky, I found in hidden away in documentation the “EXEC” function! 
So, I did the following
exec('try:\n str(2+"s")\nexcept:print(\"Can\'t add string to int")')

Which is the same as:
try:
    str(2+"s")
except:
    print("Can't add string to int")

2. Where the code goes crazy…..
r=lambda:[print(self,type(self))for self in i.values()]
The code above uses lambda function along with “List Comprehensions” to make this single line function. def can’t work here because it needs multiple lines. So we used, the statement below:
exec('while True: r()\n')
This statement causes a stack overflow (if we have a self statement properly set up), but in cause it a silented RecursionError because of the “While True statement.” If I added r() to the top line under 2, then you will see the error.

3. Raise…
WE DEMAND A RAISE! Not that type of a raise, python raise is similar to an error statement which causes an error to occur…  Look after the “\n” to see where the statement is
Remember that exec(), we talked about in 1? We used it again.

exec('while True: r()\nraise "Error cause raise is an error statement... also, not in a function"');print("ALSO, the first line has an error... I will let you find it. (Hint: Try looking a comment...):D") # Have fun! :D
'''
