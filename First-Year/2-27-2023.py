find = {
  True: lambda x: print(int(x) >= 100),
  False: lambda x: print("MUST BE A DIGIT")
}

def run():
  i = input("Insert number: ").strip()
  find[i.isdigit()](i)
  run()
run()

## FUNNY OLD WAY ##
import base64
exec(base64.b64decode(b'ZGVmIHRyaW1XaGl0ZXNwYWNlKHR4dDogc3RyKToKICBhID0gIiIKICBmb3IgYiBpbiB0eHQ6CiAgICBpZiBiLmlzc3BhY2UoKToKICAgICAgY29udGludWUKICAgIGErPWIKICByZXR1cm4gYQoKZGVmIHJ1bigpOgogIGkgPSB0cmltV2hpdGVzcGFjZShpbnB1dCgiSW5zZXJ0IG51bWJlcjogIikpO2V4ZWMoYmFzZTY0LmI2NGRlY29kZShiJ2FXWWdibTkwSUdrdWFYTmthV2RwZENncE9nb2djSEpwYm5Rb0owMTFjM1FnWW1VZ1lTQnVkVzFpWlhJaEp5azdJSEoxYmlncENtbG1JR2x1ZENocEtTQStQU0F4TURBNkNpQndjbWx1ZENoVWNuVmxLUXBsYkhObE9nb2djSEpwYm5Rb1JtRnNjMlVwJykpCiAgcnVuKCkKcnVuKCkK'.decode()))

## OLD WAY ##
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
