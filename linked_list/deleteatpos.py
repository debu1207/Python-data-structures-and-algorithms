# Delete a linked list node a give position in the LL

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

	def deletenode(self, pos):
		if self.head == None:
			return

		temp = self.head
		if pos == 0:
			self.head = temp.next
			temp = None
			return

		for i in range(pos-1):
			temp = temp.next
			if temp is None:
				break

		if temp is None:
			return

		if temp.next is None:
			return

		nexttemp = temp.next.next
		temp.next = None
		temp.next = nexttemp

	def printList(self):
		print(f'Linked list: ')
		temp = self.head
		while temp:
			print(temp.val , end = " ")
			temp = temp.next 

l = LinkedList()
l.push(1)
l.push(5)
l.push(8)
l.push(6)
l.push(7)
l.printList()
l.deletenode(3)
l.printList()
