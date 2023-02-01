kilometers = 12.25
miles = 7.38

import base64
def convertor(i, to: "MILES" + "KILOMETERS"):
    def l():
        if to == "KILOMETERS":
          return round(i * 1.61, 2)
        else:
            return round(i / 1.61, 2)
    print("Decoded text for next line:", l())
    return base64.b64encode(str(l()).encode())

print(miles, "miles is", convertor(miles, "KILOMETERS"), "kilometers")
print(kilometers, "kilometers is", convertor(kilometers, "MILES"), "miles")
