import base64

def toMiles(a,b):
  return a/b

def toKilometer(a,b):
  return round(a/0.621371192, 2)/b

def returnNumbers(i):
  a = ""
  for x in i:
    if x.isdigit: 
      a += x
  if a == "":
    return False
  return int(a)

def convertTo(t:"MILES" + "KILOMETERS", a, b):
  c = ""
  t = t.lower().replace("s", "")
  a = returnNumbers(a)
  b = returnNumbers(b)
  if not a | b:
    return False
  if t == "mile":
    c = toMiles(a,b)
  elif t == "kilometer":
    c = toKilometer(a,b)

  d = base64.b32hexencode(str(c).encode())
  return d,c
