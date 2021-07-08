# Delete node anywhere in the linked list.

class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
	
class LinkedList:
	def __init__(self):
		self.head = None

	def push(self,data):
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode

	def deletenode(self, data):
		# store head node
		temp = self.head
		if (temp is not None):
			if (temp.val == data):
				self.head = temp.next
				temp = None 
				return

		# search for the data key to be deleted, keep track of 
		# previous node as we need to change prev.next also

		while temp != None:
			if temp.val == data:
				break

			prev = temp
			temp = temp.next

		if temp == None:
			return

		prev.next = temp.next
		temp = None

	def printList(self):
		print(f'Linked list: ')
		temp = self.head 
		while temp:
			print(temp.val , end=" ")
			temp = temp.next

# driver function:
def main():
	l = LinkedList()
	l.push(4)
	l.push(2)
	l.push(9)
	l.push(7)
	l.printList()
	l.deletenode(9)
	l.printList()


main()



