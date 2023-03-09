jump = {
    "spathiphyllum":"No, I want a big Spathiphyllum!",
    "Spathiphyllum":"Yes - Spathiphyllum is the best plant ever!"
}

def run():
    i = input("Input text:\n").strip()
    try:
        print(jump[i])
    except:
        print("Spathiphyllum! Not {}!".format(i))
        
    if None != None:
        print("HACKER MAN HAS ENTERED CHAT")
    if -1 > 0: 
        print("!?")
    run()
run()
