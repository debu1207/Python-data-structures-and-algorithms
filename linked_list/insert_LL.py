# Linked list
# Inserting node at front of the linked list
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

# driver function
def main():
	L = LinkedList()
	L.push(1)
	L.push(9)
	L.push(7)
	L.push(3)
	L.push(5)
	L.printList()

if __name__ == '__main__':
	main()
