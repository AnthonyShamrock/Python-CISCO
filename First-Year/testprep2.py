sep = "# # # # # # # # #"
class nerd():
    def stringCompare():
        print('"2" is a string, proof:', type("2"))
        print(2, " is a number, proof:", type(2))

    def booLeanNerd():
        print(True, False)
        print("True/False question, or binary question\nThis incidates if something is successful or enable/disable a settting")

    def combineStringInt():
        h = "STRING "
        try:
            h += 1
        except:
            print("ERROR: Adding integer to string will error! \n CODE:\n h = \"STRING\" \n h += 1")
    
    def combineStringFloat():
        h = "STRING "
        try:
            h += 1.0
        except:
            print("ERROR: Adding float to string will error! \n CODE:\n h = \"STRING\" \n h += 1.0")

    def multStringInt():
        h = "STRING "
        try:
            h *= 1
        except:
            print("ERROR: Multiplying integer to string will error! \n CODE:\n h = \"STRING\" \n h *= 1")

    def multStringFloat():
        h = "STRING "
        try:
            h *= 1.0
        except:
            print("ERROR: Multiplying float to string will error! \n CODE:\n h = \"STRING\" \n h *= 1.0")

    def defaultPrint():
        print("Default Seperator for print: ' ' (space)")
        print("Default end for print: \\n (whitespace, new line)")

for ran in dir(nerd):
    if ran.startswith("__"): continue
    print(sep,ran, sep)
    getattr(nerd, ran)()

def run():
    sep1 = input("Change seperator\ndefault: \" \" (space)\n\nENTER TO SKIP\n")
    if len(str(sep1)) == 0:
        sep1 = " "
    end1 = input("Change terminator (or line splitter)\ndefault: \"\\n\"\nENTER TO SKIP\n")
    if len(str(end1)) == 0:
        end1 = "\n"
    
    print("TEST", "1", "2", sep=sep1, end=end1)

run()
