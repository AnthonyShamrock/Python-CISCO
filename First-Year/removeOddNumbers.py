'''
For today's lab, you are to create a list called Numbers.  Populate it with the numbers one through ten. (A simple assignment statement will do for now.)

Print the contents of the list as well as its length.

Then, using the delete function, a loop, and a continue statement, remove all the odd numbers from the list.

Finally, print the modified list with its length.

As usual, you get credit by creating a document, type your signature at the top, and paste screenshots showing your code and output.
'''

numList = []
for i in range(0,10):
    numList.append(i)

print("LIST:", numList, "LENGTH:", len(numList))

for i in numList:
    if i % 2 == 0:
        continue
    numList.remove(i)

print("LIST:", numList,"NEW LENGTH:", len(numList))
