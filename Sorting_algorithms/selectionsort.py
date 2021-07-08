# Selection sort

"""

The selection sort algorithm sorts an array by repeatedly finding the 
minimum element (considering ascending order) from unsorted part and putting
it at the beginning. The algorithm maintains two sub arrays in a given array.
1) The sub array which is already sorted.
2) Remaining sub array which is unsorted.
"""


def selectionSort(arr):
    for i in range(len(arr)):
        min_id = i 
        for j in range(i+1, len(arr)):
            if arr[min_id] > arr[j]:
                min_id = j 
        arr[min_id], arr[i] = arr[i], arr[min_id]
    return arr 


array = [4, 8, 3, 1, 9]
selectionSort(array)
print(f'sorted array')
for x in range(len(array)):
    print(array[x], end=" ")
