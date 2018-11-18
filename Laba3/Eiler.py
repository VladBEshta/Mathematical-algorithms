import sys
import numpy as np
from math import exp

def feval(funcName, *args):
    return eval(funcName)(*args)


def backwardEuler(func, yinit, x_range, h):
    m = len(yinit)
    n = int((x_range[-1] - x_range[0])/h)

    x = x_range[0]
    y = yinit

    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n):
        yprime = feval(func, x+h, y)/(1+h)

        for j in range(m):
            y[j] = y[j] + h*yprime[j]

        x += h
        xsol = np.append(xsol, x)

        for r in range(len(y)):
            ysol = np.append(ysol, y[r])
    ysol.tolist()
            # Saves all new y's
    print ([xsol, ysol])
    return ysol



def myFunc(x, y):
    dy = np.zeros((len(y)))
    dy[0] = y[0] + exp(x)/x
    print(dy)
    return dy


h = 0.1
x = np.array([1.0, 2.0])
yinit = np.array([0])

backwardEuler('myFunc', yinit, x, h)


