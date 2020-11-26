# global data
numChars = [".","-","0","1","2","3","4","5","6","7","8","9"]

def isSubset(arr1,arr2):
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            return False
    return True

def termToFunction(term,var):
    if isSubset(term,numChars):
        return ConstantFunction(float(term))
    if isSubset(term,numChars+[var,'*']) and term[0] in numChars+[var] and term[len(term)-1]==var:
        if term[0] == var:
            return LinearFunction(1)
        if term[0] == '-' and term[1] == var:
            return LinearFunction(-1)
        return LinearFunction(float(term.replace(var,'').replace('*','')))
    if isSubset(term,numChars+[var,'*','^']) and term[len(term)-1] in ["0","1","2","3","4","5","6","7","8","9"]:
        a = 1
        term = term.replace('*','')
        if term[0] == '-' and term[1] == var:
            a = -1
        if a == 1 and term[0] != var:
            a = float(term[:term.index(var)]) 
        n = float(term[term.index('^')+1:])
        return PolynomialFunction(a,n)   

# FunEx class
class FunEx:
    def __init__(self,expr,var):
        self.terms = self.parseTerms(expr)
        self.subfunctions = []
        for term in self.terms:
            self.subfunctions.append(termToFunction(term,var))
    def parseTerms(self,expr):
        output = []
        for str in expr.split("+"):
            negate = str[0]=="-"
            for str2 in str.split("-"):
                output.append("-"+str2 if negate else str2)
                negate = True
        return output
    def evaluate(self,x):
        output = 0
        for f in self.subfunctions:
            output += f.evaluate(x)
        return output

# classes for function types
class ConstantFunction:
    def __init__(self,c):
        self.c = c
    def evaluate(self,x):
        return self.c        

class LinearFunction:
    def __init__(self,m):
        self.m = m
    def evaluate(self,x):
        return self.m*x

class PolynomialFunction:
    def __init__(self,a,n):
        self.a = a
        self.n = n
    def evaluate(self,x):
        return self.a*pow(x,self.n)

