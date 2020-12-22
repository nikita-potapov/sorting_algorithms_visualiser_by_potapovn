from random import shuffle
from time import time


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def shake_sort(array):
    n = len(array)
    left = 0
    right = n - 1
    while left <= right:
        for i in range(left, right):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1
        for i in range(right, left, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1
    return array


def comb_sort(array):
    def get_next_gap(previous_gap):
        next_gap = int(previous_gap / 1.247)
        return next_gap if next_gap > 1 else 1

    n = len(array)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False

        for i in range(n - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
    return array


bubble_avg = []
shake_avg = []

n = 1000

for i in range(10):
    w = [x for x in range(n)]
    shuffle(w)

    t = time()
    bubble_sort(w.copy())
    bubble_avg.append(time() - t)

    t = time()
    shake_sort(w.copy())
    shake_avg.append(time() - t)

print('bubble_avg', sum(bubble_avg) / len(bubble_avg))
print('shake_avg ', sum(shake_avg) / len(shake_avg))
