import convert

def run():
  a = input("What are you converting? (Kilometers/Miles) \n")
  a = a.lower()
  t = ""
  if a.find("k") == 0:
    t = "KILOMETERS"
  elif a.find("m") == 0:
    t = "MILES"
  else:
    run()

  b = input("Insert number of miles/kiomters and hours \n")
  b = b.split()
  h = ""
  l = ""
  try:
   l = b[0]
  except:
    l = input("Insert number of miles/kilometers you've traveled?\n")
  try:
    h = b[1]
  except:
    h = input("Insert number of hours you have traveled\n")
  r = convert.convertTo(t,l,h)
  if not r:
    print("ERROR OCCURED!")
    run()
  print("MPH: ", r[0], "(", r[1], " MPG [Miles Per Grant])")
  run()
  
    
run()
