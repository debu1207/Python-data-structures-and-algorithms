class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		newnode = Node(data)

		newnode.next = self.head
		self.head = newnode

	def printList(self):
		temp = self.head
		print(f'Linked list: ')
		while temp:
			print(temp.val, end = " ")
			temp = temp.next

	def lengthLL(self):
		if self.head == None:
			return 0
		temp = self.head
		count = 0
		while temp:
			count += 1
			temp = temp.next

		return count

	def recurlen(self, node):
		if node == None:
			return 0
		else:
			return 1 + self.recurlen(node.next)

# driver function
def main():
	L = LinkedList()
	L.push(1)
	L.push(9)
	L.push(7)
	L.push(3)
	L.push(5)
	L.printList()
	print(f'Length of linked list: {L.lengthLL()}')
	print(f'Length of linked list: {L.recurlen(L.head)}')

if __name__ == '__main__':
	main()