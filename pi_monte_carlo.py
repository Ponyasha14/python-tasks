import math
import random
import matplotlib.pyplot as plt

def pi(n):
    s = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        r = math.pow(x, 2) + math.pow(y, 2)
        if r <= 1:
            s += 1
    pi = 4 * s / n
    return pi

print(pi(1000000))