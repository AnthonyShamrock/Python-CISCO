## +,-,*,/,**,//,%

def thing(i):
    return eval(f'3{i}2')

for x in {"+","-","*","/","**","//","%"}:
    print("2"+x+"3 =", thing(x))
