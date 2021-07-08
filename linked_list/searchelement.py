# Search an element in a linked list(Iterative and recursive)

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

	def printList(self):
		temp = self.head
		while temp:
			print(temp.val, end = " ")
			temp = temp.next

	def searchelement(self, data):
		if self.head == None:
			return False
		temp = self.head
		while temp:
			if temp.val == data:
				return True
			temp = temp.next
		return False

	def recursearch(self,node, data):
		if self.head == None:
			return False
		elif node.val == data:
			return True
		else:
			return self.recursearch(node.next, data) 


# driver function
def main():
	L = LinkedList()
	L.push(1)
	L.push(9)
	L.push(7)
	L.push(3)
	L.push(5)
	L.printList()
	if L.searchelement(7):
		print(f'Number found')
	else:
		print(f'Number not found')

	if L.recursearch(L.head,5):
		print(f'Number found')
	else:
		print(f'Number not found')


main()
