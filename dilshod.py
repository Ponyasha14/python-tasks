from math import sqrt, pow
import numpy as np

s = {1: 1, 2: 1}


def fibonachi(n):
    if s.get(n) != None:
        return s[n]
    else:
        s[n] = fibonachi(n - 1) + fibonachi(n - 2)
        return s[n]

fibonachi(999)
fibonachi(1995)
print(fibonachi(1000))
