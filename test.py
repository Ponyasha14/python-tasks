import random
from time import perf_counter as pc
import matplotlib.pyplot as plt
# from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
# from selection_sort import sel_sort

# y_sel = []
# y_bubble = []
y_py = []
y_quick = []
y_merge = []

l = 10000

for i in range(0, l, 100):
    arr = [random.randint(0, i) for j in range(i)]

    t1_py = pc()
    sorted(arr)
    t2_py = pc()
    y_py.append(t2_py - t1_py)

    # t1_sel = pc()
    # sel_sort(arr)
    # t2_sel = pc()
    # y_sel.append(t2_sel - t1_sel)

    t1_quick = pc()
    quick_sort(arr)
    t2_quick = pc()
    y_quick.append(t2_quick - t1_quick)

    t1_merge = pc()
    merge_sort(arr)
    t2_merge = pc()
    y_merge.append(t2_merge - t1_merge)

    # t1_bubble = pc()
    # bubble_sort(arr)
    # t2_bubble = pc()
    # y_bubble.append(t2_bubble - t1_bubble)

x = [i for i in range(0, l, 100)]

# plt.plot(x, y_sel, linestyle='-', linewidth=1, color='dodgerblue', label='Selection sort')
plt.plot(x, y_quick, linestyle='-', linewidth=1, color='red', label='Quick sort')
plt.plot(x, y_merge, linestyle='-', linewidth=1, color='green', label='Merge sort')
# plt.plot(x, y_bubble, linestyle='-', linewidth=1, color='black', label='Bubble sort')
plt.plot(x, y_py, linestyle='-', linewidth=1, color='orange', label='Python sort')

plt.xlim(0)
plt.ylim(0)
plt.legend()
plt.show()
