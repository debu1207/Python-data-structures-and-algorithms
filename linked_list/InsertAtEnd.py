# Insert at the end of linked list

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
		print(f'Linked List: ')
		temp = self.head
		while temp:
			print(temp.val, end = " ")
			temp = temp.next

	def append(self, data):
		newnode = Node(data)
		temp = self.head
		while temp.next:
			temp=temp.next
		temp.next = newnode


l = LinkedList()
l.push(3)
l.push(4)
l.push(7)
l.printList()
l.append(8)
l.printList()


