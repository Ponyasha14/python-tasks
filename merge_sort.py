import random
from time import perf_counter as pc


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



a = [random.randint(0, 100) for i in range(1000)]
to_be_checked = sorted(a.copy())
# print(to_be_checked, merge_sort(a), end='\n')
assert to_be_checked == merge_sort(a)
t1 = pc()
merge_sort(a)
t2 = pc()
print(t2 - t1)