from math import ceil, floor


def bubble_sort(array, *args):
    # Сортировка пузырьком
    size = len(array)
    for i in range(size):
        for j in range(size - i - 1):
            # todo
            # handleDrawing(array, j, j + 1, -1, -1)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def shake_sort(array, *args):
    # Сортировка перемешиванием
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right, 1):
            # todo
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1
        for i in range(right, left, -1):
            # todo
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1
    return array


def comb_sort(array, *args):
    # Сортировка расческой

    def get_gap(prev_gap) -> int:
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
            # handleDrawing(array, idx, idx + gap, -1, -1)
            if array[idx] > array[idx + gap]:
                array[idx], array[idx + gap] = array[idx + gap], array[idx]
                swapped = True


def insert_sort(array, *args):
    # Сортировка вставками
    size = len(array)
    for i in range(1, size):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key:
            # todo
            # handleDrawing(array, j, -1, i, -1)
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def shell_sort(array, *args, gaps_type="ciura"):
    # Сортировка Шелла
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

    # different gap sequences
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
                # handleDrawing(array, j, j - gap, -1, -1)
                array[j] = array[j - gap]
                j -= gap
            # todo
            # handleDrawing(array, -1, -1, i, j)
            array[j] = temp


def binary_insertion_sort(array, *args):
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
        # handleDrawing(arr, start, end, mid, current)
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


def selection_sort(array, *args):
    # Сортировка выбором
    size = len(array)
    for i in range(size - 1):
        small_index = i
        for j in range(i, size):
            # todo
            # handleDrawing(array, j, -1, i, -1)
            if array[j] < array[small_index]:
                small_index = j
        array[i], array[small_index] = array[small_index], array[i]


def heap_sort(array, *args):
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
                # handleDrawing(array, root, swap, -1, -1)
                array[root], array[swap] = array[swap], array[root]
                root = swap

    heapify(array, len(array))
    end = len(array) - 1
    while end > 0:
        # todo
        # handleDrawing(array, -1, -1, 0, end, )
        array[end], array[0] = array[0], array[end]
        end -= 1
        sift_down(array, 0, end)


def quick_sort(array, left, right):
    # Быстрая сортировка
    if left >= right:
        return
    index = left
    for j in range(left, right):
        # todo
        # handleDrawing(array, j, right, index, -1)
        if array[j] < array[right]:
            array[j], array[index] = array[index], array[j]
            index += 1
    array[index], array[right] = array[right], array[index]
    quick_sort(array, index + 1, right)
    quick_sort(array, left, index - 1)


def merge_sort(array, left, right):
    # Сортировка слиянием
    def merge(array, left, mid, right):
        # Функция для слияния
        left = array[left:mid + 1]
        right = array[mid + 1:right + 1]
        i = 0
        j = 0
        k = left
        while i < len(left) and j < len(right):
            # todo
            # handleDrawing(array, left+i, mid+j, left, right)
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    if left < right:
        mid = int((left + right) / 2)
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)
