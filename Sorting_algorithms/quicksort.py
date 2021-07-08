# Quick Sort

"""
QuickSort is a Divide and Conquer algorithm. It picks an elements as pivot and partitions the given array around the
picked pivot. There are many different versions of quick-sort that pick pivot in
different ways.

1. Always pick first element as pivot.
2. Always pick last element as pivot
3. Pick a random element as pivot.
4. pick median as pivot.
"""


def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


def quick_sort(start, end, array):
    if start < end:
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


arr = [10, 7, 8, 9, 1, 5]
quick_sort(0, len(arr) - 1, arr)

print(f'sorted array: {arr}')
