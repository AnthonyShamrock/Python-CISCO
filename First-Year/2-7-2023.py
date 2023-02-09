def run(): 
    try: 
        a = float(input("Insert a number (decimals are accepts)\n"))
    except:
        print("Must be an decimal (or whole number)")
        run()


    try: 
        b = float(input("Insert another number (decimals are accepts)\n"))
    except:
        print("Must be an decimal (or whole number)")
        run()
    
    print("addition", a+b)
    print("subtract", a-b)
    print("Multiply", a*b)
    if b == 0:
        print ("Can't divide by 0")
    else:
        print("divide", a/b)
    
    print("/nThat's all, folks!")
    run()
run()
