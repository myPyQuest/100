""" #24 **Sorting**
    Implement two types of sorting algorithms:
    Merge sort and bubble sort.
"""
import random


def draw_array(array):
    for i in range(len(array)):
        for j in range(array[i]):
            print(' =', end='')
        print('')


def merge(lst0, lst1):
    ret = []
    while lst0 and lst1:
        if lst0[0] <= lst1[0]:
            ret.append(lst0.pop(0))
        else:
            ret.append(lst1.pop(0))
    ret.extend(lst0)
    ret.extend(lst1)
    return ret


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    # random to avoid dead loop for special sequence
    r = lst[random.randint(0, len(lst) - 1)]
    left, mid, right = [], [], []
    for i in lst:
        if i < r:
            left.append(i)
        elif i == r:
            mid.append(i)
        else:
            right.append(i)
    left = merge_sort(left)
    left.extend(mid)
    right = merge_sort(right)
    ret = merge(left, right)
    return ret


""" bubble sorted array
"""


def bubble(bad_list):
    length = len(bad_list) - 1
    sort_ed = False  # Haven't started sorting yet

    while not sort_ed:
        sort_ed = True  # Assume the list is now sorted
        for i in range(length):
            if bad_list[i] > bad_list[i + 1]:
                sort_ed = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]


a = [1, 2, 3, 8, 7, 6, 4, 5, 0]

print(a)
bubble(a)
print(a)