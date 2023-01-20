## Easy way
[(print(a, "this value is", type(a)) and print()) for a in ["Mr.C", 1,
True, 3.14]]

t = {"oct": oct(0o123), "hex": hex(0x1), "exp note": 3**6}
for a,b in t.items():
print(b, "this value is", a)

##My way
[[[[(print(a, "this value is", type(a)) and print()) for a in [b]] for b in
[c]] for c in [d]] for d in["Mr.C", 1, True, 3.14]]
[(print(a, "this value is", type(a)) and print(b)) for a in ["Mr.C", 1,
True, 3.14]]

t = {"oct": oct(0o123), "hex": hex(0x1), "exp note": 3**6}
for a,b in t.items():
print(b, "this value is", a)
