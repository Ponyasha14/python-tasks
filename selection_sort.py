import random
from time import perf_counter as pc


def sel_sort(n):
    if len(n) <= 1:
        return n
    else:
        for j in range(len(n) - 1):
            k = j
            m = n[j]
            for i in range(j + 1, len(n) + 1):
                if n[i - 1] < m:
                    k = i - 1
                    m = n[k]
            (n[j], n[k]) = (n[k], n[j])
            k += 1
    return n


a1 = [0, 1, 5, 5, 6, 2, 1, 1, 3]
a = [random.randint(0, 100) for i in range(1000)]
#print(a)
t1 = pc()
sel_sort(a)
t2 = pc()
print(t2 - t1)

print(123)

t1 = pc()
sorted(a)
t2 = pc()
print(t2 - t1)