# Recursive insertion sort

def insertionsortrecur(arr, n):
	if n <= 1:
		return

	insertionsortrecur(arr, n-1)
	last = arr[n-1]
	j = n-2

	while (j >= 0 and arr[j] > last):
		arr[j + 1] = arr[j]
		j -= 1

	arr[j + 1] = last

def printlist(arr, n):
	for i in arr:
		print(i , end = " ")

arr = [12,11,13,5,6]
n = len(arr)
insertionsortrecur(arr, n)
printlist(arr, n)