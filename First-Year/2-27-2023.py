import base64
def trimWhitespace(txt: str):
  a = ""
  for b in txt:
    if b.isspace():
      continue
    a+=b
  return a

def run():
  i = trimWhitespace(input("Insert number: "));exec(base64.b64decode(b'aWYgbm90IGkuaXNkaWdpdCgpOgogcHJpbnQoJ011c3QgYmUgYSBudW1iZXIhJyk7IHJ1bigpCmlmIGludChpKSA+PSAxMDA6CiBwcmludChUcnVlKQplbHNlOgogcHJpbnQoRmFsc2Up'))
  run()
run()
