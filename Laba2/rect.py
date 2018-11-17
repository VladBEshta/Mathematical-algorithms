from math import *

def rec(a,b,n):
    if a>=b :
        return 0.0
    else:
        h=(b-a)/n
        S=0
        x=b
        while x>=a:
            S=S+log(5 * x)
            x=x-h
        S=S*h
        return round(S,2)

def eshka(m):
    k = e*m
    return round(k,3)

# rec(0.2,0.3,10)
