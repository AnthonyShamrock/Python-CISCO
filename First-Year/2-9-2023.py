def run():
    try:
        return float(input("Enter value for x: "))
    except:
        return run()

x = run()
print("y=", 1/(x+(1/(x+(1/(x+(1/x)))))), "(OLD METHOD)")

s = "1/"
def a():
    return "("+str(x)+"+(1/"
count = 0
while count <= 2:
    count += 1
    s += a()
s+=str(x)
for x in s:
    if x=="(":
        s+=")"

print("y =", eval(s))
