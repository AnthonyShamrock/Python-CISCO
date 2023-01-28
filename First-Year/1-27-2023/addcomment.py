def run(a):
  f = open(a)
  b = f.read().splitlines()
  with open(a, "w") as fa:
    for c in b:
      d = c.strip().lower()
      txt = ""
      if d.find("print") != -1:
        txt = "printing a value"       
      elif d.find("if") != -1:
        txt = "if-then statement"
      elif d.find("import") != -1:
        txt ="import module"
      elif len(d) == 0:
        txt = "blank"
      print(c + "# "+txt, file=fa)
