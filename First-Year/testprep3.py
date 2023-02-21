""""
Write code that will accept inout and produce output 

Use the input in two different calculations, each of which will use three different operators.  

The first statement shall have no parentheses other than those necessary foor the print statement (assuming that you do your claclulations within a print statement.)  
The second statement will use the same operators, in the same order, but you must use parentheses to change the order of operations.  
Use comments to document what yhou are doing.
"""

operators = ["+", "-", "/", "*", "//", "/"]

class calculate:
    def __init__(self, expression: str):
        if len(expression) == 0:
            raise  Exception("NO INPUT")
        formatStr = ""
        for a in expression:
            if a.isspace() or a.isalpha():
                continue
            formatStr += a
        if len(formatStr) == 0:
            raise Exception("Could parse string")
        self.expression = formatStr
    
    def get(self):
        formatStr = ""
        a = iter(self.expression)

        def parse(a: iter):
            s = ""
            while True:    
                c = next(a)
                if c == "(":
                   c = parse(a)
                elif c == ")":
                    r = str(calculate(s).get())
                    print("Let's calculate:", s, "to:", r)
                    self.expression = self.expression.replace("("+s+")", r)
                    print("updated equation", self.expression)
                    return r          
                s+=c

        for b in a:
            if b == "(":
                b = parse(a)
            formatStr+=b
        
        def combine(a: iter):
            s = ""
            op = ""
            while True:
                b = next(a, "end")
                if b == "end":
                    break
                if not b.isdigit():
                    if op != "":
                        r = str(eval(s))
                        print("Let's calculate:", s, "to:", r)
                        self.expression = self.expression.replace(s, r)
                        print("updated equation", self.expression)
                        if b:
                            return combine(iter(self.expression))
                    op = b
                s+=b
            
        combine(iter(self.expression))
        return eval(self.expression)

def run():
    try:
        a = calculate(input("Insert equation to solve! \n"))
        print(" * * * * * * ")
        print("SOLVED:", a.get())
    except Exception as a:
        print("WARNING: ", a)
    run()
run()