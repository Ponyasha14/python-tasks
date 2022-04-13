import random
from time import perf_counter as pc
import matplotlib.pyplot as plt
import numpy as np

y_sel = []
y_bubble = []
y_quick = []
y_merge = []


def bubble_sort(s):
    for i in range(len(s)):
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                (s[i], s[i + 1]) = (s[i + 1], s[i])
    return s


def quick_sort(n):
    if len(n) <= 1:
        return n
    else:
        k = random.randint(0, len(n) - 1)
        left = [i for i in n if i < n[k]]
        equal = [i for i in n if i == n[k]]
        right = [i for i in n if i > n[k]]
    return quick_sort(left) + equal + quick_sort(right)


def merge_sort(n):
    j = 0
    if len(n) <= 1:
        return n
    else:
        left = [n[i] for i in range(int(len(n) / 2))]
        right = [n[i] for i in range(int(len(n) / 2), len(n))]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)


def merge(left, right):
    s = [0 for i in range(len(left) + len(right))]
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            s[i + j] = left[i]
            i += 1
        else:
            s[i + j] = right[j]
            j += 1
    if i == len(left):
        for k in range(j, len(right)):
            s[k + i] = right[j]
            j += 1
    if j == len(right):
        for k in range(i, len(left)):
            s[k + j] = left[i]
            i += 1
    return s


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


l = 10000

for i in range(0, l, 100):
    arr = [random.randint(0, i) for j in range(i)]

    t1_sel = pc()
    sel_sort(arr)
    t2_sel = pc()
    y_sel.append(t2_sel - t1_sel)

    t1_quick = pc()
    quick_sort(arr)
    t2_quick = pc()
    y_quick.append(t2_quick - t1_quick)

    t1_merge = pc()
    merge_sort(arr)
    t2_merge = pc()
    y_merge.append(t2_merge - t1_merge)

    t1_bubble = pc()
    bubble_sort(arr)
    t2_bubble = pc()
    y_bubble.append(t2_bubble - t1_bubble)

x = [i for i in range(0, l, 100)]

plt.plot(x, y_sel, linestyle='-', linewidth=1, color='dodgerblue', label='Selection sort')
plt.plot(x, y_quick, linestyle='-', linewidth=1, color='red', label='Quick sort')
plt.plot(x, y_merge, linestyle='-', linewidth=1, color='green', label='Merge sort')
plt.plot(x, y_bubble, linestyle='-', linewidth=1, color='black', label='Bubble sort')

plt.xlim(0)
plt.ylim(0)
plt.legend()
plt.show()
