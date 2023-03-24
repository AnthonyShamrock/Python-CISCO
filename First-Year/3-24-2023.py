## Messy code, because never knew they existed, made them within 10 minutes

## Order of Operation
import random
op = ["+","-","*","/","**","//","%"]
priority = {"+":3 ,"-":3,"*":2,"/":2,"**": 1,"//":4,"%":4}

for x in op:
    r = random.choice(op)
    value = {r: priority[r], x: priority[x]}
    print("3"+x+"2"+r+"4 =", eval(f'3{x}2{r}4'))
    if value[x] > value[r]:
        print(r+" takes priority over "+x)
    else:
        print(x+" takes priority over "+r)


# pyramid code 
while True:
    blocks = int(input("Enter the number of blocks: ").strip())
    layers = [0]
    for i in range(1, blocks):
        for j in range(len(layers)):
            if blocks == 0:
                continue
            if j+1 >= len(layers):
                layers.append(0)
            
            if layers[j] >= layers[j+1] and blocks > 0:
                layers[j] += 1
                blocks -= 1
    layers.remove(0)
    print("The height of the pyramid:", len(layers))
