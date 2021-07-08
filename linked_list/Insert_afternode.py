# Insert after a node

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

	def insertafter(self, prev_node,data):
		newnode = Node(data)
		temp = self.head
		while temp.val != prev_node:
			temp = temp.next

		newtemp = temp.next
		temp.next = newnode
		newnode.next = newtemp

	def printList(self):
		print(f'Linked list: ')
		temp = self.head
		while temp:
			print(temp.val, end = " ")
			temp = temp.next

# driver function
def main():
	l = LinkedList()
	for i in range(1,6):
		l.push(i)
	l.printList()
	l.insertafter(4, 100)
	l.printList()

if __name__ == '__main__':
	main()

