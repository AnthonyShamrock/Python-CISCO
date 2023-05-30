'''
force = required to be configured
SKIP = Doesn't ask the user for input
PATH = path from q (dictionary) to a value ex) config.force == True
SkipOver = This section will not be added to the file/list of configurations

Enter to skip options

Warning: It does NOT validate settings and if they are type
'''
q = {
  "default": {
    "force": True,
    "Hostname": "hostname ARG0",
    "Enable Secret": "enable secret ARG0",
    "Banner Motd": 'banner motd "ARGALL"',
    "SKIP": "no ip domain-lookup",
    "SKIP2": "line con 0",
    "SKIP3": "logging sync",
    "SKIP4": "exit",
  },
  "config": {
    "force": True,
    "SkipOver": True,
    "Exec-timeout (in seconds)": "exec-timeout ARG0",
    "Number of interfaces (switch is 15, router is 4)": "line vty 0 ARG0"
  },
  "SSH": {
    "IP Domain Name": "ip domain-name ARG0",
    "SKIP": "crypto key generate RSA general-keys modulus 1024",
    "SKIP1": "ip ssh version 2",
    "SSH Authentication Retries": "ip ssh authentication-retries ARG0",
    "SSH Timeout": "ip ssh time-out ARG0",
    "Username & Secret": "username ARG0 secret ARG1"
  },
  "out-of-band": {
    "SKIP": "line con 0",
    "Out of Band password (enter to skip)": "password ARG0",
    "SKIP1": "login",
    "Login Local (enter to skip)": "login local",
    "PATH":  'config.Exec-timeout (in seconds)',
    "SKIP3": "exit",
  },
  "in-band": {
    "PATH": "config.Number of interfaces (switch is 15, router is 4)",
    "Out of Band password (enter to skip)": "password ARG0",
    "SKIP": "login",
    "Login Local (enter to skip)": "login local",
    "Input Transport SSH (enter to allow telnet)": "transport input ssh",
    "PATH1":  'config.Exec-timeout (in seconds)',
    "SKIP3": "exit",
  },
  "security": {
    "Login-block for (seconds attempts seconds)": "login block-for ARG0 attempts ARG1 within ARG2",
    "Min password length": "security password min-length ARG0",
    "Password encryption": "service password-encryption",
  },
}

print('''* * * * * * * *
Welcome CISCO custom autoconfiguration wizard!

This was programmed in Python by Conor Hamilton in 2023


Data Validation
- - - - - - - -
All input are submitted into str, and translated into plaintext.
We will not handle any validation for your input.


Submitting Responses
- - - - - - - - - - -
Pressing enter will submit your option to the configuration.
If you press enter and there is no input (len == 0), then the option will be disabled (or skipped)

* * * * * * * *
''')

for a in q:
  if not "force" in q[a]:
    c = input("Configure {}? (Y/N)".format(a)).strip().lower()
    if c.find("y") == -1:
      q[a] = None
      continue

  for b in q[a]:
    if type(q[a][b]) is bool or b.find("SKIP") != -1 or b.find("PATH") != -1:
      continue
    i = input(b + ": ").strip()
    if len(i) == 0:
      q[a][b] = None
      continue

    if q[a][b].find("ARGALL") != -1:
      q[a][b] = q[a][b].replace("ARGALL", i)
      continue
    l = i.split(" ")
    requireArgAmount = 0
    for m in q[a][b].split(" "):
      if m.find("ARG") != -1:
        requireArgAmount+=1
    if len(l) != requireArgAmount:
      print("MISSING ARGS")
  
    for c, d in enumerate(l):
      q[a][b] = q[a][b].replace("ARG" + str(c), d)

text = ""
for a in q:
  def parse(b):
    t = ""
    if "SkipOver" in b:
      return t
    for c in b:
      if b[c] == None or type(b[c]) is bool:
        continue
      if type(b[c]) == "dict":
        return parse(b[c])
      if c.find("PATH") != -1:
        p = q
        for x in b[c].split("."):
          p = p[x]
        b[c] = p
      t += str(b[c])+"\n"
    return t
  if q[a] == None:
    continue
  text += parse(q[a])

print("* * * * * * * * *")
print(text)
f = open("config.txt", "w")
f.write(text)
f.close()
