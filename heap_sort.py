import random
from time import perf_counter as pc

l = 100

def heap_sort(s):
    return s

def heapify(s):
    s1 = max(s)
    for i in range(int(len(s) / 2)):
        if s[i] < s[2 * i + 1]:
            print(s[i], s[2 * i + 1])
            (s[i], s[2 * i + 1]) = (s[2 * i + 1], s[i])
        if s[i] < s[2 * i]:
            print(s[i], s[2 * i])
            (s[i], s[2 * i]) = (s[2 * i], s[i])
    print(s)
    return s

a = [10, 8, 1, 7, 5, 2, 3, 4, 6, 9]
heapify(a)
a1 = [random.randint(0, 100) for i in range(l)]
#heap_sort(a)
#print(heap_sort(a))