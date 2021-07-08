# Insertion sort

"""
Algorithm:

1. Iterate from arr[1] to arr[n] over the array
2. compare the current element (key) to its predecessor
3. if the key element smaller than its predecessor, compare it to the elements
   before. Move the greater elements one position up to make
   space for the swapped element

"""


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    array = [8, 3, 2, 1, 4]
    insertionSort(array)
    print(f'\nSorted array: ')
    for x in array:
        print(x, end=" ")

"""

time complexity: O(n^2)
Auxiliary Space: O(1)

Insertion sort takes maximum time to sort if elements are sorted in reverse
order.

Algorithmic Paradigm: Incremental Approach
sorting in place: Yes
"""
