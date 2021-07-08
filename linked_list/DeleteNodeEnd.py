# Deteting a node from the linked list

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None 

	def push(self,data):
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode

	def printList(self):
		print(f'Linked list: ')
		temp = self.head
		while temp:
			print(temp.val, end = " ")
			temp = temp.next

	def deleteNode(self):
		temp = self.head
		while temp.next.next:
			temp = temp.next

		temp.next = None

def main():
	l = LinkedList()
	l.push(5)
	l.push(8)
	l.push(4)
	l.push(3)
	l.printList()
	l.deleteNode()
	l.printList()

main()