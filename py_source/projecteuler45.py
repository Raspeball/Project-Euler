import math

def Trianglenum(n):
    res = (n*(n+1))/2
    
    return res

def Pentagonalnum(k):
    res = (k*(3*k - 1))/2
    
    return res

def Hexagonalnum(j):
    res = j*(2*j - 1)
    
    return res

for h in range(144, 1000):
    for p in range(165, 1000):
        for t in range(285, 1000):
            if Trianglenum(t) == Pentagonalnum(p):
                if Trianglenum(t) == Hexagonalnum(h):
                    print(Trianglenum(t))
            else:
                continue
    