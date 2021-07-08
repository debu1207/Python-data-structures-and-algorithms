# Write a function to delete a linked list

class Node:
	def __init__(self,val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None 

	def push(self, data):
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode

	def deletelist(self):
		current = self.head
		while current:
			prev = current.next
			del current.val
			current = prev

	def printList(self):
		print(f'Linked list: ')
		temp = self.head
		while temp:
			print(temp.val , end = " ")
			temp = temp.next

l = LinkedList()
l.push(1)
l.push(1)
l.push(1)
l.push(1)
l.push(1)
l.printList()

l.deletelist()
print(f'Linked list deleted')


