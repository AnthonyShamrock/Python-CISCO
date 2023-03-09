jump = [lambda: print("Leap year"), lambda: print("Common Year")]

correct = {True: 1, False: 0}

def run():
    year = int(input("Enter a year: ").strip())
    jump[correct[bool(year % 4)]]()
    run()
run()
