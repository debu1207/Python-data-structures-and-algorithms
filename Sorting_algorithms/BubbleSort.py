"""
Bubble sort is the simplest algorithm that works by repeatedly swapping the
adjacent elements if they are in wrong order.

"""


def bubbleSort(arr):
    i = 0
    while i < len(arr):
        swap = False
        j = 0
        while j < len(arr) - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
            j += 1

        if not swap:
            break

        i += 1


if __name__ == "__main__":
    array = [4, 7, 3, 2, 8]
    bubbleSort(array)

    print(f'Sorted array: ')
    for x in array:
        print(x, end=" ")

# Worst and avg case time complexity: O(n*n)
# best time capacity: O(n)
