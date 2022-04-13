import random
from time import perf_counter as pc
import matplotlib.pyplot as plt
import numpy as np

# x = [i for i in range(1000)]
# y = []
# x2 = [i * i / 5000000 for i in range(1000)]
# k = 0

def bubble_sort(s):
    for i in range(len(s)):
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                (s[i], s[i + 1]) = (s[i + 1], s[i])
    return s
# a = [random.randint(0, 100) for i in range(1000)]

# t1 = pc()
# bubble_sort(a)
# t2 = pc()
# print(t2 - t1)

#for i in range(1000):
#    bubble_sort([random.randint(0, 100) for j in range(i)])
#    k += 1
#plt.plot(x, y, '.')
#plt.plot(x, x2)
#plt.show()
#a = [random.randint(0, 100) for i in range(30)]
#print('Изначальный список: ',a)
#print('Отсотрированный: ', bubble_sort(a))