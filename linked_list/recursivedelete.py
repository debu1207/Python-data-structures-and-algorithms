# recursively delete a node any where in the linked list

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

	def recurdelete(self, Node, data):
		if self.head == None:
			return
		if Node.next.val == data:
			Node.next = Node.next.next
			return
		return self.recurdelete(Node.next, data)



	def printList(self):
		print(f'Linked list: ')
		temp = self.head 
		while temp:
			print(temp.val, end = " ")
			temp = temp.next


def main():
	l = LinkedList()
	l.push(5)
	l.push(8)
	l.push(4)
	l.push(3)
	l.printList()
	l.recurdelete(l.head, 8)
	l.printList()

main()