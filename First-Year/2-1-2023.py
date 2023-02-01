print("Imagine not signing in. Turn off auto-login, nerd.")

def security(i):
  if "q!" in a:
    print("ERROR: Attempted injection")
    quit()
  return True

def returnNumbers(i):
  c = ""
  for x in i:
    if x.isdigit():
      c += x
  return int(c)
  
a = str(input("Insert your name.\n"))
security(a)
b = str(input("What year were you born? \n"))
security(b)
print(("You are ~{age} years old").format(age = 2023 - returnNumbers(b)))
