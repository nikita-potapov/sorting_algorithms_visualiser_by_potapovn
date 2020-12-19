from math import ceil, floor

count = 0

def bubble_sort(array, sorting_history, *args):
    # Сортировка пузырьком
    size = len(array)
    for i in range(size):
        for j in range(size - i - 1):
            # todo
            sorting_history(array, j, j + 1, -1, -1)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    sorting_history(array, -1, -1, -1, -1)
    return


def shake_sort(array, sorting_history, *args):
    # Сортировка перемешиванием
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right, 1):
            # todo
            sorting_history(array, i, i + 1, -1, -1)
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1
        for i in range(right, left, -1):
            # todo
            sorting_history(array, -1, -1, i, i + 1)
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1
    sorting_history(array, -1, -1, -1, -1)
    return


def comb_sort(array, sorting_history, *args):
    # Сортировка расческой

    def get_gap(prev_gap):
        gap = int(prev_gap / 1.3)
        if gap < 1:
            return 1
        return gap

    size = len(array)
    gap = size
    swapped = True

    while gap != 1 or swapped:
        gap = get_gap(gap)
        swapped = False

        for idx in range(0, size - gap):
            # todo
            sorting_history(array, idx, idx + gap, -1, -1)

            if array[idx] > array[idx + gap]:
                array[idx], array[idx + gap] = array[idx + gap], array[idx]
                swapped = True
    sorting_history(array, -1, -1, -1, -1)


def insert_sort(array, sorting_history, *args):
    # Сортировка вставками
    size = len(array)
    for i in range(1, size):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key:
            # todo
            sorting_history(array, j, -1, i, -1)
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    sorting_history(array, -1, -1, -1, -1)


def shell_sort(array, sorting_history, *args, gaps_type="ciura"):
    # Сортировка Шелла

    # Функции для получения элементов различных последовательностей расстояний
    # между сравниваемыми элементами в сортируемом массиве
    def get_shell_gaps(n):
        gaps, k = [], 0
        get_gaps_sequence_element = lambda k: floor(n / 2 ** k)
        while get_gaps_sequence_element(k) > 1:
            gaps.append(get_gaps_sequence_element(k))
            k += 1
        return gaps + [1]

    def get_ciura_gaps(*args):
        return [1750, 701, 301, 132, 57, 23, 10, 4, 1]

    def get_tokuda_gaps(n):
        # N. Tokuda, An Improved Shellsort, IFIP Transactions, A-12 (1992) 449-457
        gaps, k = [], 1
        get_gaps_sequence_element = lambda k: ceil((9 * (9 / 4) ** (k - 1) - 4) / 5)
        while get_gaps_sequence_element(k) <= n:
            gaps = [get_gaps_sequence_element(k)] + gaps
            k += 1
        return gaps

    def get_knuth_gaps(n):
        # Knuth, Donald E. (1997). The Art of Computer Programming.
        gaps, k = [], 0
        get_gaps_sequence_element = lambda k: (3 ** k - 1) // 2
        while get_gaps_sequence_element(k) < ceil(n / 3):
            gaps = [get_gaps_sequence_element(k)] + gaps
            k += 1
        return gaps

    GAPS_TYPES = {
        "ciura": get_ciura_gaps,
        "shell": get_shell_gaps,
        "tokuda": get_tokuda_gaps,
        "knuth": get_knuth_gaps
    }

    gaps = GAPS_TYPES.get(gaps_type, "ciura")(len(array))
    for gap in gaps:
        for i in range(gap, len(array)):
            temp, j = array[i], i
            while j >= gap and array[j - gap] > temp:
                # todo
                sorting_history(array, j, j - gap, -1, -1)
                array[j] = array[j - gap]
                j -= gap
            # todo
            sorting_history(array, -1, -1, i, j)
            array[j] = temp
    sorting_history(array, -1, -1, -1, -1)


