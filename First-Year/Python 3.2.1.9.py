#Python 3.2.1.9
import base64
# Encoded chupacabra with base64.
while True:
    i = input("Enter the secret word!\n")
    if i.strip() == base64.b64decode(b'Y2h1cGFjYWJyYQ==').decode():
        print("You've successfully left the loop.")
        break
