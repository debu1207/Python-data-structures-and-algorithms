# inserting a node in a DLL

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None


class DoublyLL:
	def __init__(self):
		self.head = None


	def push(self, data):
		newnode = Node(data)
		newnode.next = self.head
		newnode.prev = None

		if self.head != None:
			self.head.prev = newnode
		self.head = newnode

	def printdll(self):
		if self.head == None:
			print(f'DLL is empty')
		temp = self.head
		print(temp.val, end = " ")
		temp = temp.next
		while (temp.next is not self.head):
			print(temp.val, end = " ")
			temp = temp.next


dll = DoublyLL()
dll.push(4)
dll.push(6)
dll.push(0)
dll.push(8)

dll.printdll()
