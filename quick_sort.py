import random
from time import perf_counter as pc

l = 1000


def quick_sort(n):
    if len(n) <= 1:
        return n
    else:
        k = random.randint(0, len(n) - 1)
        for i in range(k - 1):
            if n[i] >= n[k]:
                for j in range(i + 1, k - 1):
                    (n[i], n[j]) = (n[j], n[i])
                    print(n[:k - 1])
        for i in range(k, len(n) - 1):
            if n[i] < n[k]:
                for j in range(k, len(n)):
                    (n[i], n[j]) = (n[j], n[i])
    #    print(k)
    return quick_sort(n[0:k])


def quick_sort_2(n):
    if len(n) <= 1:
        return n
    else:
        #        k = random.randint(0, len(n) - 1)
        k = 5
        for i in range(k):
            print(f' n[i] = {n[i]}, n[k] = {n[k]}')
            if n[i] >= n[k]:
                s1 = n[i]
                for j in range(i + 1, k + 1):
                    print(f'j = {j}, n[j] = {n[j]}')
                    n[j - 1] = n[j]
                n[k] = s1
                k -= 1

        return n


def quick_sort_3(n):
    if len(n) <= 1:
        return n
    else:
        #        k = 5
        k = random.randint(0, len(n) - 1)
        print(n[k])
        i = 0
        while i < k and k >= 1:
            if n[i] >= n[k] and i != k - 1:
                (n[k - 1], n[k], n[i]) = (n[k], n[i], n[k - 1])
                k -= 1
            elif n[i] >= n[k] and i == k - 1:
                (n[i], n[k]) = (n[k], n[i])
                k -= 1
            else:
                i += 1
        i += 1
        while i >= k and i < len(n) - 1:
            if n[i] < n[k] and i != k + 1:
                (n[k + 1], n[k], n[i]) = (n[k], n[i], n[k + 1])
                k += 1
            elif n[i] < n[k] and i == k + 1:
                (n[i], n[k]) = (n[k], n[i])
                k += 1
            else:
                i += 1
    return n


def quick_sort_4(n):
    if len(n) <= 1:
        return n
    else:
        k = random.randint(0, len(n) - 1)
        left = [i for i in n if i < n[k]]
        equal = [i for i in n if i == n[k]]
        right = [i for i in n if i > n[k]]
    return quick_sort_4(left) + equal + quick_sort_4(right)


def quick_one(n):
    return n if len(n) <= 1 else quick_one([i for i in n if i < n[0]]) + [i for i in n if i == n[0]] + quick_one(
        [i for i in n if i > n[0]])


a1 = [random.randint(0, 100) for i in range(l)]
a = [1, 3, 5, 4, 7, 2, 6, 8, 9]
# quick_sort_2(a)
# print(a1)
t1 = pc()
quick_one(a1)
t2 = pc()
print(t2 - t1)

t1 = pc()
sorted(a)
t2 = pc()
print(t2 - t1)

# print(b, b[10 - 1])
