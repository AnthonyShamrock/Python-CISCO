## EASY WAY -- (better way next page)
arrow = [" *"," * *"," * *", " * *", "*** ***", " * *", " * *", "
*****"]
##print("\n".join(arrow))
str = ""
i = 0
for a in arrow:
 def run():
  return a+a.rjust(10, " ") +"\n"
  for x in range(1):
   str += run()

print(str)

## MY WAY-- (More fun way)
arrow = [" *"," * *"," * *", " * *", "*** ***", " * *", " * *", "
*****"]
##print("\n".join(arrow))
str = ""
i = 0
for a in arrow:
 def space(l):
  l = 10
  l -= len(a)
  if l <= 0:
    return ""
  b = ""
  for _ in range(l):
   b += " "
  return b

 def run():
    return a+space(len(a))+a +"\n"

 for x in range(1):
  str += run()

print(str)