def binary_insertion_sort(array, sorting_history, *args):
    # Сортировка бинарным деревом

    def binary_search(arr, val, start, end, current):
        if start == end:
            if arr[start] > val:
                return start
            else:
                return start + 1
        if start > end:
            return start

        mid = round((start + end) / 2)
        # todo
        sorting_history(arr, start, end, mid, current)
        if arr[mid] < val:
            return binary_search(arr, val, mid + 1, end, current)
        elif arr[mid] > val:
            return binary_search(arr, val, start, mid - 1, current)
        else:
            return mid

    for i in range(1, len(array)):
        val = array[i]
        j = binary_search(array, val, 0, i - 1, i)
        array[0:len(array)] = array[:j] + [val] + array[j:i] + array[i + 1:]
    sorting_history(array, -1, -1, -1, -1)


def selection_sort(array, sorting_history, *args):
    # Сортировка выбором
    size = len(array)
    for i in range(size - 1):
        small_index = i
        for j in range(i, size):
            # todo
            sorting_history(array, j, -1, i, -1)
            if array[j] < array[small_index]:
                small_index = j
        array[i], array[small_index] = array[small_index], array[i]
    sorting_history(array, -1, -1, -1, -1)


def heap_sort(array, sorting_history, *args):
    # Пирамидальная сортировка (кучей)

    def heapify(array, count):
        start = (count - 1) // 2
        while start >= 0:
            sift_down(array, start, count - 1)
            start -= 1

    def sift_down(array, start, end):
        root = start
        while 2 * root + 1 <= end:
            child = 2 * root + 1
            swap = root
            if array[swap] < array[child]:
                swap = child
            if child + 1 <= end and array[swap] < array[child + 1]:
                swap = child + 1
            if swap == root:
                return
            else:
                # todo
                sorting_history(array, root, swap, -1, -1)
                array[root], array[swap] = array[swap], array[root]
                root = swap

    heapify(array, len(array))
    end = len(array) - 1
    while end > 0:
        # todo
        sorting_history(array, -1, -1, 0, end)
        array[end], array[0] = array[0], array[end]
        end -= 1
        sift_down(array, 0, end)
    sorting_history(array, -1, -1, -1, -1)


def quick_sort(array, sorting_history, left, right, *args):
    # Быстрая сортировка
    if left >= right:
        sorting_history(array, -1, -1, -1, -1)
        return
    index = left
    for j in range(left, right):
        # todo
        sorting_history(array, j, right, index, -1)
        if array[j] < array[right]:
            array[j], array[index] = array[index], array[j]
            index += 1
    array[index], array[right] = array[right], array[index]
    quick_sort(array, sorting_history, index + 1, right)
    quick_sort(array, sorting_history, left, index - 1)


def merge_sort(array, sorting_history, left, right):
    def merge(array, left, mid, right):
        nonlocal sorting_history
        L = array[left:mid + 1]
        R = array[mid + 1:right + 1]
        i = 0
        j = 0
        k = left
        while i < len(L) and j < len(R):
            sorting_history(array, left + i, mid + j, left, right)
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

    if left < right:
        mid = int((left + right) / 2)
        merge_sort(array, sorting_history, left, mid)
        merge_sort(array, sorting_history, mid + 1, right)
        merge(array, left, mid, right)
        sorting_history(array, -1, -1, -1, -1)


def counting_sort(array, sorting_history, *args):
    # Сортировка подсчетом
    size = len(array)
    array_copy = array.copy()
    count_array = [0 for _ in range(max(array_copy) + 2)]
    for i in range(size):
        count_array[array_copy[i]] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    for i in range(0, size):
        sorting_history(array, count_array[array_copy[size - i - 1]] - 1, -1, size - i - 1, -1)
        array[count_array[array_copy[size - i - 1]] - 1] = array_copy[size - i - 1]
        count_array[array_copy[size - i - 1]] -= 1
    sorting_history(array, -1, -1, -1, -1)


def gnome_sort(array, sorting_history, *args):
    # гномья сортировка
    i, size = 0, len(array)
    while i < size:
        if array[i - 1] <= array[i] or i == 0:
            sorting_history(array, i, i - 1, -1, -1)
            i += 1
        else:
            sorting_history(array, i, i - 1, -1, -1)
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
    sorting_history(array, -1, -1, -1, -1)
